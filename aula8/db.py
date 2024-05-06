from neo4j import GraphDatabase, basic_auth


class GameDatabase:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self):
        self._driver.close()

    def create_player(self, player_id, player_name):
        with self._driver.session() as session:
            session.write_transaction(self._create_player, player_id, player_name)

    @staticmethod
    def _create_player(tx, player_id, player_name):
        tx.run("CREATE (:Player {id: $player_id, name: $player_name})", player_id=player_id, player_name=player_name)

    def update_player(self, player_id, new_name):
        with self._driver.session() as session:
            session.write_transaction(self._update_player, player_id, new_name)

    @staticmethod
    def _update_player(tx, player_id, new_name):
        tx.run("MATCH (p:Player {id: $player_id}) SET p.name = $new_name", player_id=player_id, new_name=new_name)

    def delete_player(self, player_id):
        with self._driver.session() as session:
            session.write_transaction(self._delete_player, player_id)

    @staticmethod
    def _delete_player(tx, player_id):
        tx.run("MATCH (p:Player {id: $player_id}) DETACH DELETE p", player_id=player_id)

    def create_match(self, match_id, players, result=None):
        with self._driver.session() as session:
            session.write_transaction(self._create_match, match_id, players, result)

    @staticmethod
    def _create_match(tx, match_id, players, result):
        tx.run("CREATE (m:Match {id: $match_id, result: $result})", match_id=match_id, result=result)
        for player_id in players:
            tx.run("MATCH (p:Player {id: $player_id}), (m:Match {id: $match_id}) CREATE (p)-[:PARTICIPATED_IN]->(m)", player_id=player_id, match_id=match_id)

    def get_player_matches(self, player_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_player_matches, player_id)

    @staticmethod
    def _get_player_matches(tx, player_id):
        result = tx.run("MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match) RETURN m.id AS match_id, m.result AS result", player_id=player_id)
        return [{"match_id": record["match_id"], "result": record["result"]} for record in result]

    def get_all_players(self):
        with self._driver.session() as session:
            return session.read_transaction(self._get_all_players)

    @staticmethod
    def _get_all_players(tx):
        result = tx.run("MATCH (p:Player) RETURN p.id AS player_id, p.name AS player_name")
        return [{"player_id": record["player_id"], "player_name": record["player_name"]} for record in result]

    def get_match_details(self, match_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_match_details, match_id)

    @staticmethod
    def _get_match_details(tx, match_id):
        result = tx.run("MATCH (m:Match {id: $match_id})-[:PARTICIPATED_IN]->(p:Player) RETURN m.result AS result, collect(p.name) AS players", match_id=match_id)
        record = result.single()
        if record:
            return {"result": record["result"], "players": record["players"]}
        else:
            return None
            
