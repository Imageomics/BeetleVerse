import os
import time
import json
import uuid
import argparse
import numpy as np
import pandas as pd
import urllib.request
from tqdm import tqdm
from urllib.error import URLError, HTTPError
from PIL import Image



def extract_taxon_name(value):
    if isinstance(value, str) and '(' in value and ')' in value:
        return value.split('(')[-1].split(')')[0]
    return value


def get_taxon_path(row, base_dir):

    path_parts = []

    for col in ["Phylum", "Class", "Order", "Family", "Genus", "Species"]:
        if pd.notna(row[col]):
            path_parts.append(str(row[col]).split(' ')[-1])

    return os.path.join(base_dir, *path_parts)


def download_image(image_url, image_path, retries=3, delay=10):

    for attempt in range(retries):
        try:
            urllib.request.urlretrieve(image_url, image_path)
            return True

        except (URLError, HTTPError) as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                print(f"Failed: {image_url}\nError: {e}")
                return False

        except Exception as e:
            print(f"Unexpected error: {e}")
            return False


def is_corrupted(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()
        return False
    except Exception:
        return True




def build_dataset(json_path, output_csv):

    with open(json_path, "r") as f:
        data = json.load(f)

    insect_records = data["insect_records"]
    descrp_records = data["description_records"]

    # filter Carabidae
    carabid_records = [
        r for r in insect_records
        if "carabidae" in r.get("Family", "").lower()
    ]

    columns = [
        "id", "Phylum", "Subphylum", "Class", "Order",
        "Suborder", "Family", "Subfamily", "Tribe",
        "Genus", "Species", "image_url"
    ]

    df = pd.DataFrame([{col: r.get(col, np.nan) for col in columns} for r in carabid_records])

    taxonomic_fields = ["Phylum", "Subphylum", "Class", "Order",
                         "Suborder", "Family", "Subfamily",
                         "Tribe", "Genus", "Species"]

    df[taxonomic_fields] = df[taxonomic_fields].apply(lambda col: col.map(extract_taxon_name))

    df["image_uuid"] = [str(uuid.uuid4()) for _ in range(len(df))]

    df.to_csv(output_csv, index=False)

    print(f"Dataset saved -> {output_csv}")

    return df




def download_images(df, image_root, output_csv):

    paths = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Downloading images"):

        taxon_path = get_taxon_path(row, image_root)
        os.makedirs(taxon_path, exist_ok=True)

        image_url = row["image_url"]
        image_uuid = row["image_uuid"]

        image_path = os.path.join(taxon_path, f"{image_uuid}.png")

        if download_image(image_url, image_path):
            paths.append(image_path)
        else:
            paths.append(np.nan)

    df["image_local_path"] = paths

    df.to_csv(output_csv, index=False)

    print(f"Images downloaded + CSV saved -> {output_csv}")

    return df



def clean_corrupted(df, output_csv):

    corrupted = df[df["image_local_path"].apply(is_corrupted)]

    for path in corrupted["image_local_path"]:
        if isinstance(path, str) and os.path.exists(path):
            os.remove(path)

    df = df[~df["image_local_path"].isin(corrupted["image_local_path"])]

    print(f"Removed {len(corrupted)} corrupted images")

    # final recheck
    still_bad = df[df["image_local_path"].apply(is_corrupted)]

    if len(still_bad) == 0:
        df.to_csv(output_csv, index=False)
        print(f"Final cleaned dataset saved -> {output_csv}")

    return df




def main(args):

    df = build_dataset(args.json_path, args.output_csv_raw)

    if args.download:
        df = download_images(df, args.image_dir, args.output_csv_downloaded)

    if args.clean:
        df = pd.read_csv(args.output_csv_downloaded)
        df = clean_corrupted(df, args.output_csv_final)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--json_path", required=True, help="Path to input JSON file")

    parser.add_argument("--image_dir", required=True, help="Base directory for images")

    parser.add_argument("--output_csv_raw", required=True, help="Raw dataset CSV output")

    parser.add_argument("--output_csv_downloaded", required=True, help="CSV after downloading images")

    parser.add_argument("--output_csv_final", required=True, help="Final cleaned CSV")

    parser.add_argument("--download", action="store_true", help="Download images")
    parser.add_argument("--clean", action="store_true", help="Clean corrupted images")

    args = parser.parse_args()

    main(args)