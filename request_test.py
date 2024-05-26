import requests

headers = {
    'Authorization': 'Token aedd2a38c8a14db09b3af52d868254ba682ee976',
    # Remover 'Content-Type' pois requests automaticamente define isso para multipart/form-data quando usamos 'files'
}

def get_monografias():
    url = 'http://127.0.0.1:8000/api/monografias/'
    response = requests.get(url, headers=headers)
    return response.json()

def create_monografia(data):
    url = 'http://127.0.0.1:8000/api/monografias/add/'
    file_path = data.pop('arquivo', None)  # Extrai e remove o caminho do arquivo do dicionário
    files = {'arquivo': open(file_path, 'rb')} if file_path else None
    response = requests.post(url, headers=headers, data=data, files=files)
    if files:
        files['arquivo'].close()  # Fecha o arquivo após o upload
    try:
        return response.json()
    except ValueError:
        return response.text

def update_monografia(monografia_id, data):
    url = f'http://127.0.0.1:8000/api/monografias/update/{monografia_id}/'
    file_path = data.pop('arquivo', None)  # Extrai e remove o caminho do arquivo do dicionário
    files = {'arquivo': open(file_path, 'rb')} if file_path else None
    response = requests.put(url, headers=headers, data=data, files=files)
    if files:
        files['arquivo'].close()  # Fecha o arquivo após o upload
    try:
        return response.json()
    except ValueError:
        return response.text

def delete_monografia(monografia_id):
    url = f'http://127.0.0.1:8000/api/monografias/delete/{monografia_id}/'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        return {'message': 'Monografia deletada com sucesso'}
    else:
        try:
            return response.json()
        except ValueError:
            return response.text
        
def get_pesquisadores():
    url = 'http://127.0.0.1:8000/api/pesquisadores/'
    response = requests.get(url, headers=headers)
    return response.json()

def create_pesquisador(data):
    url = 'http://127.0.0.1:8000/api/pesquisadores/add/'
    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json()
    except ValueError:
        return response.text

def update_pesquisador(pesquisador_id, data):
    url = f'http://127.0.0.1:8000/api/pesquisadores/update/{pesquisador_id}/'
    response = requests.put(url, headers=headers, json=data)
    try:
        return response.json()
    except ValueError:
        return response.text

def delete_pesquisador(pesquisador_id):
    url = f'http://127.0.0.1:8000/api/pesquisadores/delete/{pesquisador_id}/'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        return {'message': 'Pesquisador deletado com sucesso'}
    else:
        try:
            return response.json()
        except ValueError:
            return response.text

"""
monografia_to_update = {
    "id": 31,
    "titulo": "Blockchain e Finanças Descentralizadas (DeFi): Desafios e Oportunidades",
    "resumo": "Este trabalho de conclusão de curso explora a interseção entre blockchain e finanças descentralizadas (DeFi), analisando os desafios e oportunidades dessa nova era financeira baseada em tecnologias descentralizadas. O estudo começa com uma introdução ao blockchain e seus princípios fundamentais de transparência, imutabilidade e descentralização. São discutidos os conceitos-chave da DeFi, como empréstimos peer-to-peer, staking, yield farming e criação de tokens. A pesquisa analisa os desafios técnicos e regulatórios enfrentados pela DeFi, como segurança dos contratos inteligentes, gestão de riscos e conformidade legal. Além disso, são exploradas as oportunidades de inovação na DeFi, como acesso financeiro global, redução de intermediários e novos modelos de negócio. O trabalho conclui destacando a importância da educação e da governança na evolução sustentável da DeFi, visando proporcionar benefícios significativos para a inclusão financeira e a eficiência dos mercados.",
    "palavras_chave": "Finanças; software; gestão",
    "data_entrega": "2024-05-25T11:03:43-03:00",
    "arquivo": "media/aula03.pdf",
    "nota_final": 82.0,
    "area_concentração": "Finanças",
    "autor": 26,
    "orientador": 5,
    "coorientador": 13,
    "banca": [
        5,
        8,
        12,
        13
    ]
}

print(update_monografia(31, monografia_to_update))
"""

"""
print(delete_monografia(31))
"""

"""
monografia_to_add = {
    "id": 30,
    "titulo": "Blockchain e Finanças Descentralizadas (DeFi): Desafios e Oportunidades",
    "resumo": "Este trabalho de conclusão de curso explora a interseção entre blockchain e finanças descentralizadas (DeFi), analisando os desafios e oportunidades dessa nova era financeira baseada em tecnologias descentralizadas. O estudo começa com uma introdução ao blockchain e seus princípios fundamentais de transparência, imutabilidade e descentralização. São discutidos os conceitos-chave da DeFi, como empréstimos peer-to-peer, staking, yield farming e criação de tokens. A pesquisa analisa os desafios técnicos e regulatórios enfrentados pela DeFi, como segurança dos contratos inteligentes, gestão de riscos e conformidade legal. Além disso, são exploradas as oportunidades de inovação na DeFi, como acesso financeiro global, redução de intermediários e novos modelos de negócio. O trabalho conclui destacando a importância da educação e da governança na evolução sustentável da DeFi, visando proporcionar benefícios significativos para a inclusão financeira e a eficiência dos mercados.",
    "palavras_chave": "Finanças; software; gestão",
    "data_entrega": "2024-05-25T11:03:43-03:00",
    "arquivo": "media/aula03.pdf",
    "nota_final": 82.0,
    "area_concentração": "Finanças",
    "autor": 26,
    "orientador": 5,
    "coorientador": 13,
    "banca": [
        5,
        8,
        12,
        13
    ]
}

print(create_monografia(monografia_to_add))
"""

"""
pesquisador_data = {
    "nome": "Maria de Souza",
    "nivel": "Doutorado",
    "lattes": "",
    "linkedin": "",
    "researchgate": "",
    "email": "maria.souza@gmail.com",
    "ativo": True,
    "cargo": "ALUNO"
}

print(create_pesquisador(pesquisador_data))"""