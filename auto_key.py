import pyautogui
import time
import random

count = 0
press_duration = 0.5  # 按键保持时间（秒），可以根据需要调整

# ============================================================
# 旧版本（已停用）：交替按 a / d 键 —— 防挂机 / 防掉线
# 作用：每 10 秒交替按下 a、d 键，模拟游戏角色左右轻微移动，
#       骗过游戏的"长时间无操作"判定，避免被踢下线。
# 如需恢复，取消下面这段注释即可。
# ============================================================
# while True:
#     # 等待 10 秒
#     time.sleep(10)
#
#     # 按键盘 a
#     pyautogui.keyDown('a')
#     time.sleep(press_duration)
#     pyautogui.keyUp('a')
#     count += 1
#     print(f"第 {count} 次操作：按下 'a' 键，保持 {press_duration} 秒")
#
#     # 等待 10 秒
#     time.sleep(10)
#
#     # 按键盘 d
#     pyautogui.keyDown('d')
#     time.sleep(press_duration)
#     pyautogui.keyUp('d')
#     count += 1
#     print(f"第 {count} 次操作：按下 'd' 键，保持 {press_duration} 秒")
# ============================================================

# ============================================================
# 当前版本：每隔 1 秒按下 f 键，保持 0.5 秒
# 作用：高频、持续地触发 f 键，适用于需要反复拾取 / 互动等场景。
# ============================================================
while True:
    # 按键盘 f，保持 0.5 秒
    pyautogui.keyDown('f')
    time.sleep(press_duration)
    pyautogui.keyUp('f')
    count += 1
    print(f"第 {count} 次操作：按下 'f' 键，保持 {press_duration} 秒")

    # 等待 1 秒
    time.sleep(1)
