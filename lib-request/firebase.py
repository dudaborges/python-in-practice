import requests

requisicao = requests.get('https://requests-16843-default-rtdb.firebaseio.com/.json')
print(requisicao)
print(requisicao.json())

# criar
# os dados precisam estar em formato de dicionário e string.
dados = '{"Nome:": "Maria"}'
requisicao = requests.post('https://requests-16843-default-rtdb.firebaseio.com/.json', data=dados)
print(requisicao.json())

#atualizar, se o dado que você quer atualizar não existe, ele cria outro dado
dados = '{"Nome:": "Maria", "Turma": "Palhoca", "Idade": "23"}'
requisicao = requests.patch('https://requests-16843-default-rtdb.firebaseio.com//-NTP0fFHpQWuUTQVZGgA.json', data=dados)
print(requisicao.json())

#deletar
requisicao = requests.delete('https://requests-16843-default-rtdb.firebaseio.com//1.json')
print(requisicao.json())

# substitui o dado
requisicao = requests.delete('https://requests-16843-default-rtdb.firebaseio.com//1.json')
print(requisicao.json())