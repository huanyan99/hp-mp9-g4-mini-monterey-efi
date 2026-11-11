# HP ProDesk 600 G4 Mini OpenCore EFI

OpenCore EFI packages for the HP ProDesk 600 G4 Mini / HP MP9 G4 Mini platform.

## Languages

- [中文说明](README.zh-CN.md)
- [English](README.en.md)
- [한국어](README.ko.md)

## Release

Packages:

```text
dist/custom/final/
├── hp-mp9-g4-mini-monterey-12.6.5-igpu-final.zip
├── hp-mp9-g4-mini-monterey-12.6.5-safe-rescue.zip
├── hp-prodesk-600-g4-mini-sequoia-15.8.1-public.zip
└── SHA256SUMS.txt
```

The Sequoia package is a sanitized copy of the working USB EFI. Restore your own SMBIOS identity before personal use. The internal-disk boot path has not yet been independently confirmed without the USB. See the language-specific guides for details.

The Monterey `igpu-final` and `safe-rescue` packages remain available unchanged.
