
#Sistema bacario com 3 operações

# Deposito
    #todos depositos devem ser armasenados exibido em extrato, somente valores positivos 

#Saque
    # So permitir 3 saques, maximo 500 por saque, se valor do saque for 
    # menor que o saldo mostrar mensagem na tela e mostrar cada saque no 
    # extrato

#Extrato
    # mostrar todas as operacoes e saldo no final, se nao tiver operacoes
    #mostrar nao foram realizadas movimentacoes
    # como deve ser mostrado os valores 1500.45 = R$ 1500.45

saldo = 0
operacao = True
extrato = []
deposito = 0
saque_diario = 0



def depositar(saldo, extrato):
    deposito = float(input("Qual valor deseja depositar?\n>>"))
    deposito = round(deposito, 2)    

    if deposito <= 0:
        print("Valor não suportado, tente novamente")
    else:
        saldo += deposito
        print(f"Valor de {deposito} adicionado com sucesso, seu saldo é {saldo}")
        extrato.append(("Depósito", deposito))
        
    return saldo , extrato


def sacar(saldo, saque_diario, extrato):
    saque = float(input(f" Seu saldo é R${saldo}. Qual valor deseja sacar?\n>>"))
    saque = round(saque, 2)    

    if saque <= 0:
        print("Valor não suportado, tente novamente")
    elif saque_diario >= 3:
        print("Limite de saque diario atingido!")
    elif saque > 500:
        print("Limite maximo de saque R$500,00, tente outro valor")
    elif saque > saldo:
        print(f"Saldo insuficiente! você pode sacar até R${saldo}")
    else:
        saldo -= saque
        saque_diario +=1
        print(f"Valor de R${saque} sacado com sucesso, seu saldo é R${saldo}")
        extrato.append(("Saque", -saque))
    return saldo, saque_diario, extrato

def exibir_extrato(extrato, saldo):
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for tipo, valor in extrato:
                print(f"{tipo} {valor:.2f}")
        print(f"Total:{saldo}") 



while operacao == True:

    opcao = input("""
==== = = Sistema BDJ - Banco do João = = ====  
        Selecione uma opção
        [S] Sacar
        [D] Depositar
        [E] Extrato
        [Q] Sair  
        >>""")
    opcao = opcao.upper().strip()

    if opcao== "S":
        saldo, saque_diario, extrato = sacar(saldo, saque_diario, extrato)
    elif opcao== "D":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao== "E":
        exibir_extrato(extrato, saldo)
    elif opcao == "Q":
        print("Obrigado por usar o BDJ.")
        break
    else:
        print("Opção invalida tente novamente")

print()

