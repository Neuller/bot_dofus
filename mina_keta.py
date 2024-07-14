import pyautogui
import eventos
import time

i = 0

# [-2,4] - Mina Keta

def sala01():
    loop = 0
    while loop < 1:
        print('Verificando Material p/ Coleta - ' + str(loop))
        eventos.coletarRapido(518 , 326)
        eventos.coletarRapido(553 , 312)
        eventos.coletarRapido(692 , 202)
        eventos.coletarRapido(731 , 206)
        eventos.coletarRapido(955 , 238)
        eventos.coletarRapido(990 , 256)
        eventos.coletarRapido(1017 , 279)
        eventos.coletarRapido(1087 , 313)
        eventos.coletarRapido(1127 , 330)
        eventos.coletarRapido(1191 , 361)
        time.sleep(5)
        loop += 1
    
def sala02():
    loop = 0
    while loop < 1:
        print('Verificando Material p/ Coleta - ' + str(loop))
        eventos.coletarRapido(440 , 229)
        eventos.coletarRapido(475 , 206)
        eventos.coletarRapido(654 , 122)
        eventos.coletarRapido(692 , 102)
        eventos.coletarRapido(658 , 582)
        eventos.coletarRapido(620 , 604)
        time.sleep(5)
        loop += 1
        
def sala03():
    loop = 0
    while loop < 1:
        print('Verificando Material p/ Coleta - ' + str(loop))
        eventos.coletarRapido(546 , 460)
        eventos.coletarRapido(656 , 299)
        eventos.coletarRapido(695 , 276)
        time.sleep(5)
        loop += 1
        
def sala04():
    loop = 0
    while loop < 1:
        print('Verificando Material p/ Coleta - ' + str(loop))
        eventos.coletarRapido(1012 , 403)
        eventos.coletarRapido(1053 , 389)
        time.sleep(5)
        loop += 1
        
def sala05():
    loop = 0
    while loop < 1:
        print('Verificando Material p/ Coleta - ' + str(loop))
        eventos.coletarRapido(870 , 336)
        eventos.coletarRapido(694 , 335)
        eventos.coletarRapido(654 , 315)
        eventos.coletarRapido(622 , 298)
        time.sleep(5)
        loop += 1
        
def sala06():
    loop = 0
    while loop < 1:
        print('Verificando Material p/ Coleta - ' + str(loop))
        eventos.coletarRapido(1157 , 320)
        eventos.coletarRapido(1124 , 306)
        time.sleep(5)
        loop += 1

while i < 25:
    print('==== Iniciando Ciclo ====')
    
    sala01()
        
    print('Troca de Mapa - Sala 2')
    pyautogui.click(1175 , 500)
    time.sleep(7)
    
    sala02()
    
    print('Troca de Mapa - Sala 3')
    pyautogui.click(1030 , 180)
    time.sleep(7)
    
    sala03()
        
    print('Troca de Mapa - Sala 4')
    pyautogui.click(1104 , 324)
    time.sleep(7)
    
    sala04()
        
    print('Troca de Mapa - Sala 3')
    pyautogui.click(421 , 448)
    time.sleep(7)
    
    sala03()
        
    print('Troca de Mapa - Sala 2')
    pyautogui.click(529 , 612)
    time.sleep(7)
    
    sala02()
    
    print('Troca de Mapa - Sala 5')
    pyautogui.click(670 , 720)
    time.sleep(7)
    
    sala05()
        
    print('Troca de Mapa - Sala 6')
    pyautogui.click(460 , 362)
    time.sleep(7)
    
    sala06()
    
    print('Troca de Mapa - Sala 5')
    pyautogui.click(1177 , 464)
    time.sleep(7)
    
    sala05()
    
    print('Troca de Mapa - Sala 2')
    pyautogui.click(1107 , 393)
    time.sleep(7)
    
    sala02()
    
    print('Troca de Mapa - Sala 1')
    pyautogui.click(569 , 233)
    time.sleep(7)
    
    i += 1
    print('==== Finalizando Ciclo ' + str(i) + ' ==== \n')
    
        