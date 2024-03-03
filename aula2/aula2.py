import json
import pymongo


with open('aula2\\aula.json') as arquivo_json:
    dados_json = json.load(arquivo_json)
print(dados_json) 

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Facul"]
colecao = db["Aulas"]


colecao.insert_one(dados_json)