# Secure Cloud File Storage Using AWS

## Project Overview
A Python-based project that protects files by splitting them into smaller blocks, encrypting each block, and storing the encrypted blocks in Amazon S3.

## Problem Statement
Cloud files need protection against unauthorized access. This project encrypts file contents before uploading them to cloud storage.

## Technologies Used
- Python
- Amazon S3
- AWS CLI
- Boto3
- Cryptography (Fernet)

## How It Works
1. Read the input file.
2. Split the file into smaller blocks.
3. Encrypt each block.
4. Upload encrypted blocks to Amazon S3.
5. Download the encrypted blocks when needed.
6. Decrypt the downloaded data to recover the original file.

## Main Files
- `secure_storage.py` — splits and encrypts the input file.
- `upload_to_s3.py` — uploads encrypted blocks to S3.
- `download_from_s3.py` — downloads encrypted blocks.
- `decrypt_file.py` — decrypts downloaded data.
- `requirements.txt` — lists Python dependencies.

## Setup
Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials securely before running the S3 scripts.

## Security
- Never upload `secret.key` or AWS credentials to GitHub.
- Keep encryption keys secure.
- The current decryption script supports only one block; multi-block recovery is a future improvement.

## Future Improvements
- Support multi-block file recovery.
- Improve encryption-key management.
- Add file-integrity checks and error handling.
- Develop a user-friendly interface.

## Author
Bhumika Andure
