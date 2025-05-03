import os
matrizes = []

def matriz(): #Criação das matrizes
    matriz = [[0,0,0],[0,0,0],[0,0,0]]

    for l in range(3):
        for c in range(3):
            matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]: '))

    for l in range(3):
        for c in range(3):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()

    matrizes.append(matriz)


def soma(m1, m2): #soma de matrizes
    print("--- A SOMA DAS MATRIZ 1 E A MATRIZ 2 É ---")
    resultado = []
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append(m1[l][c] + m2[l][c])
            resultado.append(linha)
            print(f'[{resultado[l][c]:^5}]', end='')
        print()

def sub(m1, m2): #Subtração de matrizes
    print("--- A SUBTRAÇÃO DAS MATRIZ 1 E A MATRIZ 2 É ---")
    resultado = []
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append(m1[l][c] - m2[l][c])
            resultado.append(linha)
            print(f'[{resultado[l][c]:^5}]', end='')
        print()

def mult(m1, m2): #Multiplicação de matrizes
    print("--- A MULTIPLICAÇÃO DAS MATRIZ 1 E A MATRIZ 2 É ---")
    resultado = []
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append(m1[l][c] * m2[l][c])
            resultado.append(linha)
            print(f'[{resultado[l][c]:^5}]', end='')
        print()

def div(m1, m2): #Divisão de matrizes
    print("--- A DIVISÃO DAS MATRIZ 1 E A MATRIZ 2 É ---")
    resultado = []
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append(m1[l][c] / m2[l][c])
            resultado.append(linha)
            print(f'[{resultado[l][c]:^5}]', end='')
        print()


def determinante(m1, m2): #Determinante
    opcao = int(input("Você deseja realizar o determinante de qual matriz [1] ou [2]: "))
    running = True
    while running:
        if opcao == 1:
            m01 = m1[0][0] * (m1[1][1] * m1[2][2] - m1[1][2] * m1[2][1])
            m02 = m1[0][1] * (m1[1][0] * m1[2][2] - m1[1][2] * m1[2][0])
            m03 = m1[0][2] * (m1[1][0] * m1[2][1] - m1[1][1] * m1[2][0])
            print(f'--- O DETERMINANTE DA MATRIZ é: ', m01 - m02 + m03)
            break
        
        elif opcao == 2:
            m11 = m2[0][0] * (m2[1][1] * m2[2][2] - m2[1][2] * m2[2][1])
            m22 = m2[0][1] * (m2[1][0] * m2[2][2] - m2[1][2] * m2[2][0])
            m33 = m2[0][2] * (m2[1][0] * m2[2][1] - m2[1][1] * m2[2][0])
            print(f'--- O DETERMINANTE DA MATRIZ é: ', m11 - m22 + m33)
            break
        

def cls(): #Limpar o código
    os.system('cls')