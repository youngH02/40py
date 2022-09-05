#pip install pyautogui
#pip install pyperclip

import pyautogui
import time
import pyperclip

# while True :
#   print(pyautogui.position())
#   time.sleep(0.1)


pyautogui.moveTo(1241,206,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

https://stackoverflow.com/questions/46390290/error-when-trying-to-install-pyautogui

