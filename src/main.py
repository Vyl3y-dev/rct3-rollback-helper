from src.diagnostics import hash_file, identify_build, find_rct3, find_steam, find_steam_libraries

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
