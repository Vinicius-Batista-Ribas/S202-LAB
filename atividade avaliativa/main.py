from database import Database
from writeAJson import writeAJson
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database("mongodb://localhost:27017/", "motorista_app")
motorista_dao = MotoristaDAO(db)


motorista_cli = MotoristaCLI(motorista_dao)
motorista_cli.executar()