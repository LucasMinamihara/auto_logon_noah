from time import sleep
import webbrowser
import pyautogui


print("running script python")
webbrowser.open("https://neoh.intelectah.com.br")
sleep(10)

pyautogui.hotkey("alt", "f4")