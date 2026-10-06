import os
import subprocess

from src.diagnostics import hash_file, LEGACY_HASH


RCT3_APP_ID = "1368820"
RCT3_DEPOT_ID = "1368821"
LEGACY_MANIFEST_ID = "3464953341930095826"


def get_downloaded_legacy_exe_path(download_directory):
    return os.path.join(download_directory, "RCT3.exe")


def download_legacy_executable(
        depot_downloader_exe_path,
        download_directory
):
    os.makedirs(download_directory, exist_ok=True)

    filelist_path = os.path.join(
        download_directory,
        "rct3_filelist.txt",
    )

    with open(filelist_path, "w") as file:
        file.write("RCT3.exe\n")

    command = [
        depot_downloader_exe_path,
        "-app", RCT3_APP_ID,
        "-depot", RCT3_DEPOT_ID,
        "-manifest", LEGACY_MANIFEST_ID,
        "-qr",
        "-dir", download_directory,
        "-filelist", filelist_path,
    ]

    creation_flags = 0

    if os.name == "nt":
        creation_flags = subprocess.CREATE_NEW_CONSOLE

    result = subprocess.run(
        command,
        creationflags=creation_flags,
    )

    return result.returncode == 0


def verify_legacy_exe_download(download_directory):
    legacy_exe_path = get_downloaded_legacy_exe_path(
        download_directory
    )

    if not os.path.exists(legacy_exe_path):
        return False

    return hash_file(legacy_exe_path) == LEGACY_HASH
