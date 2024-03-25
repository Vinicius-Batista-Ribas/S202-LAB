from pymongo import MongoClient
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from pymongo import InsertOne, DeleteOne, ReplaceOne

client = MongoClient('localhost', 27017)
db = client['biblioteca']
livros_collection = db['livros']


def listar_livros():
    return list(livros_collection.find())


def buscar_livro(titulo):
    return livros_collection.find_one({"titulo": titulo})


def inserir_livro(livro):
    try:
        livros_collection.insert_one(livro)
        print("Livro inserido com sucesso!")
    except DuplicateKeyError:
        print("Já existe um livro com este título ou ID.")


def atualizar_livro(titulo, novo_livro):
    livros_collection.replace_one({"titulo": titulo}, novo_livro)
    print("Livro atualizado com sucesso!")


def deletar_livro(titulo):
    livros_collection.delete_one({"titulo": titulo})
    print("Livro deletado com sucesso!")


def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Inserir livro")
        print("2. Listar livros")
        print("3. Buscar livro")
        print("4. Atualizar livro")
        print("5. Deletar livro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano de publicação do livro: "))
            preco = float(input("Digite o preço do livro: "))
            novo_livro = {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
            inserir_livro(novo_livro)

        elif opcao == "2":
            print("== Lista de Livros ==")
            livros = listar_livros()
            for livro in livros:
                print(livro)

        elif opcao == "3":
            titulo = input("Digite o título do livro: ")
            livro = buscar_livro(titulo)
            if livro:
                print("Livro encontrado:")
                print(livro)
            else:
                print("Livro não encontrado.")
            

        elif opcao == "4":
            titulo = input("Digite o título do livro que deseja atualizar: ")
            livro = buscar_livro(titulo)
            if livro:
                autor = input("Digite o novo autor do livro: ")
                ano = int(input("Digite o novo ano de publicação do livro: "))
                preco = float(input("Digite o novo preço do livro: "))
                novo_livro = {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
                atualizar_livro(titulo, novo_livro)
            else:
                print("Livro não encontrado.")

        elif opcao == "5":
            titulo = input("Digite o título do livro que deseja deletar: ")
            deletar_livro(titulo)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()