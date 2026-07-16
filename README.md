# AutoKey

模拟键盘按键的自动化脚本，支持通过 GitHub Actions 打包为 Windows EXE，无需本地 Windows 环境。

## 文件说明

- `auto_key.py` — 主脚本，循环模拟键盘按键
- `.github/workflows/build.yml` — GitHub Actions 自动打包配置

## 当前功能

每隔 **1 秒**按下 `f` 键，保持 **0.5 秒**后松开，循环执行。
适用于需要持续、高频触发某个按键的场景（如反复拾取 / 互动）。

## 历史版本（已在代码中注释停用）

旧版本交替按下 `a` / `d` 键，每 10 秒按一次，用于模拟游戏角色左右移动以"防挂机 / 防掉线"。
相关代码保留在 `auto_key.py` 中并已整体注释，需要时可取消注释恢复：

```python
# 旧版本：交替按 a / d 键 —— 防挂机 / 防掉线
# while True:
#     time.sleep(10)
#     pyautogui.keyDown('a')
#     time.sleep(press_duration)
#     pyautogui.keyUp('a')
#     ...
#     time.sleep(10)
#     pyautogui.keyDown('d')
#     time.sleep(press_duration)
#     pyautogui.keyUp('d')
```

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
