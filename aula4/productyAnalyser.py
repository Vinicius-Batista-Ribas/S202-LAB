from database import Database

class ProductAnalyzer:
       def VendasPorDia(self,db: Database):
            result = db.collection.aggregate([
                {"$group": {"_id": "$data_compra", "vendas_por_dia": {"$sum":1}}},
            ])
            
            return result
       
       def ProdutoMaisVendido(self, db:Database):
            result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
            ])

            return result
       

       def OMaisRico(self,db: Database):
           result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
            ])
           
           return result
       

       def ProdutosMaior1(self,db:Database):
           result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "vendas_maior_1": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"vendas_maior_1": {"$gt": 1}}},
            {"$project": {"_id": 1}}
            ])
           
           return result