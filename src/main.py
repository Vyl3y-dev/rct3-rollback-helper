from src.diagnostics import hash_file, identify_build, find_rct3

rct3_path = find_rct3()
if rct3_path is not None:
    # file_input_path = input("Paste your file path here: ")
    
    file_hash = hash_file(rct3_path)
    print(file_hash)
    game_build = identify_build(file_hash)
    print(game_build)
else:
    print("RCT3 is not installed")