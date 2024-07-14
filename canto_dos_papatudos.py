import pyautogui
import time
import eventos

i = 0

while i < 1:
    print('==== Iniciando Ciclo ====')
    
    # Início [5,7]
    eventos.coletar(321 , 102) # Madeira de Freixo
    eventos.coletar(421 , 44) # Madeira de Freixo
    eventos.coletar(462 , 92) # Madeira de Freixo
    eventos.coletar(351 , 217) # Madeira de Freixo
    eventos.coletar(1100 , 95) # Madeira de Freixo
    eventos.coletar(1244 , 66) # Madeira de Freixo
    eventos.coletar(1206 , 76) # Madeira de Freixo
    eventos.coletar(1254 , 128) # Madeira de Freixo
    eventos.coletar(318 , 632) # Madeira de Freixo
    eventos.coletar(355 , 689) # Madeira de Freixo
    eventos.descerMapa()
    
    # [5,8]
    print('Coletando Madeira de Freixo')
    eventos.coletar(424 , 216) # Madeira de Freixo
    eventos.coletar(485 , 186) # Madeira de Freixo
    eventos.coletar(602 , 277) # Madeira de Freixo
    eventos.coletar(673 , 202) # Madeira de Freixo
    eventos.coletar(1072 , 439) # Madeira de Freixo
    eventos.coletar(602 , 595) # Madeira de Freixo
    eventos.coletar(534 , 565) # Madeira de Freixo
    eventos.direitaMapa()
    
    # [6,8]
    eventos.coletar(485 , 432) # Urtiga
    eventos.coletar(1136 , 481) # Urtiga
    eventos.direitaMapa()
    
    # [7,8]
    eventos.coletar(498 , 116) # Urtiga
    eventos.coletar(880 , 415) # Urtiga
    eventos.direitaMapa()
    
    # [8,8]
    eventos.coletar(479 , 576) # Urtiga
    eventos.coletar(966 , 97) # Madeira de Freixo
    eventos.direitaMapa()
    
    # [9,8]
    eventos.direitaMapa()
    
    # [10,8]
    eventos.coletar(604 , 314) # Madeira de Freixo
    eventos.coletar(545 , 398) # Trigo
    eventos.coletar(592 , 409) # Trigo
    eventos.coletar(604 , 393) # Trigo
    eventos.coletar(645 , 356) # Trigo
    eventos.coletar(559 , 453) # Trigo
    eventos.coletar(686 , 394) # Trigo
    eventos.coletar(601 , 462) # Trigo
    eventos.coletar(643 , 442) # Trigo
    eventos.coletar(716 , 444) # Trigo
    eventos.coletar(1028 , 278) # Trigo
    eventos.coletar(1055 , 312) # Trigo
    eventos.coletar(1102 , 307) # Trigo
    eventos.coletar(1067 , 243) # Trigo
    eventos.coletar(1174 , 282) # Trigo
    eventos.direitaMapa()
    
    # [11,8]
    eventos.coletar(556 , 89) # Urtiga
    eventos.coletar(960 , 564) # Madeira de Freixo
    eventos.subirMapa()
    
    # [11,7]
    eventos.coletar(414 , 123) # Urtiga
    eventos.esquerdaMapa()
    
    # [10,7]
    eventos.esquerdaMapa()
    
    # [9,7]
    eventos.esquerdaMapa()
    
    # [8,7]
    eventos.esquerdaMapa()
    
    # [7,7]
    eventos.esquerdaMapa()
    
    # [6,7]
    eventos.coletar(1177 , 469) # Urtiga
    eventos.coletar(1145 , 690) # Urtiga
    eventos.coletar(478 , 682) # Urtiga
    eventos.esquerdaMapa()
    
    i += 1
    
    print('==== Finalizando Ciclo ' + str(i) + ' ==== \n')
