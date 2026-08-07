# Laboratório 1 - Veículos

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas


carro = Carro("Toyota", "Corolla", 4)
print(f"Marca: {carro.marca}")
print(f"Modelo: {carro.modelo}")
print(f"Quantidade de portas: {carro.qtd_portas}")
