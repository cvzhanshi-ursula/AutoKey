import pyautogui
import time
import random

count = 0
press_duration = 0.5  # 按键保持时间（秒），可以根据需要调整

while True:
    # 等待 10 秒
    time.sleep(10)
    
    # 按键盘 a
    pyautogui.keyDown('a')
    time.sleep(press_duration)
    pyautogui.keyUp('a')
    count += 1
    print(f"第 {count} 次操作：按下 'a' 键，保持 {press_duration} 秒")

    # 等待 10 秒
    time.sleep(10)
    
    # 按键盘 d
    pyautogui.keyDown('d')
    time.sleep(press_duration)
    pyautogui.keyUp('d')
    count += 1
    print(f"第 {count} 次操作：按下 'd' 键，保持 {press_duration} 秒")
