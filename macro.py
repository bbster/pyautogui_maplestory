import os, time, subprocess
import pyautogui

# 1572, 106 # 목록
# 368, 117 # 퀘스트
# 1482, 897 # 진행
# 821, 568 # 머리위 전구
# 1446, 590 # 퀘스트 수락버튼
# 784, 883 # 퀘스트 보상받기
# 1412, 378 # SP 자동분배


def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)

def imgsct():
    pyautogui.screenshot('전구.png', region=(771, 532, 100, 70))

def start():
        pyautogui.click(x=156, y=364)
        time.sleep(2)
        pyautogui.click(x=811, y=563)
        time.sleep(2)
        pyautogui.click(x=833, y=459, clicks=15, interval=0.1)
        pyautogui.click(x=1398, y=594)

        quest_accept = pyautogui.locateOnScreen('퀘스트_수락.png')
        pyautogui.click(quest_accept)
        time.sleep(2)

        quest_progress = pyautogui.locateOnScreen('퀘스트_진행.png')
        pyautogui.click(quest_progress)
        time.sleep(2)

        quest_complete = pyautogui.locateOnScreen('퀘스트_완료.png')
        pyautogui.click(x=833, y=459, clicks=15, interval=0.1)
        pyautogui.click(quest_complete)
        time.sleep(2)

        quest_get_rewarded = pyautogui.locateOnScreen('퀘스트_보상받기.png')
        pyautogui.click(quest_get_rewarded)
        time.sleep(2)

        pyautogui.click(x=1398, y=595)
        time.sleep(90)


def buff():
    while True:
        time.sleep(3)
        pyautogui.press(keys='1', presses=2, interval=0.5)  # 버프 1번
        time.sleep(2)
        pyautogui.press(keys='2', presses=2, interval=0.5)  # 버프 2번
        time.sleep(2)
        pyautogui.press(keys='3', presses=2, interval=0.5)  # 버프 3번
        time.sleep(2)
        pyautogui.press(keys='4', presses=2, interval=0.5)  # 버프 4번
        time.sleep(2)
        pyautogui.press(keys='b', presses=2, interval=0.5)  # 버프 5번
        time.sleep(150)

# 미니 던전용
def mini_dungeon():
    while True:
        time.sleep(2)
        # 1층
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')
        time.sleep(0.5)
        pyautogui.press(keys='d')
        time.sleep(1)
        pyautogui.press(keys='space')
        time.sleep(0.1)
        pyautogui.keyDown('up')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(1)
        pyautogui.keyUp('up')
        time.sleep(1)

        # 2층
        pyautogui.press(keys='d')
        time.sleep(1)
        pyautogui.press(keys='space')
        time.sleep(0.1)
        pyautogui.keyDown('up')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(1)
        pyautogui.keyUp('up')
        time.sleep(1)

        # 3층
        pyautogui.press(keys='d')
        time.sleep(1)
        pyautogui.keyDown('down')
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(1)
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        pyautogui.keyUp('down')
        time.sleep(1)
        pyautogui.press(keys='d')
        time.sleep(1)

        # #방향 틀어서
        # # 1층
        # pyautogui.keyDown('right')
        # pyautogui.keyUp('right')
        # time.sleep(0.5)
        # pyautogui.press(keys='d')
        # time.sleep(1)
        # pyautogui.press(keys='space')
        # pyautogui.keyDown('up')
        # pyautogui.keyDown('space')
        # pyautogui.keyUp('space')
        # time.sleep(1)
        # pyautogui.keyUp('up')
        #
        # time.sleep(1)
        #
        # # 2층
        # pyautogui.press(keys='d')
        # time.sleep(1)
        # pyautogui.press(keys='space')
        # pyautogui.keyDown('up')
        # pyautogui.keyDown('space')
        # pyautogui.keyUp('space')
        # time.sleep(1)
        # pyautogui.keyUp('up')
        # time.sleep(1)
        #
        # # 3층
        # pyautogui.press(keys='d')
        # time.sleep(1)
        # pyautogui.keyDown('down')
        # pyautogui.keyDown('space')
        # pyautogui.keyUp('space')
        # time.sleep(1)
        # pyautogui.keyDown('space')
        # pyautogui.keyUp('space')
        # pyautogui.keyUp('down')
        # time.sleep(1)
        # pyautogui.press(keys='d')
        # time.sleep(1)


while True:
    buff()
    # start()
    # mini_dungeon
    # imgsct()
    # print_mouse_pos()
