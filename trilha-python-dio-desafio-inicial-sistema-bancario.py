menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        dep = float(input("Digite o quanto voce quer depositar\n"))
        if dep > 0:
            saldo += dep
            extrato += (f"Deposito de R$ {dep: .2f}\n")
        else:
            print("Operacao falhou! Valor invalido de deposito.")

    elif opcao == "2":
        excedeu_saque = numero_saques > LIMITE_SAQUES
        
        if not excedeu_saque:
            saque = float(input("Digite o quanto voce quer sacar.\n"))
            excedeu_saldo = saque > saldo
            excedeu_limite = saque > 500
            if not excedeu_saldo and not excedeu_limite:
                saldo -= saque
                extrato += (f"Saque de R$: {saque: .2f}\n")
            else:
                if excedeu_saldo:
                    print("Nao foi possivel efetuar a operacao! Valor informado maior que saldo atual.")
                else:
                    print("Nao foi possivel efetuar a operacao! Valor informado excedeu o limite máximo de saque.")

        else:
            print("Limite de saques diarios esgotados! Volte amanha.")

    elif opcao == "3":
        print(f"{'EXTRATO'.center(30, "=")}\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"O saldo atual é: R$ {saldo: .2f}\n")
        print(f"{''.center(30, "=")}")
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")