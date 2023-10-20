from conta import (Conta_corrente, Conta_poupanca)
from random import randint

print("Bem vindo ao seu banco.")

escolha = int(input("Digite o tipo de conta você quer criar:\n"
                    "1 - Conta Corrente\n"
                    "2 - Conta Poupança\n"))

nome = input("Digite o seu nome: ")

numero_conta = randint(0, 1000)

match escolha:
    case 1:
        conta = Conta_corrente(numero_conta, nome, 0)

        while True:
            escolha = int(input("Escolha uma opção:\n"
                                "1 - Verificar informações\n"
                                "2 - Deposito\n"
                                "3 - Sacar\n"
                                "0 - Sair"))
            
            match escolha:
                case 1:
                    conta.verificar_info()
                
                case 2:
                    valor = float(input("Qual o valor a depositar:"))
                    conta.deposito(valor)

                case 3:
                    valor = float(input("Qual o valor a depositar:"))
                    conta.sacar(valor)

                case 0:
                    break

                case _:
                    print("Opção invalida")
                    
    
    case 2:
        conta = Conta_poupanca(numero_conta, nome, 0)

        while True:
            escolha = int(input("Escolha uma opção:\n"
                                "1 - Verificar informações\n"
                                "2 - Deposito\n"
                                "0 - Sair"))
            
            match escolha:
                case 1:
                    conta.verificar_info()
                
                case 2:
                    valor = float(input("Qual o valor a depositar:"))
                    conta.deposito(valor)

                case 0:
                    break

                case _:
                    print("Opção invalida")
    
    case _:
        print("Opção invalida")


    
