import os
from cryptography.fernet import Fernet

def load_or_generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
    return open("key.key", "rb").read()

def encrypt_folder(folder_path):
    key = load_or_generate_key()
    fernet = Fernet(key)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)

            with open(file_path, "wb") as f:
                f.write(encrypted)

            print(f"Encrypted: {file}")

if __name__ == "__main__":
    encrypt_folder("test_folder")
    print("\nEncryption completed successfully!")
