from src.diagnostics import hash_file, identify_build, find_rct3, find_steam, find_steam_libraries

steam_path = find_steam()
print(steam_path)
if steam_path is not None:
    libraries = find_steam_libraries(steam_path)
    print(libraries)
    rct3_path = find_rct3(libraries)
    print(rct3_path)

    if rct3_path is not None:
        file_hash = hash_file(rct3_path)
        print(file_hash)
        game_build = identify_build(file_hash)
        print(game_build)

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
