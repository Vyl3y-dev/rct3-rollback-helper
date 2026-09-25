# RCT3 Complete Edition 2026 Regression Findings

## Issue
Before realizing it was ever updated in March or broken at all, like every random game I own on Steam, I got the sudden urge to play RCT3 with one specific goal in mind. To make a family of peeps with my husband and build a custom theme park for funzies. RCT3 suddenly stopped working. Ran fine but upon trying to save peeps it would crash. The gameplay worked as intended otherwise. This was first observed after the Mar. 2026 patch. Last time I played the game was before this patch, but I wanted to rule out things before jumping to conclusions. I also found many other people were unable to save peeps/experienced crashing and some even couldn't open the game itself. I later experienced this after everything I looked into surface level that could be causing the peeps to not save wasn't working and uninstalled/reinstalled the game only for it to not open and immediately crash, not even making it past the credit screens.

## Known Builds
Right now through my research of the current patch (2026) and the initial Complete edition release in 2020, Frontier/Atari considered both versions to be 3.2.5.13 despite clearly updating it 6 years after the initial steam build released. They are different builds. Producers claim the only change made was to add Chinese translations, implied GUI changes and such as necessary, even though its not mentioned in the patch notes. 

## Timeline
Last time played: Some time well before the Mar 2026 update --> game works as intended completely. Had a nice big park and everything. 
Recent attempt to play (before discovering there was an update 9/23/26-ish): game loads and plays but making peeps crashes the game entirely.
Reading/Following crashdumps, grafixlogs, and online advice here and there nothing would keep it from crashing on the peep designer. Game was still playable. 
All else failed --> "have you tried turning it off and back on again?" so uninstalled through steam and reinstalled + verified files (many times throughout this entire process) --> game no longer loads past opening credit screens/immediately crashes.

## Crash Signature
Observed after reinstall on the current build:
- Faulting application: `RCT3.exe`
- Application version: `3.2.5.13`
- Faulting module: `RCT3.exe`
- Exception code: `0xc0000005`
- Exception offset: `0x00381bae`

## Current Findings
* Ruled out Steam hanging on to persistent data which might be causing issues.
* A general system incompatibility became unlikely after the legacy build ran successfully on the same PC/OS/hardware configuration. 
* Crashdump mentions access violations which adds up with error reported in eventvwr but no obvious solutions actually worked.
* Found previous build through steamdb.info/depot and downloaded it via Steam console. It runs the game fine and saved peeps (as expected). 
* Compared hashes --> found difference in build despite being listed as the same version.
* Measured file count of both legacy and current builds --> current build had 8 more files (not including crashdump which gets created after runs) and all were language related which was expected/matches vague patch notes of the last update (i.e. current build).
* Files changed, however, was an extensive list of more than just language additions. Most are expected GUI changes due to language addition. Some are less expected edits to other language files but not super suspicious enough to be the culprit for the crashes. 
    * Created a copy of the legacy build for testing: legacy-prime.
        * replaced .exe file in legacy-prime with .exe from current build to test if files were causing the crashes in the game overall and/or peep designer. It did load the game with a blank ingame popup, upon clicking the ok to close the popup, went to test peep designer and it crashed (not unexpected).
        * replaced .exe file in legacy-prime (which was current build) with the legacy build .exe and the game ran fine, peeps worked as intended. 

Current testing strongly implicates changes to RCT3.exe in the reproduced Peep Designer crash. Further testing is ongoing to determine the exact cause and whether additional files contribute to other reported crashes.

## Hash Comparisons
Current/2026 RCT3.exe SHA-256:
1C9316E728D67AAA3BFE36D0A1634F3139582927440A5467C351E4C949B5B21D

Legacy/2020 RCT3.exe SHA-256:
E2273B00242DFBC23E72F0A20A64A88528AFF01543534309F4D46B7D720695C1

## Legacy Manifest
App:      1368820\
Depot:    1368821\
Manifest: 3464953341930095826