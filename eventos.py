import pyautogui
import time

def coletar(x, y):
    pyautogui.moveTo(x , y, 1)
    pyautogui.click()
    time.sleep(5)
    
def coletarRapido(x, y):
    pyautogui.moveTo(x , y)
    pyautogui.click()
    time.sleep(0.5)
    
def descerMapa():
    pyautogui.moveTo(747 , 750, 1)
    pyautogui.click()
    time.sleep(5)
    
def subirMapa():
    pyautogui.moveTo(741 , 29, 1)
    pyautogui.click()
    time.sleep(5)
    
def esquerdaMapa():
    pyautogui.moveTo(217 , 385, 1)
    pyautogui.click()
    time.sleep(5)
    
def direitaMapa():
    pyautogui.moveTo(1422 , 425, 1)
    pyautogui.click()
    time.sleep(5)