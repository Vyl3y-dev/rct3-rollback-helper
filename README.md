# rct3-rollback-helper
# RCT3 Community Fix

A community-made diagnostic and recovery tool for RollerCoaster Tycoon 3:
Complete Edition on Steam.

This project was created while investigating crashes observed after the
March 2026 update, including a reproducible crash when saving families in
Peep Designer.

The goal is to provide Steam users with a safe way to identify affected
installations and, eventually, assist with recovery using files obtained
through the user's own Steam installation.

## Current Status

🚧 Work in progress.

The current diagnostic version can:

- Locate Steam using the Windows Registry
- Detect configured Steam library locations
- Locate RollerCoaster Tycoon 3: Complete Edition
- Calculate the SHA-256 hash of `RCT3.exe`
- Identify known legacy and affected executable builds
- Safely report unknown executable builds

The tool does not currently modify the game installation.

## Known Builds

| Build | SHA-256 | Status |
| --- | --- | --- |
| Legacy 2020 | `e2273b00242dfbc23e72f0a20a64a88528aff01543534309f4d46b7d720695c1` | Known working in current testing |
| Post-March 2026 update | `1c9316e728d67aaa3bfe36d0a1634f3139582927440a5467c351e4c949b5b21d` | Known affected in current testing |

Both executables report version `3.2.5.13`, so the executable hash is used
to distinguish them.

## Safety

RCT3 Community Fix does not redistribute RollerCoaster Tycoon 3 game files.

The project is intended to work with legitimate Steam installations and
files retrieved through the user's own Steam account.

Unknown executable builds are treated as unsupported and will not be
modified.

## Research

Technical findings and reproduction tests are documented in:

- [`docs/findings.md`](docs/findings.md)
- [`docs/test-matrix.md`](docs/test-matrix.md)

## Project Status

### v0.1 — Diagnostics

- [x] Detect Steam installation
- [x] Detect Steam libraries
- [x] Locate RCT3
- [x] Hash `RCT3.exe`
- [x] Identify known builds
- [x] Display diagnostic results

### Planned

- [ ] Legacy build retrieval assistance
- [ ] Installation backup and recovery safeguards
- [ ] Guided repair workflow
- [ ] Additional diagnostics for unknown builds

## Disclaimer

This is an unofficial community project and is not affiliated with or
endorsed by Atari, Frontier Developments, or Valve.
