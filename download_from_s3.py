
import boto3
from pathlib import Path

BUCKET_NAME = "bhumika-secure-storage"
REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=REGION)

download_folder = Path("downloaded_blocks")
download_folder.mkdir(exist_ok=True)

s3_key = "encrypted_blocks/block_0.enc"
local_path = download_folder / "block_0.enc"

s3.download_file(BUCKET_NAME, s3_key, str(local_path))

print("Encrypted block downloaded successfully!")
print(f"Saved at: {local_path}")
