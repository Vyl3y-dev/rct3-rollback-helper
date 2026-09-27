# RCT3 Complete Edition 2026 Regression Findings

## Issue
Before realizing it was ever updated in March or broken at all, like every random game I own on Steam, I got the sudden urge to play RCT3 with one specific goal in mind. To make a family of peeps with my husband and build a custom theme park for funzies. RCT3 suddenly stopped working. Ran fine but upon trying to save peeps it would crash. The gameplay worked as intended otherwise. This was first observed after the Mar. 2026 patch. Last time I played the game was before this patch, but I wanted to rule out things before jumping to conclusions. I also found many other people were unable to save peeps/experienced crashing and some even couldn't open the game itself. I later experienced this after everything I looked into surface level that could be causing the peeps to not save wasn't working and uninstalled/reinstalled the game only for it to not open and immediately crash, not even making it past the credit screens.

## Known Builds
Right now through my research of the current patch (2026) and the initial Complete edition release in 2020, Frontier/Atari considered both versions to be 3.2.5.13 despite clearly updating it 6 years after the initial steam build released. They are different builds. Producers claim the only change made was to add Chinese translations, implied GUI changes and such as necessary, even though its not mentioned in the patch notes. 

## Timeline
Last time played: Some time well before the Mar 2026 update --> game works as intended completely. Had a nice big park and everything. 
Recent attempt to play (before discovering there was an update 9/23/26-ish): game loads and plays but making peeps crashes the game entirely.
Reading/Following crashdumps, grafixlogs, and online advice here and there nothing would keep it from crashing on the peep designer. Game was still playable. 
Initial troubleshooting included uninstalling/reinstalling and repeatedly verifying the current Steam build. During later testing, a startup crash was observed in the official installation directory. This was ultimately traced to a same-named ZIP archive (`RollerCoaster Tycoon 3 Complete Edition.zip`) that had been manually created beside the installation while preparing files for external testing. RCT3 attempted to read this archive during startup. Renaming/removing the archive eliminated the startup crash.

This startup failure is therefore considered a testing artifact and is not currently considered part of the March 2026 regression.

## Crash Signature
Observed after reinstall on the current build:
- Faulting application: `RCT3.exe`
- Application version: `3.2.5.13`
- Faulting module: `RCT3.exe`
- Exception code: `0xc0000005`
- Exception offset: `0x00381bae`

## Current Findings
* Ruled out Steam hanging on to persistent data which might be causing issues.
## Current Findings

* The legacy 2020 build runs successfully on the same PC/OS/hardware configuration and saves Peep Designer groups correctly.
* The legacy and current executables both report version `3.2.5.13`, but their SHA-256 hashes differ, confirming that they are different binaries.
* The current build contains eight additional Simplified Chinese GUI resource files, consistent with the March 2026 language update.
* Additional existing resource files were also modified between the builds.
* Current resource groups were tested with the legacy executable individually and cumulatively. The game launched and Peep Designer saves succeeded.
* With the current 2026 executable restored to the otherwise-working current installation, the game launches and functions normally until saving a Peep Designer group, which reproducibly crashes the game.
* Replacing only the current executable with the verified legacy executable allows the same installation to launch and save Peep Designer groups successfully.

Current testing therefore strongly implicates a change in the post-March 2026 `RCT3.exe` in the reproducible Peep Designer save crash. The exact failing operation is still under investigation.

A byte-for-byte comparison was performed between a working reconstructed installation and the crashing Steam installation. Excluding generated/debugging files (`CrashDump.txt` and `RCT3CommunityFix_Backup\RCT3.exe`), the installations contained no differing, missing, or additional game files.

Further path testing produced a reproducible startup-crash condition tied to the exact official Steam installation path:

`C:\Program Files (x86)\Steam\steamapps\common\RollerCoaster Tycoon 3 Complete Edition`

A byte-identical copy located at:

`C:\Program Files (x86)\Steam\steamapps\common\RollerCoaster Tycoon 3 Complete Edition TEST`

launched successfully and allowed Peep groups to be saved.

The two directories were then renamed as a cross-test. The previously crashing installation was renamed to `RollerCoaster Tycoon 3 Complete Edition BROKEN` and immediately launched and saved Peeps successfully. The previously working installation was renamed to the exact official directory name, `RollerCoaster Tycoon 3 Complete Edition`, and immediately reproduced the startup crash.

This demonstrates that, in the current test environment, the startup crash follows the exact official installation pathname rather than the physical copy of the game or the contents of its game files. The mechanism responsible for this path-specific behavior has not yet been identified.

## Hash Comparisons
Current/2026 RCT3.exe SHA-256:
1C9316E728D67AAA3BFE36D0A1634F3139582927440A5467C351E4C949B5B21D

Legacy/2020 RCT3.exe SHA-256:
E2273B00242DFBC23E72F0A20A64A88528AFF01543534309F4D46B7D720695C1

## Legacy Manifest
App:      1368820\
Depot:    1368821\
Manifest: 3464953341930095826