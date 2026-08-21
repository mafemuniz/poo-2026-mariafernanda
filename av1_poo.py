class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario
        else:
            print("Erro: o salário deve ser maior que zero.")

    def calcular_salario_final(self):
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500
        else:
            return self.get_salario_base()



# TESTES


# Criando um Gerente
gerente = Gerente(
    "Maria Fernanda",
    "1234",
    8000,
    2000
)

# Criando um Desenvolvedor Senior
desenvolvedor = Desenvolvedor(
    "Gilkka",
    "1235",
    6000,
    "Senior"
)

# Tentativa de alterar diretamente o atributo privado
gerente.__salario_base = -100

# Verificando se o salário protegido foi alterado
print("Salário base do gerente:", gerente.get_salario_base())

# Exibindo os salários finais
print("Funcionários:")

print("Nome:", gerente.nome)
print("Salário final:", "R$", gerente.calcular_salario_final())


print("Nome:", desenvolvedor.nome)
print("Salário final:", "R$", desenvolvedor.calcular_salario_final())

