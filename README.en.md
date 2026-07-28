# HP MP9 G4 Mini macOS Monterey 12.6.5 EFI

This is the final OpenCore EFI package for a personal HP MP9 G4 Mini build, adjusted from the HP ProDesk 600 G4 DM / HP MP9 G4 Mini platform EFI.

## Hardware

| Item | Configuration |
| --- | --- |
| Device | HP MP9 G4 Mini / HP 600 G4 Mini platform |
| CPU | Intel Core i5-8400T |
| iGPU | Intel UHD Graphics 630 |
| Wi-Fi | BCM94360CS2 |
| Storage | 500GB SATA HDD |
| macOS | macOS Monterey 12.6.5 (21G531) |
| SMBIOS | Macmini8,1 |

## Final EFI

Final source EFI:

```text
all_efi/custom/final/hp-mp9-g4-mini-i5-8400t-bcm94360cs2-monterey-12.6.5/
├── igpu/EFI
└── safe/EFI
```

Final zip packages:

```text
dist/custom/final/
├── hp-mp9-g4-mini-monterey-12.6.5-igpu-final.zip
├── hp-mp9-g4-mini-monterey-12.6.5-safe-rescue.zip
└── SHA256SUMS.txt
```

## Versions

`igpu-final` is the final daily optimized EFI:

- UHD 630 acceleration enabled
- No `-igfxvesa`
- No extra HDMI / DVMT framebuffer patches
- BCM94360CS2 Wi-Fi kept in native mode, without `brcmfx-country` / `brcmfx-aspm`
- `SecureBootModel = Disabled` for the HeiPG Monterey 12.6.5 installer

`safe-rescue` is the rescue EFI:

- Keeps `-igfxvesa`
- Intended for black screen, installation, or recovery
- No full iGPU acceleration
- Also uses `SecureBootModel = Disabled`

## Usage

1. Extract the zip package you need.
2. Copy the `EFI` folder to the root of the USB or internal disk EFI partition.
3. On first boot after replacement, enter OpenCore, press Space, and select `Reset NVRAM`.
4. Reboot and select `Macintosh HD`.

## SMBIOS

The public package keeps placeholder SMBIOS values:

```text
SystemSerialNumber = CHANGEME_SERIAL
MLB                = CHANGEME_MLB
SystemUUID         = 00000000-0000-0000-0000-000000000000
```

Generate your own `Macmini8,1` serial number, MLB, UUID, and ROM before daily use.

## Wi-Fi Notes

BCM94360CS2 is treated as a native Monterey-compatible card. If Wi-Fi rejects a correct password, first remove the saved macOS network profile and Keychain password, then reconnect. Adding `brcmfx-country` by default is not recommended for this build.

## Credits

Based on the HP ProDesk 600 G4 DM OpenCore EFI. Thanks to the original author for the base platform support.
