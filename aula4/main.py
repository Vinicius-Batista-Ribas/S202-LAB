from database import Database
from productyAnalyser import ProductAnalyzer as pa
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="produtos")
db.resetDatabase()

analyzer = pa()
# Vendas por dia
result = analyzer.VendasPorDia(db)
writeAJson(result, "Total de vendas por dia")

result = analyzer.ProdutoMaisVendido(db)
writeAJson(result, "Produto mais vendido por compra")

result = analyzer.OMaisRico(db)
writeAJson(result, "Cliente que mais gastou")

result = analyzer.ProdutosMaior1(db)
writeAJson(result, "Produtos com vendas acima de 1")

