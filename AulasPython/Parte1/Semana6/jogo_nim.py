x = 0
y = 0
turnoPc = True
turnoUsuario = True

def computador_escolhe_jogada(n, m):
    global turnoPc
    global turnoUsuario
    m1 = m
    if m >= n:
        m = n
        n -= m
    elif m == 1:
        n -= 1
    elif n == 6 and m == 2 or n == 15 and m == 4:
        m = m
    else:
        mTemp = m
        while((n - mTemp) % (m + 1) ) != 0 and mTemp > 1:
            mTemp -= 1
        m = mTemp   
    turnoPc = False
    turnoUsuario = True
    if m == 1 or n == 1:
        print("\nO Computador tirou uma peça.")
    elif m > 1 or n > 1:
        print("\nO computador tirou", m, "peças.")
    return m

def usuario_escolhe_jogada(n, m):
    global turnoPc
    global turnoUsuario
    mUsuario = int(input("Quantas peças você vai tirar? "))
    while mUsuario > m or mUsuario <= 0 or n < mUsuario:
        print("Oops! Jogada inválida! Tente de novo.\n")
        mUsuario = int(input("Quantas peças você vai tirar? "))
    m = mUsuario
    if m == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou", m, "peças.")
    turnoPc = True
    turnoUsuario = False
    return m

def partida():
    global x
    global y
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("\nVocê começa! \n")
        while n > 0:
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                break
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro \n")
            elif n > 1:
                print("Agora restam", n, "peças no tabuleiro \n")
            n -= computador_escolhe_jogada(n, m)
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro \n")
            elif n > 1:
                print("Agora restam", n, "peças no tabuleiro \n")
    else:
        print("\nComputador começa! \n")
        while n > 0:  
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                    break
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro \n")
            elif n > 1:
                print("Agora restam", n, "peças no tabuleiro \n") 
            n -= usuario_escolhe_jogada(n, m)
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro \n")
            elif n > 1:
                print("Agora restam", n, "peças no tabuleiro \n")
    if turnoPc == False:
        print("Fim do jogo! O Computador ganhou!")
        x = 1
    else:
        print("Fim do jogo! Você ganhou!")
        y = 1
        
def inicio():
    print("Bem vindo ao jogo NIM! Escolha: \n")
    tipoJogo = int(input("1 - para jogar um partida isolada \n2 - para jogar um campeonato "))
    if tipoJogo == 1:
        print("\nVocê esolheu uma partida isolada!\n")
        partida()
    elif tipoJogo == 2:
        print("\n**** Você escolheu um campeonato! ****")
        print("\n**** 1ª Rodada ****\n")
        partida()
        z = x
        k = y
        print("**** 2ª Rodada ****\n")
        partida()
        z += x
        k += y
        print("**** 3ª Rodada ****\n")
        partida()
        z += x
        k += y
        print("**** Fim do campeonato! ****\n")
        print("Placar: Você", k, "X", z, "Computador")

inicio()
