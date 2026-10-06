# RCT3 Compatibility Helper

**Repository:** `rct3-rollback-helper`

An unofficial Windows compatibility and recovery utility for **RollerCoaster Tycoon 3: Complete Edition on Steam**.

This project was created while investigating crashes observed after the March 2026 update, including a reproducible crash when saving families in Peep Designer.

## What It Does

RCT3 Compatibility Helper detects known RCT3 executable builds and provides a reversible compatibility rollback for the affected March 2026 build.

The current recovery workflow can:

- Locate Steam through the Windows Registry
- Detect configured Steam library locations
- Locate RollerCoaster Tycoon 3: Complete Edition
- Identify known builds using the SHA-256 hash of `RCT3.exe`
- Retrieve the known-working legacy executable through the user's own Steam account
- Verify the retrieved executable before using it
- Back up and verify the currently installed executable
- Install and verify the known-working legacy executable
- Restore the backed-up current executable when explicitly requested
- Refuse to modify unknown executable builds

The project does **not** redistribute RollerCoaster Tycoon 3 game files.

## Current Status

🚧 **Release candidate for v0.1**

The diagnostic, acquisition, rollback, verification, backup, restore, and graphical interface workflows have been implemented and tested.

The recovery workflow has successfully restored Peep Designer saving on a reproduced affected installation. Packaging and a final clean-install end-to-end release test remain before the first public release.

## Known Builds

| Build | SHA-256 | Status |
| --- | --- | --- |
| Legacy 2020 | `e2273b00242dfbc23e72f0a20a64a88528aff01543534309f4d46b7d720695c1` | Known working in current testing |
| Post-March 2026 update | `1c9316e728d67aaa3bfe36d0a1634f3139582927440a5467c351e4c949b5b21d` | Known affected in current testing |

Both executables report version `3.2.5.13`, so the executable hash is used to distinguish them.

## Safety and Recovery Design

RCT3 Compatibility Helper is intentionally conservative about modifying a game installation.

Before a rollback is installed:

1. The installed executable must match the known affected build.
2. DepotDownloader is obtained from a pinned release and its downloaded archive is verified against the expected SHA-256 hash before extraction.
3. The legacy executable is retrieved through the user's own Steam account.
4. The downloaded legacy executable must match the known legacy SHA-256 hash.
5. The current executable is backed up.
6. The backup is verified before the installed executable is replaced.
7. The installed replacement is verified after copying.

If a required verification fails, the recovery workflow stops rather than continuing with an unverified file.

The original executable can be restored only from a backup that matches the known current-build hash. Restore is an explicit user action; detecting the legacy executable does not automatically restore the affected build.

Unknown executable builds are treated as unsupported and are not modified.

## Steam Authentication and DepotDownloader

RCT3 Compatibility Helper uses **DepotDownloader**, an independent SteamRE project, to retrieve the historical executable from Steam. DepotDownloader runs separately from RCT3 Compatibility Helper.

When authentication is required, a Command Prompt window opens and displays a Steam QR code. Scan the QR code with the Steam mobile app to continue.

RCT3 Compatibility Helper does not receive or store the user's Steam username, password, or Steam Guard credentials.

The helper pins the DepotDownloader version it uses and verifies the downloaded DepotDownloader archive before extracting it. Runtime dependency and download files are stored under the user's local application-data directory rather than inside the game installation.

DepotDownloader project:
https://github.com/SteamRE/DepotDownloader

## Steam and Game Files

This project does not bundle or redistribute `RCT3.exe` or other copyrighted RollerCoaster Tycoon 3 game files.

Compatible game files are obtained from Steam using the user's own account and access to the game.

Steam updates or **Verify integrity of game files** may replace the compatibility executable with the current Steam version.

## Research

The technical investigation, reproduction tests, resource-isolation experiments, and excluded/contaminated tests are documented separately:

- [`docs/findings.md`](docs/findings.md)
- [`docs/test-matrix.md`](docs/test-matrix.md)

The research documentation is intended to preserve both successful findings and investigative dead ends rather than presenting the recovery method as a reverse-engineered patch. The exact code-level cause of the Peep Designer regression has not yet been identified.

## v0.1 Progress

- [x] Detect Steam installation
- [x] Detect Steam libraries
- [x] Locate RCT3
- [x] Hash `RCT3.exe`
- [x] Identify known legacy and affected builds
- [x] Retrieve the legacy executable through Steam
- [x] Limit retrieval to the required executable
- [x] Verify the retrieved legacy executable
- [x] Back up and verify the current executable
- [x] Install and verify the compatibility rollback
- [x] Restore and verify the original executable
- [x] Graphical user interface
- [x] Store runtime application data outside the repository/game directory
- [x] Pin and verify the DepotDownloader dependency archive
- [ ] Package standalone Windows release
- [ ] Clean-install end-to-end release test
- [ ] Publish v0.1

## Disclaimer

This is an unofficial community project and is not affiliated with or endorsed by Atari, Frontier Developments, Valve, Steam, SteamRE, or DepotDownloader.

Use of this project requires a legitimate Steam installation and access to RollerCoaster Tycoon 3: Complete Edition.


## Forks and Modified Versions

RCT3 Compatibility Helper is licensed under the GNU General Public License v3.0. You are welcome to study, modify, and redistribute the project in accordance with that license.

If you distribute a modified version, please clearly identify it as modified and preserve the project's copyright and licensing notices.

Modified or derivative versions are maintained by their respective authors. Changes made by third parties are not endorsed, supported, or warranted by the original project unless explicitly stated otherwise.

For your safety, users should obtain official RCT3 Compatibility Helper releases from this repository. The original project cannot verify the behavior or integrity of third-party builds.
