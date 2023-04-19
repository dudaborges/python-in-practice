import requests

requisicao = requests.get('https://www.youtube.com/')
# trás todo o conteúdo da página
print(requisicao.content)