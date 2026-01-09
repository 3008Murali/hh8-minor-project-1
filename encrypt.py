import os
from cryptography.fernet import Fernet
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    return open("key.key", "rb").read()
def encrypt_folder(folder_path):
    key = load_key()
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
    if not os.path.exists("key.key"):
        generate_key()

    encrypt_folder("test_folder")
    print("\nEncryption completed successfully!")

