nomes = ['maria', 'eduarda', 'julia']

def lenNome(nome):
    print(f'{nome} tem {len(nome)} caracteres')

nome = [lenNome(nome) for nome in nomes]

#é a mesma coisa que fazer isso aqui:

def lenNome2(nome):
    print(f'{nome} tem {len(nome)} caracteres')

for nome in nomes:
    lenNome2(nome)