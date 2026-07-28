# HP MP9 G4 Mini macOS Monterey 12.6.5 EFI

这是给个人设备整理的最终 OpenCore EFI，基于 HP ProDesk 600 G4 DM / HP MP9 G4 Mini 同平台 EFI 调整而来。

## 设备配置

| 项目 | 配置 |
| --- | --- |
| 设备 | HP MP9 G4 Mini / HP 600 G4 Mini 同平台 |
| CPU | Intel Core i5-8400T |
| 核显 | Intel UHD Graphics 630 |
| Wi-Fi | BCM94360CS2 |
| 硬盘 | 500GB SATA HDD |
| 系统 | macOS Monterey 12.6.5 (21G531) |
| SMBIOS | Macmini8,1 |

## 最终 EFI

最终源码目录：

```text
all_efi/custom/final/hp-mp9-g4-mini-i5-8400t-bcm94360cs2-monterey-12.6.5/
├── igpu/EFI
└── safe/EFI
```

最终压缩包：

```text
dist/custom/final/
├── hp-mp9-g4-mini-monterey-12.6.5-igpu-final.zip
├── hp-mp9-g4-mini-monterey-12.6.5-safe-rescue.zip
└── SHA256SUMS.txt
```

## 版本说明

`igpu-final` 是最终日用优化版：

- 开启 UHD 630 核显加速
- 不使用 `-igfxvesa`
- 不加入额外 HDMI / DVMT framebuffer 补丁
- Wi-Fi 回滚为 BCM94360CS2 原生状态，不加入 `brcmfx-country` / `brcmfx-aspm`
- `SecureBootModel = Disabled`，适配 HeiPG Monterey 12.6.5 安装包

`safe-rescue` 是安全救援版：

- 保留 `-igfxvesa`
- 用于黑屏、安装、救援
- 没有完整核显加速
- 同样关闭 `SecureBootModel`

## 使用方法

1. 解压需要使用的 zip。
2. 将里面的 `EFI` 文件夹复制到 U 盘或硬盘 EFI 分区根目录。
3. 首次替换后进入 OpenCore，按空格选择 `Reset NVRAM`。
4. 重启后选择 `Macintosh HD` 启动。

## SMBIOS

公开版保留占位信息：

```text
SystemSerialNumber = CHANGEME_SERIAL
MLB                = CHANGEME_MLB
SystemUUID         = 00000000-0000-0000-0000-000000000000
```

实际使用前建议生成自己的 `Macmini8,1` 序列号、MLB、UUID 和 ROM。

## Wi-Fi 说明

BCM94360CS2 在 Monterey 下按原生免驱处理。若出现 Wi-Fi 密码正确但连不上，优先删除 macOS 已保存网络和钥匙串密码后重新连接，不建议默认添加 `brcmfx-country`。

## 致谢

基于 HP ProDesk 600 G4 DM OpenCore EFI 整理，感谢原作者的基础适配。
