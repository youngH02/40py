#pip install pyautogui
#pip install pyperclip 클립보드 사용
#pip install schedule 일정시간마다 함수를 동작

import pyautogui

picPosition = pyautogui.locateOnScreen(r'profile.png')
print(picPosition)

clickPosition =  pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)