import pyautogui
import time

i = 0

while i < 1000:
    print('==== Iniciando Coleta ====')
    
    # Sala 1
    pyautogui.moveTo(1067 , 493, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1019 , 468, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(873 , 291, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(835 , 265, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(668 , 335, 1)
    pyautogui.click()
    time.sleep(5)
    
    # Ir para Sala 2
    pyautogui.moveTo(528 , 294, 1)
    pyautogui.click()
    time.sleep(5)
    
    # Sala 2
    pyautogui.moveTo(482 , 330, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(709 , 496, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(509 , 310, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(582 , 276, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(836 , 225, 1)
    pyautogui.click()
    time.sleep(5)
    
    # Voltar
    pyautogui.moveTo(1086 , 571, 1)
    pyautogui.click()
    time.sleep(5)
    
    # Ir para Sala 3
    pyautogui.moveTo(942 , 291, 1)
    pyautogui.click()
    time.sleep(5)
    
    # Sala 3
    pyautogui.moveTo(727 , 189, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(936 , 240, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1017 , 170, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1054 , 188, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1089 , 278, 1)
    pyautogui.click()
    time.sleep(5)
    
    # Voltar
    pyautogui.moveTo(488 , 556, 1)
    pyautogui.click()
    time.sleep(5)
    
    i += 1
    print('==== Finalizando Ciclo ' + str(i) + ' ==== \n')
    

# Sala1
# 1067 , 493
# 1019 , 468
# 873 , 291
# 835 , 265
# 668 , 335

# Ir Sala2
# 522 , 351

# Sala2
# 482 , 330
# 709 , 496
# 509 , 310
# 582 , 276
# 836 , 225

# Voltar
# 1086 , 571

# Ir Sala3
# 950 , 373

# Sala3
# 727 , 189
# 936 , 240
# 1017 , 170
# 1054 , 188
# 1089 , 278

# Voltar
# 488 , 556
