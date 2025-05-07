import funcoes

print('\nSeja bem vindo a calculadora de matrizes.')
op1 = int(input("Quer gerar matrizes automaticas [1] Sim [2] Não: "))

if op1 == 1:
        funcoes.cls()
        funcoes.gerar_matriz()


elif op1 == 2: 
    print("\nCriando primeira matriz:")
    funcoes.matriz()
            
    print("\nCriando segunda matriz:")
    funcoes.matriz()


run = True
while run:
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Multiplicação por escalar") 
    print("[5] Determinante")
    print("[0] Sair")
    op = int(input("\nO que o usuário deseja fazer: "))

    if op == 0:
        #funcoes.cls()
        print("Você escolheu sair do programa. Volte sempre!")
        run = False

    elif op == 1:
        #funcoes.cls()
        funcoes.soma(funcoes.matrizes[0], funcoes.matrizes[1])
    
    elif op == 2:
        #funcoes.cls()
        funcoes.sub(funcoes.matrizes[0], funcoes.matrizes[1])
        
    elif op == 3:
        #funcoes.cls()
        funcoes.mult(funcoes.matrizes[0], funcoes.matrizes[1])

    elif op == 4:
        #funcoes.cls()
        funcoes.multEsc(funcoes.matrizes[0], funcoes.matrizes[1])

    elif op == 5:
        #funcoes.cls()
        funcoes.determinante(funcoes.matrizes[0], funcoes.matrizes[1])
    
    
    elif op == 6:
        #funcoes.cls()
        funcoes.gerar_matriz()