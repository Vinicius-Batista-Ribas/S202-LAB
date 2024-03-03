import json
import pymongo

class Professor:
    def __init__(self,nome):
        self.nome = nome


    def mestrar(self,assunto):
        return f"O professor {self.nome} esta ministrando uma aula sobre {assunto}."

class Aluno:
    def __init__(self,nome):
        self.nome = nome

    def presenca(self):
        return f"O aluno {self.nome} esta presente."

class Aula:
    def __init__(self,professor,assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionarAluno(self,aluno):
        self.alunos.append(aluno)

    def chamada(self):
        listaAlunos = ", ".join([aluno.nome for aluno in self.alunos])
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n{listaAlunos}"

professor = Professor("Lucas")

aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aluno3 = Aluno("Ana")

aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionarAluno(aluno1)
aula.adicionarAluno(aluno2)
aula.adicionarAluno(aluno3)

aluno1.presenca()
aluno2.presenca()
aluno3.presenca()

print(professor.mestrar("Python"))

print(aula.chamada())   

with open('aula 1\\aula.json') as arquivo_json:
    dados_json = json.load(arquivo_json)
print(dados_json) 

# client = pymongo.MongoClient("mongodb://localhost:27017/")

# db = client["Facul"]
# colecao = db["Aulas"]


# colecao.insert_one(dados_json)