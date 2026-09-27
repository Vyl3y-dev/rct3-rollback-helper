import hashlib
import os

def simple_file_hasher():
    file_path = input("Enter file path for game: ")
    print(file_path)

    if not os.path.exists(file_path):
        return "this path doesn't exist"
    try:
        with open(file_path, "rb") as f:
            contents = f.read()
            file_hash = hashlib.sha256(contents)
            return file_hash.hexdigest()
    except (FileNotFoundError):
        return "this file doesn't exist"


if __name__ == "__main__":
    print(simple_file_hasher())