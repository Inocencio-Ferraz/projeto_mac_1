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

def cls():
    os.system('cls')