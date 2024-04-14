class SimpleCLI:
    def __init__(self):
        self.comandos = {}

    def adicionar_comando(self, nome, funcao):
        self.comandos[nome] = funcao

    def executar(self):
        while True:
            comando = input("Digite um comando: ")
            if comando == "sair":
                print("Até logo!")
                break
            elif comando in self.comandos:
                self.comandos[comando]()
            else:
                print("Comando inválido. Tente novamente.")

class Motorista:
    def __init__(self, nome, nota, corridas):
        self.nome = nome
        self.nota = nota
        self.corridas = corridas

class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro


class MotoristaCLI(SimpleCLI):
    def __init__(self, dao_motorista):
        super().__init__()
        self.dao_motorista = dao_motorista
        self.adicionar_comando("criar", self.criar_motorista)
        self.adicionar_comando("ler", self.ler_motorista)
        self.adicionar_comando("atualizar", self.atualizar_motorista)
        self.adicionar_comando("excluir", self.excluir_motorista)

    def criar_motorista(self):
        nome = input("Digite o nome do motorista: ")
        nota = input("Digite A NOTA do motorista: ")
        corridas = []

        while True:
            nota = float(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distância percorrida: "))
            valor = float(input("Digite o valor da corrida: "))
            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")

            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)

            continuar = input("Adicionar outra corrida? (s/n): ")
            if continuar.lower() != 's':
                break

        motorista = Motorista(nome, nota, corridas)
        self.dao_motorista.criar_motorista(motorista)
        print("Motorista criado com sucesso!")

    def ler_motorista(self):
        id_motorista = input("Digite o ID do motorista: ")
        motorista = self.dao_motorista.ler_motorista_por_id(id_motorista)
        if motorista:
            print("Motorista encontrado:")
            print("Nome:", motorista.nome)
            print("Documento:", motorista.documento)
            print("Corridas:")
            for corrida in motorista.corridas:
                print("  Nota:", corrida.nota)
                print("  Distância:", corrida.distancia)
                print("  Valor:", corrida.valor)
                print("  Passageiro:", corrida.passageiro.nome)
                print("  Documento do Passageiro:", corrida.passageiro.documento)
                print()
        else:
            print("Motorista não encontrado.")

    def atualizar_motorista(self):
        id_motorista = input("Digite o ID do motorista que deseja atualizar: ")
        motorista = self.dao_motorista.ler_motorista_por_id(id_motorista)
        if motorista:
            print("Motorista encontrado:")
            print("Nome:", motorista.nome)
            print("Documento:", motorista.documento)

            novo_nome = input("Digite o novo nome do motorista (deixe em branco para manter o mesmo): ")
            novo_documento = input("Digite o novo documento do motorista (deixe em branco para manter o mesmo): ")

            if novo_nome:
                motorista.nome = novo_nome
            if novo_documento:
                motorista.documento = novo_documento

            self.dao_motorista.atualizar_motorista(id_motorista, {'nome': motorista.nome, 'documento': motorista.documento})
            print("Motorista atualizado com sucesso!")
        else:
            print("Motorista não encontrado.")

    def excluir_motorista(self):
        id_motorista = input("Digite o ID do motorista que deseja excluir: ")
        motorista = self.dao_motorista.ler_motorista_por_id(id_motorista)
        if motorista:
            confirmacao = input("Tem certeza que deseja excluir o motorista? (s/n): ")
            if confirmacao.lower() == 's':
                self.dao_motorista.excluir_motorista(id_motorista)
                print("Motorista excluído com sucesso!")
        else:
            print("Motorista não encontrado.")

    def executar(self):
        print("Bem-vindo ao CLI de motoristas!")
        print("Comandos disponíveis: criar, ler, atualizar, excluir, sair")
        super().executar()
