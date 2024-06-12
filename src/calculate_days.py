from os import path
from datetime import date
from src.write_error import writeError

# Funcao que calcula a quanto dias um arquivo foi criado
def calculateDays(pathFile: str):
    try:
        # Obtendo a data de criacao do arquivo
        creation_date = date.fromtimestamp(path.getctime(pathFile))
        # Obtendo a data atual
        today = date.today()
        # Calculando os dias
        delta = today - creation_date
        
        return delta.days
    except Exception as e:
        writeError(e)
        exit()