# AutoKey

模拟键盘按键的自动化脚本，支持通过 GitHub Actions 打包为 Windows EXE，无需本地 Windows 环境。

## 文件说明

- `auto_key.py` — 主脚本，三个版本均封装为函数
- `.github/workflows/build.yml` — GitHub Actions 自动打包配置

## 三个版本

三个版本各自封装成一个函数，在 `auto_key.py` 末尾的 `if __name__ == '__main__':` 中切换要运行的版本。

### 第一版：`anti_afk_ad()` —— a / d 防挂机（旧版本）

每 10 秒交替按下 `a`、`d` 键，模拟游戏角色左右轻微移动，骗过游戏的"长时间无操作"判定，避免被踢下线。
不传参数时为无限循环；也可传入时长（秒）限定运行时间。

### 第二版：`spam_f()` —— 高频按 f

每隔 **1 秒**按下 `f` 键，保持 **0.5 秒**后松开，无限循环。
适用于需要持续、高频触发某个按键的场景（如反复拾取 / 互动）。

### 第三版：`version3_loop()` —— 大循环（当前默认）

一轮流程：

1. 单击 `f` 键 **5 次**（每次保持 0.5s，每次间隔 3s）
2. 第一版防挂机（交替按 `a` / `d`）—— 循环 **13 分钟**
3. 按下 `esc`

一轮结束后回到步骤 1，无限循环。

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

> macOS 需在系统偏好设置 → 安全性与隐私 → 辅助功能 中给终端授权。
