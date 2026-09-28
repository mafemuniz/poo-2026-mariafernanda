
class Pessoa:
    def __init__(self, nome, cpf, mensalidade_base):
        self._nome = nome
        self._cpf = cpf
        self._mensalidade_base = mensalidade_base

    def calcular_pagamento(self):
        return self._mensalidade_base


class Aluno(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, nota_desempenho):
        super().__init__(nome, cpf, mensalidade_base)
        self.nota_desempenho = nota_desempenho

    def calcular_pagamento(self):
        if self.nota_desempenho >= 9.0:
            return self._mensalidade_base * 0.80
        return self._mensalidade_base


class Professor(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, horas_extras):
        super().__init__(nome, cpf, mensalidade_base)
        self.horas_extras = horas_extras

    def calcular_pagamento(self):
        return self._mensalidade_base + (self.horas_extras * 40)


def exibir_relatorio_financeiro(pessoa):
    print("\n===== RELATÓRIO FINANCEIRO =====")
    print("Nome:", pessoa._nome)
    print("CPF:", pessoa._cpf)
    print("Valor final: R$", format(pessoa.calcular_pagamento(), ".2f"))
    print("================================")


def ler_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor > 0:
                return valor
            else:
                print("Erro: digite um valor maior que zero.")

        except ValueError:
            print("Erro: digite um número válido.")


def ler_inteiro_nao_negativo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor >= 0:
                return valor
            else:
                print("Erro: digite um número inteiro maior ou igual a zero.")

        except ValueError:
            print("Erro: digite um número inteiro válido.")


def main():
    print("===== SISTEMA DE GESTÃO ESCOLAR =====")
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Professor")

    opcao = input("Escolha uma opção: ")

    try:
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        mensalidade = ler_float_positivo("Digite o valor base: R$ ")

        if opcao == "1":
            nota = ler_float_positivo("Digite a nota de desempenho: ")

            pessoa = Aluno(nome, cpf, mensalidade, nota)

        elif opcao == "2":
            horas = ler_inteiro_nao_negativo("Digite as horas extras: ")

            pessoa = Professor(nome, cpf, mensalidade, horas)

        else:
            print("Opção inválida.")
            return

        exibir_relatorio_financeiro(pessoa)

    except Exception as erro:
        print("Ocorreu um erro:", erro)

    finally:
        print("\nGeração do relatório concluída ou interrompida.")


main()