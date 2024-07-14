import pyautogui
import pyscreeze
import time

# imageOffSet = 25

# def checkImage():
#     try:
#         pos = pg.locateOnScreen("./urtiga.png", confidente=0.8)
#         pg.moveTo(pos[0]+imageOffSet, pos[1]+imageOffSet)
#         pg.click()
#         time.sleep(1)
#     except:
#         print("Imagem não encontrada no Dofus.")

# checkImage()

# pos = pyautogui.locateOnScreen('./urtiga.png')

img = pyscreeze.locateOnScreen('urtiga.png')

print(img)

