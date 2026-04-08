import pyautogui
import time
import random

count = 0

while True:
    # 按键盘 2
    time.sleep(random.uniform(0.1, 0.2))
    pyautogui.keyDown('2')
    time.sleep(random.uniform(0.05, 0.12))
    pyautogui.keyUp('2')

    count += 1
    print(f"已按第 {count} 次")

    # 每按5次动一下鼠标
    if count % 5 == 0:
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        pyautogui.moveRel(dx, dy, duration=0.1)
        time.sleep(random.uniform(0.05, 0.15))
        print("动了一下鼠标")

    # 核心间隔 5~10 秒
    time.sleep(random.uniform(5, 10))

    # 每15次多休息一会
    if count % 15 == 0:
        print("休息一会儿...")
        time.sleep(random.uniform(8, 15))

    # 每40次休息更久
    if count % 40 == 0:
        print("长时间休息")
        time.sleep(random.uniform(20, 40))
