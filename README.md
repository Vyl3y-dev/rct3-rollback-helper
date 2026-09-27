# RCT3 Compatibility Helper

**Repository:** `rct3-rollback-helper`

An unofficial compatibility and recovery utility for **RollerCoaster
Tycoon 3: Complete Edition on Steam**.

This project was created while investigating crashes observed after the
March 2026 update, including a reproducible crash when saving families
in Peep Designer.

## What It Does

RCT3 Compatibility Helper detects known RCT3 executable builds and
provides a reversible compatibility rollback for the affected March 2026
build.

The current recovery workflow can:

-   Locate Steam through the Windows Registry
-   Detect configured Steam library locations
-   Locate RollerCoaster Tycoon 3: Complete Edition
-   Identify known builds using the SHA-256 hash of `RCT3.exe`
-   Retrieve the known-working legacy executable through the user's own
    Steam account
-   Verify the retrieved executable before using it
-   Back up and verify the currently installed executable
-   Install and verify the known-working legacy executable
-   Restore the backed-up current executable when explicitly requested
-   Refuse to modify unknown executable builds

The project does **not** redistribute RollerCoaster Tycoon 3 game files.

## Current Status

🚧 **Pre-release / v0.1 in development**

The diagnostic, acquisition, rollback, verification, backup, and restore
workflows have been implemented and tested. A user-friendly graphical
interface is currently being developed before the first public release.

The recovery workflow has successfully restored Peep Designer saving on
a reproduced affected installation.

## Known Builds

  --------------------------------------------------------------------------------------------------------------------
  Build                   SHA-256                                                              Status
  ----------------------- -------------------------------------------------------------------- -----------------------
  Legacy 2020             `e2273b00242dfbc23e72f0a20a64a88528aff01543534309f4d46b7d720695c1`   Known working in
                                                                                               current testing

  Post-March 2026 update  `1c9316e728d67aaa3bfe36d0a1634f3139582927440a5467c351e4c949b5b21d`   Known affected in
                                                                                               current testing
  --------------------------------------------------------------------------------------------------------------------

Both executables report version `3.2.5.13`, so the executable hash is
used to distinguish them.

## Safety and Recovery Design

RCT3 Compatibility Helper is intentionally conservative about modifying
a game installation.

Before a rollback is installed:

1.  The installed executable must match the known affected build.
2.  The legacy executable is retrieved through the user's own Steam
    account.
3.  The downloaded executable must match the known legacy SHA-256 hash.
4.  The current executable is backed up.
5.  The backup is verified before the installed executable is replaced.
6.  The installed replacement is verified after copying.

If a required verification fails, the recovery workflow stops rather
than continuing with an unverified file.

The original executable can be restored only from a backup that matches
the known current-build hash. Restore is an explicit user action;
detecting the legacy executable does not automatically restore the
affected build.

Unknown executable builds are treated as unsupported and are not
modified.

## Steam and Game Files

This project does not bundle or redistribute `RCT3.exe` or other
copyrighted RollerCoaster Tycoon 3 game files.

Compatible game files are obtained from Steam using the user's own
account and access to the game. Steam authentication is handled by the
Steam-compatible retrieval tooling rather than by RCT3 Compatibility
Helper storing the user's Steam password.

Steam updates or **Verify integrity of game files** may replace the
compatibility executable with the current Steam version.

## Research

The technical investigation, reproduction tests, resource-isolation
experiments, and excluded/contaminated tests are documented separately:

-   [`docs/findings.md`](docs/findings.md)
-   [`docs/test-matrix.md`](docs/test-matrix.md)

The research documentation is intended to preserve both successful
findings and investigative dead ends rather than presenting the recovery
method as a reverse-engineered patch. The exact code-level cause of the
Peep Designer regression has not yet been identified.

## v0.1 Progress

-   [x] Detect Steam installation
-   [x] Detect Steam libraries
-   [x] Locate RCT3
-   [x] Hash `RCT3.exe`
-   [x] Identify known legacy and affected builds
-   [x] Retrieve the legacy executable through Steam
-   [x] Limit retrieval to the required executable
-   [x] Verify the retrieved legacy executable
-   [x] Back up and verify the current executable
-   [x] Install and verify the compatibility rollback
-   [x] Restore and verify the original executable
-   [ ] Graphical user interface
-   [ ] Package standalone Windows release
-   [ ] Clean-install end-to-end release test
-   [ ] Publish v0.1

## Disclaimer

This is an unofficial community project and is not affiliated with or
endorsed by Atari, Frontier Developments, Valve, or the developers of
any third-party retrieval tooling used by the project.

Use of this project requires a legitimate Steam installation and access
to RollerCoaster Tycoon 3: Complete Edition.
