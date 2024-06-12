def writeError(e: Exception):
    # Em caso de erro, escreve no arquivo para facilitar a correcao
        fileErrors = open('./errors.txt', 'a')
        fileErrors.write(f"{e}\n")
        fileErrors.close()