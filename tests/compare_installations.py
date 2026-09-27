import os
from src.diagnostics import hash_file


def inventory_folder(folder_path):
    inventory = {}

    for root, directories, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, folder_path)

            inventory[relative_path] = {
                "size": os.path.getsize(full_path),
                "hash": hash_file(full_path)
            }

    return inventory


def compare_installations(working_folder, broken_folder):
    working = inventory_folder(working_folder)
    broken = inventory_folder(broken_folder)

    working_files = set(working.keys())
    broken_files = set(broken.keys())

    only_working = working_files - broken_files
    only_broken = broken_files - working_files
    shared_files = working_files & broken_files

    different = []

    for file_path in shared_files:
        if working[file_path]["hash"] != broken[file_path]["hash"]:
            different.append(file_path)

    print("\n=== ONLY IN WORKING INSTALLATION ===")
    if only_working:
        for file_path in sorted(only_working):
            print(file_path)
    else:
        print("None")

    print("\n=== ONLY IN BROKEN INSTALLATION ===")
    if only_broken:
        for file_path in sorted(only_broken):
            print(file_path)
    else:
        print("None")

    print("\n=== DIFFERENT FILES ===")
    if different:
        for file_path in sorted(different):
            print(file_path)

            print(
                f"  Working: "
                f"{working[file_path]['size']} bytes | "
                f"{working[file_path]['hash']}"
            )

            print(
                f"  Broken:  "
                f"{broken[file_path]['size']} bytes | "
                f"{broken[file_path]['hash']}"
            )
    else:
        print("None")

    print("\n=== SUMMARY ===")
    print(f"Working installation files: {len(working)}")
    print(f"Broken installation files:  {len(broken)}")
    print(f"Only in working:             {len(only_working)}")
    print(f"Only in broken:              {len(only_broken)}")
    print(f"Different contents:          {len(different)}")


if __name__ == "__main__":
    working_folder = input(
        "Path to WORKING RCT3 test folder: "
    ).strip().strip('"')

    broken_folder = input(
        "Path to BROKEN RCT3 Steam folder: "
    ).strip().strip('"')

    print("\nInventorying installations...")
    print("This may take a moment.\n")

    compare_installations(
        working_folder,
        broken_folder
    )