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
| Legacy | Legacy | PASS | PASS | PASS | Known-working baseline |
| Current | Current | FAIL* | — | — | Fresh Steam installation crashes during startup |
| Current | Legacy | PASS* | PASS | FAIL | Blank popup appeared during startup; game continued after dismissing it |
| Legacy | Current | PASS | PASS | PASS | Current resources function with legacy executable |

\* Before reinstalling the current build, the game launched and gameplay
functioned, but saving a Peep group caused a crash. After reinstalling the
current build, startup itself began consistently crashing.


## Test Procedure
launch → Tools → Peep Designer → create new disposable group → edit peeps → save