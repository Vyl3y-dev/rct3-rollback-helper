import os
from src.dependencies import get_app_data_directory, get_depot_downloader
from src.diagnostics import hash_file, identify_build, find_rct3, find_steam, find_steam_libraries
from src.recovery import (
    get_backup_path,
    create_backup_path,
    backup_current_executable,
    verify_backup_executable,
    install_legacy_executable,
    restore_current_executable,
    verify_restore_executable,
)
from src.steam_depot import (
    download_legacy_executable,
    get_downloaded_legacy_exe_path,
    verify_legacy_exe_download,
)


def recover_rct3(download_directory=None):
    """Temporary controller until the GUI becomes the application controller."""

    steam_path = find_steam()
    if steam_path is None:
        return False, "Steam is not installed."

    libraries = find_steam_libraries(steam_path)
    rct3_path = find_rct3(libraries)
    if rct3_path is None:
        return False, "RCT3 is not installed."

    game_build = identify_build(hash_file(rct3_path))

    if game_build == "legacy":
        return True, "Known working legacy executable is already installed."

    if game_build != "current":
        return False, "Unknown RCT3 executable detected. No changes were made."

    depot_downloader_exe_path = get_depot_downloader()

    if depot_downloader_exe_path is None:
        return False, "DepotDownloader could not be installed. Recovery stopped."
    
    if download_directory is None:
        download_directory = os.path.join(
            get_app_data_directory(),
            "downloads",
            "legacy",
        )

    if not download_legacy_executable(
        depot_downloader_exe_path,
        download_directory,
    ):
        return False, "Legacy executable download failed. Recovery stopped."

    if not verify_legacy_exe_download(download_directory):
        return False, "Legacy executable verification failed. Recovery stopped."

    legacy_exe_path = get_downloaded_legacy_exe_path(download_directory)

    backup_directory = get_backup_path(rct3_path)
    create_backup_path(backup_directory)

    backup_file_path = backup_current_executable(
        rct3_path,
        backup_directory,
    )

    if not verify_backup_executable(rct3_path, backup_file_path):
        return False, "Backup verification failed. Recovery stopped."

    if not install_legacy_executable(legacy_exe_path, rct3_path):
        return False, "Installation verification failed."

    return True, "Compatibility fix installed successfully."


def restore_rct3():
    """Restore the backed-up current executable after validating it."""

    steam_path = find_steam()
    if steam_path is None:
        return False, "Steam is not installed."

    libraries = find_steam_libraries(steam_path)
    rct3_path = find_rct3(libraries)
    if rct3_path is None:
        return False, "RCT3 is not installed."

    game_build = identify_build(hash_file(rct3_path))

    if game_build == "current":
        return True, "The original current executable is already installed."

    if game_build != "legacy":
        return False, "Unknown RCT3 executable detected. No changes were made."

    backup_directory = get_backup_path(rct3_path)

    if not verify_restore_executable(backup_directory):
        return False, "A verified original executable backup was not found. Restore stopped."

    backup_file_path = os.path.join(
        backup_directory,
        "RCT3.exe",
    )

    if not restore_current_executable(backup_file_path, rct3_path):
        return False, "Restore verification failed."

    return True, "Original RCT3 executable restored successfully."


# Temporary development entry point.
# The GUI will replace this once it becomes the application's controller.
if __name__ == "__main__":
    print("Yoan I love you 💖")

    success, message = recover_rct3()

    print(message)
