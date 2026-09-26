import hashlib
import os

LEGACY_HASH = "e2273b00242dfbc23e72f0a20a64a88528aff01543534309f4d46b7d720695c1"
CURRENT_HASH = "1c9316e728d67aaa3bfe36d0a1634f3139582927440a5467c351e4c949b5b21d"

def hash_file(file_path):
    if not os.path.exists(file_path):
        return "this path doesn't exist"
    try:
        with open(file_path, "rb") as f:
            contents = f.read()
            file_hash = hashlib.sha256(contents)
            return file_hash.hexdigest()
    except (FileNotFoundError):
        return "this file doesn't exist"

def identify_build(file_hash):
    if file_hash == LEGACY_HASH:
        return "legacy"
    elif file_hash == CURRENT_HASH:
        return "current"
    else:
        return "unknown"

def find_rct3():
    rct3_path = r"C:\Program Files (x86)\Steam\steamapps\common\RollerCoaster Tycoon 3 Complete Edition\RCT3.exe"

    if not os.path.exists(rct3_path):
        return None
    else:
        return rct3_path