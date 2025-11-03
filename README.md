# 🏦 Sistema Bancário Simples em Python 🐍

Este é um projeto de console simples que simula operações bancárias básicas, demonstrando conceitos fundamentais de Programação Orientada a Objetos (POO) em Python.

## ✨ Funcionalidades

* **Criação de Contas:** Permite ao usuário criar uma Conta Corrente ou uma Conta Poupança.
* **Operações Bancárias:**
    * Depositar
    * Sacar
    * Ver Saldo
* **Recursos Específicos:**
    * **Conta Corrente:** Possui um limite de cheque especial (definido como R$500 no código).
    * **Conta Poupança:** Possui uma função para aplicar juros sobre o saldo.
* **Menu Interativo:** Um menu de console limpo e interativo para navegar pelas funções.

## 💻 Conceitos de POO Aplicados

Este projeto foi desenvolvido para praticar e demonstrar os principais pilares da Programação Orientada a Objetos:

### 1. Encapsulamento
O saldo da conta (`__saldo`) é um atributo privado. Ele só pode ser acessado ou modificado através de métodos públicos (como `depositar`, `sacar`) ou propriedades (`@property` e `@saldo.setter`), garantindo que regras de negócio (como não permitir saldo negativo no setter) sejam aplicadas.

### 2. Herança
Existe uma classe base `ContaBancaria` que define os atributos e métodos comuns a todas as contas (titular, saldo, depositar, sacar, ver_saldo).

As classes `ContaCorrente` e `ContaPoupanca` herdam de `ContaBancaria`, reutilizando o código base e adicionando suas próprias funcionalidades e regras específicas.

### 3. Polimorfismo
Os métodos `sacar` e `ver_saldo` são sobrescritos (overriding) nas classes filhas:
* `ContaCorrente.sacar()`: Modificado para incluir a lógica do limite.
* `ContaPoupanca.ver_saldo()`: Modificado para incluir a taxa de juros.
* `ContaCorrente.ver_saldo()`: Modificado para incluir o limite.

## 🚀 Como Executar

Este projeto não requer nenhuma biblioteca externa além das bibliotecas padrão do Python (`time` e `os`).

1.  **Clone o repositório (opcional):**
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
    cd NOME-DO-REPOSITORIO
    ```
    *(Substitua `SEU-USUARIO` e `NOME-DO-REPOSITORIO` pelos seus dados)*

2.  **Salve o Código:**
    Salve o código fornecido em um arquivo com a extensão `.py` (por exemplo, `banco.py`).

3.  **Execute o Script:**
    Abra seu terminal ou prompt de comando no diretório onde o arquivo foi salvo e execute o comando:

    ```bash
    python banco.py
    ```
    *(Se você usa python3, o comando pode ser `python3 banco.py`)*

4.  **Interaja com o Menu:**
    O programa será iniciado no terminal, e você poderá seguir as instruções do menu.
