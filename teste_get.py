import requests

headers = {'Authorization': 'Token ee11c53d836f28c5bd7e4cafbf49c552847aa901'} #6a192de3bb41380ba44d477ecce73d377ebfba1a
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

# Teste endpoint correto:
# assert resultado.status_code == 200 #Se URI estiver incorreta, mostrará erro

# Teste qtde de registros:
# assert resultado.json()['count'] == 2

# Teste de título do primeiro registro
# assert resultado.json()['results'][0]['titulo'] == 'Título teste'