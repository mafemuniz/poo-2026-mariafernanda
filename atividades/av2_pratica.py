# Sistema de Gestão de Frota e Locação de Veículos

from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo, placa, valor_diaria):
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    def get_modelo(self):
        return self.__modelo

    def get_placa(self):
        return self.__placa

    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_modelo(self, modelo):
        if not modelo.strip():
            raise ValueError("O modelo não pode ficar vazio.")
        self.__modelo = modelo

    def set_placa(self, placa):
        if not placa.strip():
            raise ValueError("A placa não pode ficar vazia.")
        self.__placa = placa

    def set_valor_diaria(self, valor):
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")
        return self.__valor_diaria * dias


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)
        if portas <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")
        self.portas = portas

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel(dias) + 50.00


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        if cilindradas <= 0:
            raise ValueError("As cilindradas devem ser maiores que zero.")
        self.cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel(dias) * 0.90

#Lista centralizada com objetos diferentes

frota = []

def cadastrar_carro():
    try:
        modelo = input("Digite o modelo do carro: ")
        placa = input("Digite a placa: ")
        valor_diaria = float(input("Digite o valor da diária: R$ "))
        portas = int(input("Digite a quantidade de portas: "))

        carro = Carro(modelo, placa, valor_diaria, portas)
        frota.append(carro)
    except ValueError as erro:
        print("Erro:", erro)
    else:
        print("Carro cadastrado com sucesso!")
    finally:
        print("Operação de cadastro finalizada.")

def cadastrar_moto():
    try:
        modelo = input("Digite o modelo da moto: ")
        placa = input("Digite a placa: ")
        valor_diaria = float(input("Digite o valor da diária: R$ "))
        cilindradas = int(input("Digite as cilindradas: "))

        moto = Moto(modelo, placa, valor_diaria, cilindradas)
        frota.append(moto)
    except ValueError as erro:
        print("Erro:", erro)
    else:
        print("Moto cadastrada com sucesso!")
    finally:
        print("Operação de cadastro finalizada.")

def listar_veiculos():
    if not frota:
        print("Nenhum veículo cadastrado.")
        return
    print("\n--- VEÍCULOS CADASTRADOS ---")
    for i, veiculo in enumerate(frota, start=1):
        print(i, "- Modelo:", veiculo.get_modelo(), "| Placa:",
              veiculo.get_placa(), "| Diária: R$", veiculo.get_valor_diaria())

def calcular_aluguel():
    if not frota:
        print("Nenhum veículo cadastrado.")
        return

    listar_veiculos()
    try:
        escolha = int(input("\nDigite o número do veículo: "))
        if escolha < 1 or escolha > len(frota):
            raise ValueError("Veículo inexistente.")
        dias = int(input("Digite a quantidade de dias de aluguel: "))
        veiculo = frota[escolha - 1]
        valor = veiculo.calcular_aluguel(dias)
    except ValueError as erro:
        print("Erro:", erro)
    else:
        print(f"\n--- CÁLCULO DO ALUGUEL ---\nModelo: {veiculo.get_modelo()}\n"
              f"Placa: {veiculo.get_placa()}\nDias: {dias}\nValor total: R$ {valor:.2f}")
    finally:
        print("Operação de cálculo finalizada.")

def menu():
    while True:
        print("\n==============================")
        print(" SISTEMA DE GESTÃO DE FROTA")
        print("==============================")
        print("1 - Cadastrar carro")
        print("2 - Cadastrar moto")
        print("3 - Listar veículos")
        print("4 - Calcular aluguel")
        print("5 - Sair")
        print("==============================")
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_carro()

            elif opcao == 2:
                cadastrar_moto()

            elif opcao == 3:
                listar_veiculos()

            elif opcao == 4:
                calcular_aluguel()

            elif opcao == 5:
                print("Programa encerrado.")
                break

            else:
                raise ValueError("Opção inexistente.")

        except ValueError as erro:
            print("Erro:", erro)
        finally:
            print("Voltando ao menu...")

menu()