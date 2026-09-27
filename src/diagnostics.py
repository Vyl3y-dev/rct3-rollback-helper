import hashlib
import os
import winreg

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

def find_rct3(libraries):
    rct3_path = r"steamapps\common\RollerCoaster Tycoon 3 Complete Edition\RCT3.exe"

    for library in libraries:
        full_rct3_path = os.path.join(library, rct3_path)

        if os.path.exists(full_rct3_path):
            return full_rct3_path

    return None
    # rct3_path = r"C:\Program Files (x86)\Steam\steamapps\common\RollerCoaster Tycoon 3 Complete Edition\RCT3.exe"

    # if not os.path.exists(rct3_path):
    #     return None
    # else:
    #     return rct3_path

def find_steam():
    try:
        with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Valve\Steam"
            ) as key:
                steam_path, value_type = winreg.QueryValueEx(key, "SteamPath")
        
                return steam_path
    except FileNotFoundError:
        return None

def find_steam_libraries(steam_path):
    library_file = os.path.join(
        steam_path,
        "steamapps",
        "libraryfolders.vdf"
    )

    if not os.path.exists(library_file):
        return None

    libraries = []

    with open(library_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith('"path"'):
                parts = line.split('"')
                clean_path = parts[3].replace("\\\\", "\\")
                libraries.append(clean_path)
    return libraries