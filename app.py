
import time     
import os     
  
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



# Classe base - ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado (encapsulado)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_novo):
        if saldo_novo >= 0:
            self.__saldo = saldo_novo
        else:
            print("ERRO! O valor precisa ser positivo.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("ERRO! O valor precisa ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("ERRO! O valor precisa ser positivo.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("ERRO! Saldo insuficiente.")

    def ver_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.__saldo:.2f}")



# Classe filha - ContaCorrente
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("ERRO! O valor precisa ser positivo.")
        elif valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado (usando limite se necessário).")
        else:
            print("ERRO! Saldo insuficiente, mesmo com o limite.")

    def ver_saldo(self):
        print(f"Conta Corrente - Titular: {self.titular} | Saldo: R${self.saldo:.2f} | Limite: R${self.limite:.2f}")



# Classe filha - ContaPoupanca

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_juros=0.05):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        rendimento = self.saldo * self.taxa_juros
        self.saldo += rendimento
        print(f"Juros aplicados: R${rendimento:.2f}. Novo saldo: R${self.saldo:.2f}")

    def ver_saldo(self):
        print(f"Conta Poupança - Titular: {self.titular} | Saldo: R${self.saldo:.2f} | Juros: {self.taxa_juros*100:.1f}%")


# Função de menu interativo
def menu():
    print("\n==============================")
    print("         MENU DO BANCO ")
    print("==============================")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Aplicar juros (Poupança)")
    print("5 - Sair")
    print("==============================")



# Programa principal
limpar_tela()
print("Bem-vindo ao Banco Python!\n")

# Escolha do tipo de conta
tipo = input("Você deseja criar uma conta Corrente (C) ou Poupança (P)? ").upper()
titular = input("Digite o nome do titular: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

# Criação do objeto da conta
if tipo == "C":
    conta = ContaCorrente(titular, saldo_inicial)
elif tipo == "P":
    conta = ContaPoupanca(titular, saldo_inicial)
else:
    print("Tipo inválido! Encerrando programa.")
    exit()

# Loop principal do menu
while True:
    time.sleep(1)      # pausa para dar sensação de fluidez
    limpar_tela()      # limpa o terminal
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
        time.sleep(1.5)

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
        time.sleep(1.5)

    elif opcao == "3":
        conta.ver_saldo()
        input("\nPressione ENTER para continuar...")

    elif opcao == "4":
        if isinstance(conta, ContaPoupanca):
            conta.aplicar_juros()
        else:
            print("ERRO! Essa opção é exclusiva para contas poupança.")
        time.sleep(1.5)

    elif opcao == "5":
        print("Encerrando... Obrigado por usar o Banco! ")
        time.sleep(1.5)
        limpar_tela()
        break

    else:
        print("Opção inválida, tente novamente.")
        time.sleep(1.5)
