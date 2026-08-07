# Laboratório 3 - E-commerce

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem / 100)


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


livro = Livro("Dom Casmurro", 50.0, "Machado de Assis")
eletronico = Eletronico("Smartphone", 1200.0, 127)

livro.aplicar_desconto(15)
eletronico.aplicar_desconto(10)

print(f"Livro: {livro.nome} - R$ {livro.preco:.2f}")
print(f"Eletrônico: {eletronico.nome} - R$ {eletronico.preco:.2f}")
