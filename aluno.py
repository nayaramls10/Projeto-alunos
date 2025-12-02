class Aluno:
    
    def __init__(self,nome,matricula,nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota 

    def __str__(self):
        return f"Nome: {self.nome} | Matrícula: {self.matricula}| nota: {self.nota}\n"