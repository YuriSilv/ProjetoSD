from django.shortcuts import render
import requests
import pandas as pd

def request_info_monografia(url_path:str):
    headers = {
        'Authorization': 'Token aedd2a38c8a14db09b3af52d868254ba682ee976',
        'Content-Type': 'application/json',
    }
    #url = 'http://127.0.0.1:8000/api/monografias/'
    response = requests.get(url_path, headers=headers)
    return response.json()

def load_dataframe(url):
    return pd.read_json(request_info_monografia(url))

#df = load_dataframe('http://127.0.0.1:8000/api/monografias/')

def dash_view(request):
    return render(request, 'dash.html')