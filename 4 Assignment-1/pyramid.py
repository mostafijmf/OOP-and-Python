import pyautogui
from time import *

n = int(input())

for i in range(n):
    j = i+1
    pyautogui.write('#' * j)
    pyautogui.write('\n')
