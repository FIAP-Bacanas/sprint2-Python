# Codigo pertencente ao grupo com os membros
# David Denunci
# Eduardo Pielich
# Igor Nunes
# Victor Hugo Andrade
# João Rodrigo Nogueira


#Import das bibliotecas que serão utilizadas

import time as tm

# Definição de variaveis
sens1 = False
sens2 = False
num_travessias = 0
v2 = 2

sm_verm = False
sm_ama = False
sm_verd = True

sm1_verm = True
sm1_verd = False


#definição de funções 

def menu():
    print("="*30)
    print("")
    print("Bem vindo a simulação de travessia com o semaforo com sensor de proximidade")
    print("")
    print("Hoje atravessaram ",num_travessias ," pessoas")
    print("="*30)

def farol(flag):
    if flag == 1:
        print("="*30)

        print("Carros    Pedestres")
        print("  (0)        (X)")
        print("  (0)        (0)")
        print("  (X)  ")
        print("="*30)

    elif flag == 2:
        print("="*30)

        print("Carros    Pedestres")
        print("  (0)        (X)")
        print("  (X)        (0)")
        print("  (0)  ")
        print("="*30)

        #dois segundos para ficar parado no amarelo
        tm.sleep(2)
    elif flag == 3:
        print("="*30)

        print("Carros    Pedestres")
        print("  (X)        (0)")
        print("  (0)        (X)")
        print("  (0)  ")
        print("="*30)


# laço de repetição infinito para travessia de pedestres
while True:
    menu()
    farol(1)
    while True:
        try:
            v1 = int(input("O Farol para carros está aberto, deseja atravessar?\n1- Sim \n2- Não\n"))
            if v1 < 3 and v1 > 0:
                break
            else:
                print("Insira um valor válido")
        except ValueError:
            print("Insira um valor válido")
    # se a pessoa passar pelo sensor, nesse caso representado pelo input
    if v1 == 1:
        sens1 = True # simualçao do sensor
        if sens1:
            # troca do sinal para amarelo
            sm_verd = False
            sm_ama = True
            farol(2)
            # troca o sinal para vermelho e o sinal de pedestre para verde
            sm_ama = False
            sm_verm = True
            sm1_verm = False
            sm1_verd = True
            farol(3)
            # se a pessoa passar pelo segundo sensor, representado pelo segundo input
            while v2 == 2:
                try:
                    v2 = int(input("Você atravessou?\n1- Sim \n2- Não\n"))
                    if v2 < 2 and v2 > 0:
                        break
                    elif v2 == 2:
                        print("Atravesse")
                    else:
                        print("Insira um valor válido")
                except ValueError:
                    print("Insira um valor válido")
            if v2 == 1:
                sens2 = True
                if sens2:
                    num_travessias += 1
                    # troca o sinal para verde e o de pedestre para vermelho
                    sm_verm = True
                    sm_verd = False
                    sm1_vem = True
                    sm1_verd = False
                    farol(1)
                    # Delay até a proxima pessoa possa atravessar
                    tm.sleep(10)   
            


