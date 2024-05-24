import requests

url = 'http://127.0.0.1:8000/api/monografias/'

headers = {
    'Authorization': 'Token aedd2a38c8a14db09b3af52d868254ba682ee976',
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

print(response.json())  # Exibe a resposta JSON da solicitação
