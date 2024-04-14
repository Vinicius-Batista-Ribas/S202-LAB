from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, nome: str, documento: str):
        try:
            res = self.db.collection.insert_one({"nome": nome, "documento": documento, "corridas": []})
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")
            return None

    def update_motorista(self, id: str, nome: str, documento: str):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome, "documento": documento}})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista excluído: {res.deleted_count} documento(s) excluído(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao excluir o motorista: {e}")
            return None
