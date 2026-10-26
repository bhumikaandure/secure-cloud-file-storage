
from cryptography.fernet import Fernet
from pathlib import Path

# Load the encryption key
key = Path("secret.key").read_bytes()
cipher = Fernet(key)

# Folder containing downloaded encrypted blocks
input_folder = Path("downloaded_blocks")

# Find all encrypted blocks and sort them by block number
encrypted_blocks = sorted(
    input_folder.glob("block_*.enc"),
    key=lambda path: int(path.stem.split("_")[1])
)

if not encrypted_blocks:
    raise FileNotFoundError("No encrypted blocks found in downloaded_blocks.")

# Decrypt and combine all blocks in the correct order
recovered_data = bytearray()

for block_path in encrypted_blocks:
    encrypted_data = block_path.read_bytes()
    decrypted_data = cipher.decrypt(encrypted_data)
    recovered_data.extend(decrypted_data)
    print(f"Decrypted: {block_path.name}")

# Save the complete recovered file
output_path = Path("recovered_sample.txt")
output_path.write_bytes(recovered_data)

print("\nFile recovered successfully!")
print(f"Recovered file: {output_path}")
print(f"Recovered size: {len(recovered_data)} bytes")
print(f"Total blocks decrypted: {len(encrypted_blocks)}")
