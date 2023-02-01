# pysupport

A Python cross-platform log gathering tool.

## Building

This app is built using [`pyinstaller`](pyinstaller.org). Note that apps must be built on the OS and hardware the app is intended to run on. This means apps built on Mac M1 systems will not work on Intel Macs. The future plan is to have GitHub actions build binaries for every applicable OS on appropriate runners during release.

### macOS

Build with `pyinstaller support/__main__.py --onefile --name pysupport`

### Windows

TBD

### Linux

TBD
