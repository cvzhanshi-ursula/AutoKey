import pyautogui
import time
import random

count = 0

while True:
    # 等待 10 秒
    time.sleep(10)
    
    # 按键盘 a
    pyautogui.press('a')
    count += 1
    print(f"第 {count} 次操作：按下 'a' 键")

    # 等待 10 秒
    time.sleep(10)
    
    # 按键盘 d
    pyautogui.press('d')
    count += 1
    print(f"第 {count} 次操作：按下 'd' 键")
