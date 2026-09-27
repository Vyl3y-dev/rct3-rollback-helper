import os
from src.diagnostics import hash_file, identify_build, find_rct3, find_steam, find_steam_libraries
from src.recovery import get_legacy_download_command, get_legacy_depot_path, find_legacy_executable, verify_legacy_executable, get_backup_path, create_backup_path, backup_current_executable, verify_backup_executable, install_legacy_executable
print(hash_file(r"C:\Users\vcmun\Desktop\RCT3-Test\RCT3.exe"))
print("RCT3 Community Fix")
print("-------------------")
print()

print("Checking Steam installation...")
steam_path = find_steam()

if steam_path is not None:
    print(f"Steam found: {steam_path}")
    print("-------------------")
    print()

    print("Checking Steam library location(s)...")
    libraries = find_steam_libraries(steam_path)
    print("Steam libraries located:")
    for library in libraries:
        print(f"  {library}")
    print("-------------------")
    print()

    print("Checking RCT3 installation...")
    rct3_path = find_rct3(libraries)
    print(f"RCT3 found: {rct3_path}")
    print("-------------------")
    print()

    if rct3_path is not None:
        print("Hashing RCT3.exe...")
        file_hash = hash_file(rct3_path)
        print(f"File hashed: {file_hash}")
        print("-------------------")
        print()

        print("Identifying game build...")
        game_build = identify_build(file_hash)
        if game_build == "legacy":
            print("Known working legacy executable detected.")

        elif game_build == "current":
            print("Known affected post-March 2026 executable detected.")
            print("Recover build available.")
            print("Steam depot command: ")
            print(get_legacy_download_command())
            legacy_depot_path = get_legacy_depot_path(steam_path)
            print(legacy_depot_path)
            legacy_exe_path = find_legacy_executable(legacy_depot_path)

            if legacy_exe_path is not None:
                legacy_verified = verify_legacy_executable(legacy_exe_path)

                if legacy_verified:
                    print("Legacy executable verified.")

                    backup_path = get_backup_path(rct3_path)

                    create_backup_path(backup_path)

                    backup_file_path = backup_current_executable(
                        rct3_path,
                        backup_path
                    )

                    verify_backup_executable(
                        rct3_path,
                        backup_file_path
                    )

                    install_legacy_executable(legacy_exe_path, rct3_path)

                else:
                    print("Legacy executable verification failed. Recovery stopped.")

            else:
                print("Legacy executable not found.")

        else:
            print("Unknown RCT3 executable detected. No changes will be made.")

    else:
        print("RCT3 is not installed")

else:
    print("Steam is not installed")


# rct3_path = find_rct3()
# steam_path = find_steam()
# if steam_path is not None:
#     print(steam_path)
#     libraries = find_steam_libraries(steam_path)
#     print(libraries)
#     if rct3_path is not None:
#         # file_input_path = input("Paste your file path here: ")
        
#         file_hash = hash_file(rct3_path)
#         print(file_hash)
#         game_build = identify_build(file_hash)
#         print(game_build)
#     else:
#         print("RCT3 is not installed")
# else:
#     print("Steam not installed")
