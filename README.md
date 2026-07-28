# HP MP9 G4 Mini macOS Monterey 12.6.5 EFI

这是给个人设备整理的 OpenCore EFI，基于 HP ProDesk 600 G4 DM / HP MP9 G4 Mini 同平台 EFI 调整而来。

## 设备配置

| 项目 | 配置 |
| --- | --- |
| 设备 | HP MP9 G4 Mini |
| CPU | Intel Core i5-8400T |
| 核显 | Intel UHD Graphics 630 |
| Wi-Fi | BCM94360CS2 |
| 硬盘 | 500GB SATA HDD |
| 系统 | macOS Monterey 12.6.5 (21G531) |
| SMBIOS | Macmini8,1 |

## 下载

最终压缩包在：

```text
dist/custom/final/
├── hp-mp9-g4-mini-monterey-12.6.5-igpu-final.zip
├── hp-mp9-g4-mini-monterey-12.6.5-safe-rescue.zip
└── SHA256SUMS.txt
```

`igpu-final` 是日用版，开启 UHD 630 核显加速。

`safe-rescue` 是救援版，保留 `-igfxvesa`，用于黑屏、安装或救援。

## 源 EFI

解压前也可以直接查看 EFI 目录：

```text
all_efi/custom/final/hp-mp9-g4-mini-i5-8400t-bcm94360cs2-monterey-12.6.5/
├── igpu/EFI
└── safe/EFI
```

## 当前最终配置

- `SecureBootModel = Disabled`
- SMBIOS: `Macmini8,1`
- UHD 630 使用原作者基础注入，不额外添加 HDMI / DVMT framebuffer 补丁
- BCM94360CS2 按 Monterey 原生免驱处理
- Wi-Fi 不加入 `brcmfx-country` / `brcmfx-aspm`

## 使用

1. 解压需要使用的 zip。
2. 把里面的 `EFI` 文件夹复制到 U 盘或硬盘 EFI 分区根目录。
3. 首次替换后进入 OpenCore，按空格选择 `Reset NVRAM`。
4. 重启后选择 `Macintosh HD`。

## SMBIOS

公开版保留占位信息：

```text
SystemSerialNumber = CHANGEME_SERIAL
MLB                = CHANGEME_MLB
SystemUUID         = 00000000-0000-0000-0000-000000000000
```

实际使用前建议生成自己的 `Macmini8,1` 序列号、MLB、UUID 和 ROM。

## 致谢

基于 HP ProDesk 600 G4 DM OpenCore EFI 整理，感谢原作者的基础适配。
