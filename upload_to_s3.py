
import boto3
from pathlib import Path

BUCKET_NAME = "bhumika-secure-storage"
REGION = "ap-south-1"
BLOCK_FOLDER = Path("encrypted_blocks")

s3 = boto3.client("s3", region_name=REGION)

for block_path in BLOCK_FOLDER.glob("*.enc"):
    s3_key = f"encrypted_blocks/{block_path.name}"

    s3.upload_file(
        str(block_path),
        BUCKET_NAME,
        s3_key
    )

    print(f"Uploaded: {block_path.name}")

print("All encrypted blocks uploaded successfully!")
