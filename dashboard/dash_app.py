import dash
import requests
import pandas as pd
import plotly.express as px
from dash import dcc, html, callback, Output, Input
from django_plotly_dash import DjangoDash

# Função para fazer a requisição
def request_info_monografia(url_path:str):
    headers = {
        'Authorization': 'Token aedd2a38c8a14db09b3af52d868254ba682ee976',
        'Content-Type': 'application/json',
    }
    response = requests.get(url_path, headers=headers)
    return response.json()['data']

# Função para carregar o dataframe
def load_dataframe(url):
    data = request_info_monografia(url)
    return pd.DataFrame(data)

# Inicializando o aplicativo Dash
app = DjangoDash('dash')  # Substitui dash.Dash

# Layout inicial do app
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

# Callback para atualizar o dropdown e o gráfico
@app.callback(
    [Output('dropdown-selection', 'options'),
     Output('dropdown-selection', 'value')],
    Input('dropdown-selection', 'value')
)
def update_dropdown(value):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    options = [{'label': autor, 'value': autor} for autor in df['autor'].unique()]
    return options, options[0]['value'] if options else None

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    if value is None:
        return px.line()  # Retorna um gráfico vazio se nenhum valor for selecionado
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    dff = df[df.autor == value]
    return px.line(dff, x='nota_final', y='nota_final')
