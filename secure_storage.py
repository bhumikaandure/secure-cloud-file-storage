from cryptography.fernet import Fernet
from pathlib import Path
import json

# Project settings
INPUT_FILE = "sample.txt"
CHUNK_SIZE = 1024  # 1 KB per block

# Load the encryption key created earlier
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Create a folder for encrypted blocks
output_folder = Path("encrypted_blocks")
output_folder.mkdir(exist_ok=True)

# Read and split the original file
with open(INPUT_FILE, "rb") as file:
    block_number = 0

    while True:
        block = file.read(CHUNK_SIZE)

        if not block:
            break

        # Encrypt each block
        encrypted_block = cipher.encrypt(block)

        # Save encrypted block
        block_path = output_folder / f"block_{block_number}.enc"
        block_path.write_bytes(encrypted_block)

        print(f"Block {block_number} encrypted successfully")
        block_number += 1

print(f"\nFile split and encrypted successfully!")
print(f"Total blocks: {block_number}")
print(f"Encrypted blocks saved in: {output_folder}")