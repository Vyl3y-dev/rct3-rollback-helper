from src.diagnostics import hash_file, identify_build


file_path_input = input("Paste your file path here: ")
file_hash = hash_file(file_path_input)
print(file_hash)
game_build = identify_build(file_hash)
print(game_build)