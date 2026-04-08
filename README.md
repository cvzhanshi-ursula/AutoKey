# AutoKey

模拟键盘按键的自动化脚本，支持通过 GitHub Actions 打包为 Windows EXE，无需本地 Windows 环境。

## 文件说明

- `auto_key.py` — 主脚本，循环按 `2` 键并模拟人类操作节奏
- `.github/workflows/build.yml` — GitHub Actions 自动打包配置

## 打包方法（不需要 Windows）

1. 把这个目录推送到你的 GitHub 仓库
2. GitHub Actions 会自动在 Windows 环境打包
3. 进入仓库 → Actions → 最新构建 → Artifacts → 下载 `auto_key_windows.zip`
4. 解压后得到 `auto_key.exe`，双击运行即可

也可以在 Actions 页面点 **Run workflow** 手动触发打包。

## 本地运行（macOS/Linux）

```bash
pip install pyautogui
python auto_key.py
```

> macOS 需在系统偏好设置 → 安全与隐私 → 辅助功能 中给终端授权。
