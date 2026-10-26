
from cryptography.fernet import Fernet
from pathlib import Path

# Load the original encryption key
key = Path("secret.key").read_bytes()
cipher = Fernet(key)

# Read the encrypted block downloaded from S3
encrypted_path = Path("downloaded_blocks/block_0.enc")
encrypted_data = encrypted_path.read_bytes()

# Decrypt the block
decrypted_data = cipher.decrypt(encrypted_data)

# Save the recovered original file
output_path = Path("recovered_sample.txt")
output_path.write_bytes(decrypted_data)

print("File decrypted successfully!")
print(f"Recovered file: {output_path}")
print(f"Recovered size: {len(decrypted_data)} bytes")
