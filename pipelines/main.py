from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="produtos")
db.resetDatabase()

# Vendas por dia
result = db.collection.aggregate([
    {"$group": {"_id": "$data_compra", "vendas_por_dia": {"$sum":1}}},
])

writeAJson(result, "Total de vendas por dia")


# 2- Produto mais vendido por compra
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total_vendido": -1}},
    {"$limit": 1}
])

writeAJson(result, "Produto mais vendido por compra")

# 3 - cliente que mais gastou
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result, "Cliente que mais gastou")


# 4 - Produtos com vendas acima de 1

result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "vendas_maior_1": {"$sum": "$produtos.quantidade"}}},
    {"$match": {"vendas_maior_1": {"$gt": 1}}},
    {"$project": {"_id": 1}}
])


writeAJson(result, "Produtos com vendas acima de 1")

