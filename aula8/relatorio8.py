from neo4j import GraphDatabase, basic_auth

from db import GameDatabase

uri = "bolt://18.206.89.38:7687"
user = "neo4j"
password = "insignias-coughs-prints"

db = GameDatabase(uri, user, password)

# Criar jogadores
db.create_player("player1", "Alice")
db.create_player("player2", "Bob")

# Criar uma partida
db.create_match("match1", ["player1", "player2"], result="draw")

# Obter histórico de partidas de um jogador
print("Histórico de partidas do jogador 'player1':")
player1_matches = db.get_player_matches("player1")
for match in player1_matches:
    print("Match ID:", match["match_id"], "- Resultado:", match["result"])

# Obter todos os jogadores
print("\nLista de todos os jogadores:")
all_players = db.get_all_players()
for player in all_players:
    print("ID do jogador:", player["player_id"], "- Nome:", player["player_name"])

# Obter detalhes de uma partida
print("\nDetalhes da partida 'match1':")
match_details = db.get_match_details("match1")
if match_details:
    print("Resultado:", match_details["result"])
    print("Jogadores:", match_details["players"])
else:
    print("Partida não encontrada.")

db.close()            