# HP ProDesk 600 G4 Mini OpenCore EFI

## macOS Sequoia 15.8.1 公开备份

`dist/custom/final/hp-prodesk-600-g4-mini-sequoia-15.8.1-public.zip` 是从当前可用的 U 盘 EFI 精简而来，适用于本机 HP ProDesk 600 G4 Mini、i5-8400T、UHD 630、BCM94360CS2、Realtek 有线网卡及 256GB SATA SSD。保留了正在使用的 ACPI、驱动、Kext、OpenCanopy 资源和原始启动二进制。U 盘原件未改动；内置盘 EFI 已完成文件校验，但尚未收到拔掉 U 盘独立启动的确认。

本版 `AirportBrcmFixup.kext` 和 `AirPortBrcmNIC_Injector.kext` 均为**禁用**，这是当前 Wi-Fi 正常工作的状态，请勿照旧教程重新启用。测试系统还安装了 OCLP 2.5.1 Modern Wireless 根补丁；此 zip **不包含**系统卷补丁，单靠 EFI 不保证全新安装的 Sequoia Wi-Fi 可用。

公开包已将 `PlatformInfo -> Generic` 中的序列号、MLB、UUID、ROM 改为占位值。个人恢复时请先备份目标 EFI，再从自己保存的私有工作配置恢复这些字段；不要把真实值提交到 GitHub。复制 `EFI` 文件夹到 EFI 分区根目录时，保留原有 `EFI/APPLE`。首次启动保留 U 盘作为回退，不要无故 Reset NVRAM。此包使用 U 盘原有 OpenCore 二进制，其具体构建来源尚未独立确认；`ocvalidate` 1.0.8 对工作配置检查为零错误，公开版仅更改了身份字段。

校验值见 `dist/custom/final/SHA256SUMS.txt`。可用仓库根目录的 `build-sequoia-public.py` 从指纹匹配的工作 U 盘重新生成去标识版本。下面是保留的 Monterey 12.6.5 旧版说明。

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
