import os
import argparse
import requests
import numpy as np
import pandas as pd
from PIL import Image


def get_species_by_key(species_key):
    url = f"https://api.gbif.org/v1/species/{species_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return {
            "species": data.get("scientificName") or np.nan,
            "canonicalName": data.get("canonicalName") or np.nan,
            "rank": data.get("rank") or np.nan,
            "kingdom": data.get("kingdom") or np.nan,
            "phylum": data.get("phylum") or np.nan,
            "class": data.get("class") or np.nan,
            "order": data.get("order") or np.nan,
            "family": data.get("family") or np.nan,
            "genus": data.get("genus") or np.nan,
            "speciesKey": data.get("key") or np.nan
        }

    return None


def is_corrupted(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()
        return False
    except Exception:
        return True


def main(data_dir, output_csv):

    species_keys_list = os.listdir(data_dir)

    columns = [
        "ImageFileName",
        "ImageFilePath",
        "Kingdom",
        "Phylum",
        "Class",
        "Order",
        "Family",
        "Genus",
        "Species",
        "CanonicalName"
    ]

    df = pd.DataFrame(columns=columns)

    for key in species_keys_list:

        key_dir = os.path.join(data_dir, key)

        if not os.path.isdir(key_dir):
            continue

        species_info = get_species_by_key(key)

        if species_info is None:
            continue

        species = species_info["species"]
        species = " ".join(species.split()[:2]) if isinstance(species, str) else np.nan

        im_files = os.listdir(key_dir)

        for im_file in im_files:
            im_path = os.path.join(key_dir, im_file)

            df = pd.concat([df, pd.DataFrame([{
                "ImageFileName": im_file,
                "ImageFilePath": im_path,
                "Kingdom": species_info["kingdom"],
                "Phylum": species_info["phylum"],
                "Class": species_info["class"],
                "Order": species_info["order"],
                "Family": species_info["family"],
                "Genus": species_info["genus"],
                "Species": species,
                "CanonicalName": species_info["canonicalName"]
            }])], ignore_index=True)

    corrupted_images = df[df["ImageFilePath"].apply(is_corrupted)]

    if len(corrupted_images) == 0:
        print(f"All {len(corrupted_images)} instances verified!")

        df.to_csv(output_csv, index=False)
        print(f"Saved CSV to: {output_csv}")
    else:
        print(f"Found {len(corrupted_images)} corrupted images (not saving CSV).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data_dir",
        type=str,
        required=True,
        help="Path to dataset directory"
    )

    parser.add_argument(
        "--output_csv",
        type=str,
        required=True,
        help="Path to output CSV file"
    )

    args = parser.parse_args()

    main(args.data_dir, args.output_csv)