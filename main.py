import funcoes
_oop = True
while _oop:
    try:
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
            print("[6] Matriz Transposta")
            print("[7] Limpar terminal")
            print("[0] Sair")
            op = int(input("\nO que o usuário deseja fazer: "))

            if op == 0:
                print("Você escolheu sair do programa. Volte sempre!")
                run = False
                _oop = False

            elif op == 1:
                funcoes.soma(funcoes.matrizes[0], funcoes.matrizes[1])
            
            elif op == 2:
                funcoes.sub(funcoes.matrizes[0], funcoes.matrizes[1])
                
            elif op == 3:
                funcoes.mult(funcoes.matrizes[0], funcoes.matrizes[1])

            elif op == 4:
                funcoes.multEsc(funcoes.matrizes[0], funcoes.matrizes[1])

            elif op == 5:
                funcoes.determinante(funcoes.matrizes[0], funcoes.matrizes[1])

            elif op ==6:
                funcoes.transposta(funcoes.matrizes[0], funcoes.matrizes[1])
            
            
            elif op == 7:
                funcoes.cls()
                print("--- MATRIZ 1 ---")
                for l in range(3):
                    for c in range(3):
                        print(f'[{funcoes.matrizes[0][l][c]:^5}]', end=' ')
                    print()

                print("\n--- MATRIZ 2 ---")
                for l in range(3):
                    for c in range(3):
                        print(f'[{funcoes.matrizes[1][l][c]:^5}]', end=' ')
                    print()

    except ValueError:
        print('-------- Digite um valor correto ---------')
        continue