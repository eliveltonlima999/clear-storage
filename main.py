from psutil import disk_usage
from src.clear_files import clearFiles

# Disco e diretorio dos arquivos
disk_used = disk_usage('/')
dir_files = './arquives'

# Verifica a porcentagem de uso do dico e deleta os arquivos quando
#  a porcentagem for 80%
if (disk_used.percent == 80.0):
    clearFiles(dir_files)
else:
    print(f"O disco ainda não atingiu 80.0% de uso. Porcentagem atual: {disk_used.percent}")
