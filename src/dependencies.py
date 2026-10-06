import hashlib
import os
import shutil
import tempfile
import urllib.request
import zipfile


DEPOT_DOWNLOADER_VERSION = "3.4.0"
DEPOT_DOWNLOADER_SHA256 = (
    "41c9e9f0df54b3ad02e67a11726756e5"
    "c73283bd7c2e1b04acfa5ae4c2ed3767"
)

DEPOT_DOWNLOADER_URL = (
    "https://github.com/SteamRE/DepotDownloader/releases/download/"
    f"DepotDownloader_{DEPOT_DOWNLOADER_VERSION}/"
    f"DepotDownloader-windows-x64.zip"
)


def get_app_data_directory():
    local_app_data = os.getenv("LOCALAPPDATA")

    if not local_app_data:
        raise RuntimeError("Windows LOCALAPPDATA directory could not be found.")

    app_data_directory = os.path.join(
        local_app_data,
        "RCT3 Compatibility Helper",
    )

    os.makedirs(app_data_directory, exist_ok=True)
    return app_data_directory


def get_dependency_directory():
    return os.path.join(
        get_app_data_directory(),
        "dependencies",
        "DepotDownloader",
    )


def get_depot_downloader_path():
    return os.path.join(
        get_dependency_directory(),
        "DepotDownloader.exe",
    )


def find_depot_downloader():
    depot_downloader_path = get_depot_downloader_path()

    if os.path.exists(depot_downloader_path):
        return depot_downloader_path

    return None


def download_depot_downloader():
    dependency_directory = get_dependency_directory()

    os.makedirs(
        dependency_directory,
        exist_ok=True,
    )

    with tempfile.TemporaryDirectory() as temporary_directory:
        archive_path = os.path.join(
            temporary_directory,
            "DepotDownloader.zip",
        )

        print("Downloading DepotDownloader...")

        urllib.request.urlretrieve(
            DEPOT_DOWNLOADER_URL,
            archive_path,
        )

        archive_hash = hashlib.sha256()

        with open(archive_path, "rb") as archive_file:
            for chunk in iter(lambda: archive_file.read(8192), b""):
                archive_hash.update(chunk)

        if archive_hash.hexdigest() != DEPOT_DOWNLOADER_SHA256:
            print("DepotDownloader verification failed.")
            return None

        print("DepotDownloader verified.")
        print("Extracting DepotDownloader...")

        with zipfile.ZipFile(archive_path, "r") as archive:
            archive.extractall(dependency_directory)

    depot_downloader_path = get_depot_downloader_path()

    if not os.path.exists(depot_downloader_path):
        return None

    return depot_downloader_path


def get_depot_downloader():
    depot_downloader_path = find_depot_downloader()

    if depot_downloader_path is not None:
        return depot_downloader_path

    return download_depot_downloader()