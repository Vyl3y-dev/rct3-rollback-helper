import os
import shutil


GROUPS = {
    "languages": [
        r"gui\Danish.common.ovl",
        r"gui\Danish.unique.ovl",
        r"gui\Dutch.common.ovl",
        r"gui\Dutch.unique.ovl",
        r"gui\English.common.ovl",
        r"gui\English.unique.ovl",
        r"gui\Finnish.common.ovl",
        r"gui\Finnish.unique.ovl",
        r"gui\French.common.ovl",
        r"gui\French.unique.ovl",
        r"gui\German.common.ovl",
        r"gui\German.unique.ovl",
        r"gui\Italian.common.ovl",
        r"gui\Italian.unique.ovl",
        r"gui\Norwegian.common.ovl",
        r"gui\Norwegian.unique.ovl",
        r"gui\Spanish.common.ovl",
        r"gui\Spanish.unique.ovl",
        r"gui\Swedish.common.ovl",
        r"gui\Swedish.unique.ovl",

        r"gui\SChinese.common.ovl",
        r"gui\SChinese.unique.ovl",
        r"gui\800\SChinese.common.ovl",
        r"gui\800\SChinese.unique.ovl",
        r"gui\1024\SChinese.common.ovl",
        r"gui\1024\SChinese.unique.ovl",
        r"gui\1280\SChinese.common.ovl",
        r"gui\1280\SChinese.unique.ovl",
    ],

    "resolution": [
        r"gui\800\Resolution.common.ovl",
        r"gui\800\Resolution.unique.ovl",
        r"gui\1024\Resolution.common.ovl",
        r"gui\1024\Resolution.unique.ovl",
        r"gui\1280\Resolution.common.ovl",
        r"gui\1280\Resolution.unique.ovl",
    ],

    "front_ui": [
        r"gui\Banner\Banner.common.ovl",
        r"gui\Banner\Banner.unique.ovl",

        r"gui\FrontScreen\ScenarioLogos\Base\FrontScreen.common.ovl",
        r"gui\FrontScreen\ScenarioLogos\Base\FrontScreen.unique.ovl",

        r"gui\FrontScreen\ScenarioLogos\Wild\FrontScreen.common.ovl",
        r"gui\FrontScreen\ScenarioLogos\Wild\FrontScreen.unique.ovl",

        r"gui\FrontScreen\UpdatedTShirt\FrontScreen_UpdatedTShirt.common.ovl",
        r"gui\FrontScreen\UpdatedTShirt\FrontScreen_UpdatedTShirt.unique.ovl",

        r"gui\LoadingScreen\LoadingScreen.common.ovl",
        r"gui\LoadingScreen\LoadingScreen.unique.ovl",

        r"gui\UpdatedIcons\UpdatedIcons.common.ovl",
        r"gui\UpdatedIcons\UpdatedIcons.unique.ovl",
    ],

    "cache": [
        "SCCache.bin",
        "STCache.bin",
    ],
}


def apply_group(current_folder, experiment_folder, group_name):
    files = GROUPS[group_name]

    print(f"\nApplying current '{group_name}' files...\n")

    for relative_path in files:
        source = os.path.join(current_folder, relative_path)
        destination = os.path.join(experiment_folder, relative_path)

        if not os.path.exists(source):
            print(f"SKIPPED: {relative_path}")
            continue

        os.makedirs(
            os.path.dirname(destination),
            exist_ok=True
        )

        shutil.copy2(source, destination)

        print(f"COPIED: {relative_path}")


def show_groups():
    print("\nAvailable groups:")

    for group_name in GROUPS:
        print(f"  - {group_name}")


if __name__ == "__main__":
    print("\nRCT3 Resource Test Utility")
    print("--------------------------")
    print("This tool modifies the EXPERIMENT folder only.\n")

    current_folder = input(
        "Path to CURRENT Steam installation: "
    ).strip().strip('"')

    experiment_folder = input(
        "Path to disposable EXPERIMENT folder: "
    ).strip().strip('"')

    show_groups()

    group_name = input(
        "\nGroup to apply: "
    ).strip().lower()

    if group_name not in GROUPS:
        print("\nUnknown group.")
        raise SystemExit

    print("\nWARNING:")
    print("Files in the experiment folder will be overwritten.")
    print("Do NOT use the original legacy depot as the experiment folder.")

    confirm = input("\nContinue? (y/n): ").strip().lower()

    if confirm != "y":
        print("\nCancelled.")
        raise SystemExit

    apply_group(
        current_folder,
        experiment_folder,
        group_name
    )

    print(
        f"\nDone! Current '{group_name}' files have been "
        "applied to the experiment folder."
    )