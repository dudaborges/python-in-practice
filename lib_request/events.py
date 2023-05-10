import requests

requisicao = requests.get('https://api.github.com/events')
# print(requisicao.json())
print(requisicao.status_code)
# trás informações sobre o servidor que está hospedando a api
# print(requisicao.headers)
print(requisicao.headers)

