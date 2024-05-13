import requests

url = 'http://127.0.0.1:8000/api/pesquisadores/'

headers = {
    'Authorization': 'Token c0d00a2d1e0f79b94115747edef8c3ae320c1d7a',
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

print(response.json())  # Exibe a resposta JSON da solicitação
