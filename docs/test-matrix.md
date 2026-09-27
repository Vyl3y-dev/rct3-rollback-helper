# RCT3 2026 Regression Test Matrix

Testing performed on the same Windows system using Steam copies of
RollerCoaster Tycoon 3: Complete Edition.

## Builds

### Legacy Build
- Release: 2020
- App ID: `1368820`
- Depot ID: `1368821`
- Manifest ID: `3464953341930095826`
- Reported executable version: `3.2.5.13`
- RCT3.exe SHA-256:
  `E2273B00242DFBC23E72F0A20A64A88528AFF01543534309F4D46B7D720695C1`

### Current Build
- Updated: March 2026
- App ID: `1368820`
- Depot ID: `1368821`
- Reported executable version: `3.2.5.13`
- RCT3.exe SHA-256:
  `1C9316E728D67AAA3BFE36D0A1634F3139582927440A5467C351E4C949B5B21D`

## Test Matrix

| Executable | Resources | Startup | Peep Designer | Peep Save | Notes |
|---|---|---|---|---|---|
| Legacy | Legacy | PASS | PASS | PASS | Known-working 2020 baseline |
| Legacy | Current | PASS | PASS | PASS | Current resources function with legacy executable |
| Current | Legacy | PASS* | PASS | FAIL | Blank popup appeared during earlier hybrid test; game continued after dismissing it |
| Current | Current | PASS | PASS | FAIL | Reproduces the original reported regression |

\* Earlier hybrid test produced a blank in-game popup during startup. This did not prevent entry into Peep Designer; saving the group still crashed.


## Test Procedure
launch → Tools → Peep Designer → create new disposable group → edit peeps → save


## Resource Group Tests

All tests below began with a pristine legacy depot copy using the legacy executable.

| Current Resource Group Applied | Startup | Peep Designer | Peep Save |
|---|---|---|---|
| Languages + SChinese additions | PASS | PASS | PASS |
| Resolution | PASS | PASS | PASS |
| Front/UI | PASS | PASS | PASS |
| Cache (`SCCache.bin`, `STCache.bin`) | PASS | PASS | PASS |
| Languages + Resolution | PASS | PASS | PASS |
| Languages + Resolution + Front/UI | PASS | PASS | PASS |
| All above groups combined | PASS | PASS | PASS |

## Contaminated Path Investigation

> **Excluded from regression evidence:** These tests were performed while a
> manually-created archive named `RollerCoaster Tycoon 3 Complete Edition.zip`
> existed beside the Steam installation. ProcMon later showed that RCT3
> attempted to read a ZIP matching the installation directory name during
> startup. Renaming/removing the archive eliminated the apparent path-dependent
> startup crash.

| Installation Path | Result |
|---|---|
| `...\common\RCT3-Experiment` | PASS |
| `...\Steam\RCT3-Experiment` | PASS |
| `...\steamapps\RCT3-Experiment` | PASS |
| `...\common\RCT3-Experiment` | PASS |
| `...\common\RollerCoaster Tycoon 3 Complete Edition TEST` | PASS |
| `...\common\RollerCoaster Tycoon 3 Complete Edition` | FAIL* |
| `...\common\RollerCoaster Tycoon 3 Complete Edition BROKEN` | PASS |

\* This failure was later determined to be contaminated by the presence of a
same-named sibling ZIP archive and is **not evidence of the March 2026 regression**.