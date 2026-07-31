import pyautogui
import time
import random

press_duration = 0.5  # 按键保持时间（秒），可以根据需要调整


# ============================================================
# 第一版（旧版本，已停用）：交替按 a / d 键 —— 防挂机 / 防掉线
# 作用：每 10 秒交替按下 a、d 键，模拟游戏角色左右轻微移动，
#       骗过游戏的"长时间无操作"判定，避免被踢下线。
# 如需单独运行该版本，在 __main__ 中调用 anti_afk_ad() 即可。
# ============================================================
def anti_afk_ad(duration_seconds=None):
    """
    交替按 a / d 键 —— 防挂机 / 防掉线。
    :param duration_seconds: 持续时长（秒）；传 None 则无限循环（第一版原始行为）。
    """
    deadline = time.time() + duration_seconds if duration_seconds else None
    count = 0
    while True:
        if deadline is not None and time.time() >= deadline:
            break

        # 等待 10 秒
        time.sleep(10)

        # 按键盘 a
        pyautogui.keyDown('a')
        time.sleep(press_duration)
        pyautogui.keyUp('a')
        count += 1
        print(f"第 {count} 次操作：按下 'a' 键，保持 {press_duration} 秒")

        if deadline is not None and time.time() >= deadline:
            break

        # 等待 10 秒
        time.sleep(10)

        # 按键盘 d
        pyautogui.keyDown('d')
        time.sleep(press_duration)
        pyautogui.keyUp('d')
        count += 1
        print(f"第 {count} 次操作：按下 'd' 键，保持 {press_duration} 秒")


# ============================================================
# 第二版（当前版本）：每隔 1 秒按下 f 键，保持 0.5 秒
# 作用：高频、持续地触发 f 键，适用于需要反复拾取 / 互动等场景。
# ============================================================
def spam_f():
    """每隔 1 秒按下 f 键，保持 0.5 秒，循环执行。"""
    count = 0
    while True:
        # 按键盘 f，保持 0.5 秒
        pyautogui.keyDown('f')
        time.sleep(press_duration)
        pyautogui.keyUp('f')
        count += 1
        print(f"第 {count} 次操作：按下 'f' 键，保持 {press_duration} 秒")

        # 等待 1 秒
        time.sleep(1)


# ============================================================
# 第三版：大循环
# 流程（一轮）：
#   1. 单击 f 键 5 次（每次保持 0.5s，每次间隔 3s）
#   2. 第一版防挂机（交替按 a / d）—— 循环 13 分钟
#   3. 按 esc
# 一轮结束后回到步骤 1，无限循环。
# ============================================================
def version3_loop():
    """第三版大循环：f 连按 → 防挂机 13 分钟 → esc，周而复始。"""
    round_count = 0
    while True:
        round_count += 1
        print(f"\n========== 第三版大循环 第 {round_count} 轮 ==========")

        # 阶段 1：单击 f 键 5 次，每次保持 0.5s，每次间隔 3s
        print("阶段一：单击 f 键 5 次（保持 0.5s，间隔 3s）")
        for i in range(5):
            pyautogui.keyDown('f')
            time.sleep(press_duration)
            pyautogui.keyUp('f')
            print(f"  第 {i + 1}/5 次：按下 'f' 键，保持 {press_duration} 秒")
            time.sleep(3)  # 每次间隔 3s

        # 阶段 2：第一版防挂机，循环 13 分钟
        print("阶段二：防挂机（交替按 a / d），持续 13 分钟")
        anti_afk_ad(13 * 60)

        # 阶段 3：按 esc
        print("阶段三：按下 esc 键")
        pyautogui.press('esc')


if __name__ == '__main__':
    # 切换版本：取消对应行的注释即可
    # anti_afk_ad()        # 第一版：a/d 防挂机（无限循环）
    # spam_f()             # 第二版：每 1 秒按 f
    version3_loop()        # 第三版：大循环（默认）
