import pyautogui as pg
import time

try:
    time.sleep(2)
    x , y = pg.position()

    print(x, ",", y)
except:
    print("Erro na execução.")