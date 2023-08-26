print("Olá, Seja Bem Vindo ao nosso sistema, Por Favor Insira Uma das Opções Abaixo Para Iniciar Sua Operação Bancária: ")

Menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Opção: """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(Menu)

    if opcao == "1":
        valor = float(input("Informe um Valor Para Depósito: "))

        if valor > 0:
            saldo += valor
            
            print(f"Depósito de R$ {valor:.2f} Realizado com Sucesso.")  #Vai aparecer o valor Depositado.
        
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou: Valor de Parâmetro Inválido.")

    elif opcao == "2":
        valor = float(input("Informe um Valor Para Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques =  numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação Falhou: Você Não Possui Saldo Suficiente.")  
            
            print("Faça um Novo Depósito.")  #Ênfase para o usuario realizar um Depósito.

        elif excedeu_limite:
            print("Operação Falhou! O Valor de Saque Excede o Valor Limite.")  #Excedeu o valor do saldo explícito no início, no valor de R$2000

        elif excedeu_saques:
            print("Operação Falhou! Excedeu o Número Máximo de Saque Diário.")
            
            print("Limite Diário de Saque 3x.")  #Ênfase para o usuário, caso não lembre quantas vezes efetuou o saque.

        elif valor > 0:
            saldo -= valor
            
            print(f"Saque de R$ {valor:.2f} Realizado com Sucesso") #Expõe o valor do Saque.
            
            extrato += f"\nSaque: R$ {valor:.2f}" #valor explícito no Saque.
            
            numero_saque += 1   #Vai sempre contabilizar o saque feito e somar +1, até chegar no saque máximo de 3x

        else:
            print("Operação Falhou! Valor da Operação Inválida.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        
        print("Não Foi Realizada Nenhuma Movimentação." if not extrato else extrato)
        
        print(f"\nSaldo: R$ {saldo:.2f}")
        
        print("=========================================")

    elif opcao == "4":
        print("Obrigado Por Utilizar o Nosso Sistema.")
        
        break

    else:
        print("Operação Inválida, Por Favor Selecione Uma Das Opções Abaixo Para Iniciar a Operação Bancária.")