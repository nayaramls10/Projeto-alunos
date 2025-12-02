from aluno import Aluno

class AlunoDB:
    def __init__(self):
        self.alunos = []


    def adicionarAluno(self):
        nome = input("Digite um nome:  ")
        matricula = input("Matrícula:  ")
        nota = float(input("Nota: "))

        aluno = Aluno(nome,matricula,nota)
        self.alunos.append(aluno)

        print(f" Aluno {nome}, cadastrado! ")

    def listarAluno(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado! ")
            return
        print("\n#----Alunos----")
        for aluno in self.alunos:
            print(aluno)
        print()
    

    def menu(self):
        while(True):
            print("""
                ==== Sistema de cadastro de alunos == 
                1. Cadastrar Aluno : 
                2. Listas alunos : 
                3. Atualizar aluno: 
                4. Excluir aluno: 
                5. Sair """)
        
            opcao = input("Escolha a opção desejada :  ")

            match opcao:
                case "1":
                    self.adicionarAluno()
                case "2":
                    self.listarAluno()
                case "3":
                    self.atualizarAluno()
                case "4":
                    self.deletarAluno()
                case _:
                    break

if __name__ == "__main__":
    bancoDados = AlunoDB()
    bancoDados.menu()

            


 
