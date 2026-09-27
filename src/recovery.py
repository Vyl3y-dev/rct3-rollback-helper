import os
import shutil
from src.diagnostics import hash_file, LEGACY_HASH, CURRENT_HASH

RCT3_APP_ID = "1368820"
RCT3_DEPOT_ID = "1368821"
LEGACY_MANIFEST_ID = "3464953341930095826"

def get_legacy_download_command():
    legacy_download = f"download_depot {RCT3_APP_ID} {RCT3_DEPOT_ID} {LEGACY_MANIFEST_ID}"
    return legacy_download

def get_legacy_depot_path(steam_path):
    legacy_depot_path = os.path.join(steam_path, "steamapps", "content", f"app_{RCT3_APP_ID}", f"depot_{RCT3_DEPOT_ID}")
    return legacy_depot_path

def find_legacy_executable(legacy_depot_path):
    legacy_exe_path = os.path.join(legacy_depot_path, "RCT3.exe")

    if os.path.exists(legacy_exe_path):
        return legacy_exe_path
    else:
        return None

def verify_legacy_executable(legacy_exe_path):
    legacy_hash = hash_file(legacy_exe_path)

    if legacy_hash == LEGACY_HASH:
        return True
    else:
        return False


def get_backup_path(rct3_path):
    game_directory = os.path.dirname(rct3_path)
    backup_directory = os.path.join(game_directory, "RCT3CommunityFix_Backup")
    return backup_directory

def create_backup_path(backup_directory):
    os.makedirs(backup_directory, exist_ok=True)

def backup_current_executable(rct3_path, backup_directory):
    backup_file_path = os.path.join(backup_directory, "RCT3.exe")

    if os.path.exists(backup_file_path):
        print("Backup already exists")

    else:
        shutil.copy2(rct3_path, backup_file_path)
        print("Backup successful")

    return backup_file_path

def verify_backup_executable(rct3_path, backup_file_path):
    original_hash = hash_file(rct3_path)
    backup_hash = hash_file(backup_file_path)

    if original_hash == backup_hash:
        return True
    else:
        return False

def install_legacy_executable(legacy_exe_path, rct3_path):
    print(f"Source: {legacy_exe_path}")
    print(f"Destination: {rct3_path}")

    print(f"Source hash before copy: {hash_file(legacy_exe_path)}")
    print(f"Destination hash before copy: {hash_file(rct3_path)}")

    shutil.copy2(legacy_exe_path, rct3_path)

    installed_hash = hash_file(rct3_path)

    print(f"Destination hash after copy: {installed_hash}")
    print(f"Expected legacy hash: {LEGACY_HASH}")

    if installed_hash == LEGACY_HASH:
        return True
    else:
        return False

def restore_current_executable(backup_file_path, rct3_path):

    shutil.copy2(backup_file_path, rct3_path)
    restored_hash = hash_file(rct3_path)

    if restored_hash == CURRENT_HASH:
        return True
    else:
        return False

def verify_restore_executable(backup_directory):
    backup_file_path = os.path.join(backup_directory, "RCT3.exe")

    if not os.path.exists(backup_file_path):
        return False

    backup_hash = hash_file(backup_file_path)

    if backup_hash == CURRENT_HASH:
        return True
    else:
        return False