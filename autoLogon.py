from time import sleep
import subprocess
import webbrowser
import pyautogui
import os

print("running script python")
webbrowser.open("https://neoh.intelectah.com.br")
sleep(10)

pyautogui.click(800, 479)
print("X: 812, Y: 484")

sleep(5)

pyautogui.click(211, 374)
sleep(10)

pyautogui.hotkey("f11")
sleep(7200)
subprocess.run([r"C:\Users\%username%\Downloads\echo.bat"])


