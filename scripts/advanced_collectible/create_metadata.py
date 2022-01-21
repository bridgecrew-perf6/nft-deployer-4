from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed 
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests


def main():
    advanced_collectible = AdvancedCollectible[-1]
    num_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {num_of_advanced_collectibles} collectibles!")
    for token_id in range(num_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        
        print(metadata_file_name)

        collectible_metadata = metadata_template


        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists")
        else:
            print(f"Creating metadata file: {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed}"
            print(collectible_metadata)
            image_uri = upload_to_ipfs()
            collectible_metadata["image"] = image_uri
            image_path =  "./img/" + breed.lower().replace("_", "-") + ".png"

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # upload stuff...




