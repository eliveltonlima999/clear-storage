from os import remove, listdir
from src.calculate_days import calculateDays
from src.write_error import writeError

# Funcao que deleta os arquivos
def clearFiles(dirFiles: str):
    try:
        # Obtem a lista de arquivos da pasta
        fileList = listdir(dirFiles)
        for f in fileList:
            # Monta o path do arquivo
            filePath = f"{dirFiles}/{f}"

            # Analisar a necessidade, pois pode haver
            # conflitos com a data de criacao e o armazenamento do
            # disco.
            daysCreatedFile = calculateDays(filePath)

            # Deletando os arquivos criados a mais de 30 dias
            if (daysCreatedFile > 30):
                remove(filePath)
    except Exception as e:
        writeError(e)
        exit()

