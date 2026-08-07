# Laboratório 2 - Escola

class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina


class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula


professor = Professor("Ana Silva", "123.456.789-00", "ana@email.com", "Programação")
aluno = Aluno("João Souza", "987.654.321-00", "joao@email.com", "2024001")

print("Professor:")
professor.exibir_perfil()
print(f"Disciplina: {professor.disciplina}")

print("\nAluno:")
aluno.exibir_perfil()
print(f"Matrícula: {aluno.matricula}")
