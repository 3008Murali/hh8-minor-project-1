import os
from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def decrypt_folder(folder_path):
    key = load_key()
    fernet = Fernet(key)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                encrypted_data = f.read()

            decrypted = fernet.decrypt(encrypted_data)

            with open(file_path, "wb") as f:
                f.write(decrypted)

            print(f"Decrypted: {file}")

if __name__ == "__main__":
    decrypt_folder("test_folder")
    print("\nDecryption completed successfully!")
