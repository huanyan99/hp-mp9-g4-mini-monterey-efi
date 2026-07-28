# HP MP9 G4 Mini macOS Monterey 12.6.5 EFI

이 저장소는 HP ProDesk 600 G4 DM / HP MP9 G4 Mini 계열 EFI를 기반으로 조정한 HP MP9 G4 Mini용 최종 OpenCore EFI 패키지입니다.

## 하드웨어

| 항목 | 구성 |
| --- | --- |
| 장치 | HP MP9 G4 Mini / HP 600 G4 Mini 계열 |
| CPU | Intel Core i5-8400T |
| iGPU | Intel UHD Graphics 630 |
| Wi-Fi | BCM94360CS2 |
| 저장 장치 | 500GB SATA HDD |
| macOS | macOS Monterey 12.6.5 (21G531) |
| SMBIOS | Macmini8,1 |

## 최종 EFI

최종 소스 EFI:

```text
all_efi/custom/final/hp-mp9-g4-mini-i5-8400t-bcm94360cs2-monterey-12.6.5/
├── igpu/EFI
└── safe/EFI
```

최종 zip 패키지:

```text
dist/custom/final/
├── hp-mp9-g4-mini-monterey-12.6.5-igpu-final.zip
├── hp-mp9-g4-mini-monterey-12.6.5-safe-rescue.zip
└── SHA256SUMS.txt
```

## 버전 설명

`igpu-final`은 최종 일상 사용용 EFI입니다.

- UHD 630 그래픽 가속 활성화
- `-igfxvesa` 미사용
- 추가 HDMI / DVMT framebuffer 패치 미적용
- BCM94360CS2 Wi-Fi는 네이티브 상태로 유지하며 `brcmfx-country` / `brcmfx-aspm` 미사용
- HeiPG Monterey 12.6.5 설치 이미지에 맞춰 `SecureBootModel = Disabled`

`safe-rescue`는 복구용 EFI입니다.

- `-igfxvesa` 유지
- 블랙 스크린, 설치, 복구 상황에 사용
- 완전한 iGPU 가속 없음
- `SecureBootModel = Disabled` 동일 적용

## 사용 방법

1. 필요한 zip 패키지를 압축 해제합니다.
2. 안에 있는 `EFI` 폴더를 USB 또는 내장 디스크의 EFI 파티션 루트에 복사합니다.
3. 교체 후 첫 부팅 때 OpenCore에서 Space 키를 누르고 `Reset NVRAM`을 선택합니다.
4. 재부팅 후 `Macintosh HD`를 선택합니다.

## SMBIOS

공개 패키지는 SMBIOS 자리 표시자를 유지합니다.

```text
SystemSerialNumber = CHANGEME_SERIAL
MLB                = CHANGEME_MLB
SystemUUID         = 00000000-0000-0000-0000-000000000000
```

실사용 전에는 본인만의 `Macmini8,1` 시리얼 번호, MLB, UUID, ROM을 생성하는 것을 권장합니다.

## Wi-Fi 참고

BCM94360CS2는 Monterey에서 네이티브 호환 카드로 처리합니다. Wi-Fi 비밀번호가 맞는데 연결되지 않는 경우, 먼저 macOS에 저장된 네트워크와 키체인 비밀번호를 삭제한 뒤 다시 연결하세요. 이 빌드에서는 `brcmfx-country`를 기본으로 추가하지 않는 것을 권장합니다.

## Credits

HP ProDesk 600 G4 DM OpenCore EFI를 기반으로 정리했습니다. 기본 플랫폼 지원을 제공한 원작자에게 감사드립니다.
