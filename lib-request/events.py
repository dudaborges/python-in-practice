import requests

requisicao = requests.get('https://api.github.com/events')
print(requisicao.json())
