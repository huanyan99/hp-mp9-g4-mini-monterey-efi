"""Build a minimal public Sequoia EFI from the verified USB configuration."""

import hashlib
import plistlib
import shutil
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("F:/EFI")
NAME = "hp-prodesk-600-g4-mini-sequoia-15.8.1"
DEST = ROOT / "all_efi" / "custom" / "final" / NAME / "EFI"
ARCHIVE = ROOT / "dist" / "custom" / "final" / f"{NAME}-public.zip"
EXPECTED_CONFIG_MD5 = "da196c84c31a9809c0ec3d87af9f27e9"
EXPECTED_OC_MD5 = "ca55381385ec7921387f31a63210a60f"


def digest(path, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def checked_path(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()) or not path.exists():
        raise ValueError(f"Missing or unsafe referenced path: {relative}")
    return path


config_path = SOURCE / "OC" / "config.plist"
oc_path = SOURCE / "OC" / "OpenCore.efi"
if digest(config_path, "md5") != EXPECTED_CONFIG_MD5:
    raise SystemExit("USB config differs from the verified working version")
if digest(oc_path, "md5") != EXPECTED_OC_MD5:
    raise SystemExit("USB OpenCore binary differs from the verified working version")
if DEST.exists() or ARCHIVE.exists():
    raise SystemExit("Output already exists; refusing to overwrite")

config = plistlib.loads(config_path.read_bytes())
generic = config["PlatformInfo"]["Generic"]
private_values = (
    generic["SystemSerialNumber"],
    generic["MLB"],
    generic["SystemUUID"],
    generic["ROM"],
)
if not all(private_values):
    raise SystemExit("Unexpected empty device identity")

for expected in ("AirportBrcmFixup.kext", "AirportBrcmFixup.kext/Contents/PlugIns/AirPortBrcmNIC_Injector.kext"):
    entries = [item for item in config["Kernel"]["Add"] if item["BundlePath"] == expected]
    if len(entries) != 1 or entries[0]["Enabled"]:
        raise SystemExit(f"Unexpected Wi-Fi configuration: {expected}")

generic.update(
    SystemSerialNumber="CHANGEME0000",
    MLB="CHANGEME_MLB_0001",
    SystemUUID="00000000-0000-0000-0000-000000000000",
    ROM=b"\x00" * 6,
)

DEST.mkdir(parents=True)
shutil.copytree(SOURCE / "BOOT", DEST / "BOOT", ignore=shutil.ignore_patterns("._*", ".DS_Store"))
target_oc = DEST / "OC"
target_oc.mkdir()
shutil.copy2(oc_path, target_oc / "OpenCore.efi")
shutil.copytree(SOURCE / "OC" / "Resources", target_oc / "Resources", ignore=shutil.ignore_patterns("._*", ".DS_Store"))

for category, entries, key in (
    ("ACPI", config["ACPI"]["Add"], "Path"),
    ("Drivers", config["UEFI"]["Drivers"], "Path"),
    ("Kexts", config["Kernel"]["Add"], "BundlePath"),
):
    target_dir = target_oc / category
    target_dir.mkdir()
    for entry in entries:
        if not entry["Enabled"]:
            continue
        relative = Path(entry[key])
        if category == "Kexts":
            relative = Path(relative.parts[0])
        source_path = checked_path(SOURCE / "OC" / category, relative)
        target_path = target_dir / relative
        if target_path.exists():
            continue
        if source_path.is_dir():
            shutil.copytree(source_path, target_path, ignore=shutil.ignore_patterns("._*", ".DS_Store"))
        else:
            shutil.copy2(source_path, target_path)

private_config_bytes = config_path.read_bytes()
public_config_bytes = plistlib.dumps(config, sort_keys=False)
for value in private_values:
    if isinstance(value, bytes):
        needle = value.hex().upper().encode("ascii")
        if needle in public_config_bytes.upper():
            raise SystemExit("Private ROM remains in public config")
    elif value.encode("utf-8") in public_config_bytes:
        raise SystemExit("Private identity remains in public config")
if private_config_bytes == public_config_bytes:
    raise SystemExit("Public config was not sanitized")
(target_oc / "config.plist").write_bytes(public_config_bytes)

public_config = plistlib.loads((target_oc / "config.plist").read_bytes())
for category, entries, key in (
    ("ACPI", public_config["ACPI"]["Add"], "Path"),
    ("Drivers", public_config["UEFI"]["Drivers"], "Path"),
    ("Kexts", public_config["Kernel"]["Add"], "BundlePath"),
):
    for entry in entries:
        if entry["Enabled"]:
            checked_path(target_oc / category, entry[key])

ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(DEST.rglob("*")):
        if path.is_file():
            archive.write(path, path.relative_to(DEST.parent).as_posix())

print(f"EFI: {DEST}")
print(f"ZIP: {ARCHIVE} ({ARCHIVE.stat().st_size} bytes)")
print(f"SHA256: {digest(ARCHIVE)}")
