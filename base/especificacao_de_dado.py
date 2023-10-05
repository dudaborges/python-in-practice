#função recebe um argumento do tipo string e retorna um dado tipo inteiro
def setNome(nome: str) -> int:
    return len(nome)

print(setNome("maria"))