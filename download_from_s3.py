
import boto3
from pathlib import Path

BUCKET_NAME = "bhumika-secure-storage"
REGION = "ap-south-1"
S3_PREFIX = "encrypted_blocks/"

s3 = boto3.client("s3", region_name=REGION)

download_folder = Path("downloaded_blocks")
download_folder.mkdir(exist_ok=True)

# Find all encrypted blocks stored in S3
paginator = s3.get_paginator("list_objects_v2")
total_downloaded = 0

for page in paginator.paginate(Bucket=BUCKET_NAME, Prefix=S3_PREFIX):
    for obj in page.get("Contents", []):
        s3_key = obj["Key"]

        if not s3_key.endswith(".enc"):
            continue

        filename = Path(s3_key).name
        local_path = download_folder / filename

        s3.download_file(BUCKET_NAME, s3_key, str(local_path))

        print(f"Downloaded: {filename}")
        total_downloaded += 1

if total_downloaded == 0:
    print("No encrypted blocks found in S3.")
else:
    print(f"\nAll downloads complete! Total blocks: {total_downloaded}")
    print(f"Saved in: {download_folder}")
