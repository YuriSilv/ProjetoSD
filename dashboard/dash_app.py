# dash_app/dash_apps.py
import dash
import requests
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from dash import dcc, html
from dash.dependencies import Output, Input
from django_plotly_dash import DjangoDash
import plotly.express as px

def request_info_monografia(url_path: str):
    headers = {
        'Authorization': 'Token aedd2a38c8a14db09b3af52d868254ba682ee976',
        'Content-Type': 'application/json',
    }
    response = requests.get(url_path, headers=headers)
    response.raise_for_status()  # Levanta exceções em caso de erro
    return response.json()['data']

def load_dataframe(url):
    data = request_info_monografia(url)
    return pd.DataFrame(data)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    buffer = BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    return image_base64

app = DjangoDash('dash')

# Layout inicial do app
app.layout = html.Div([
    html.H1('Dashboard Interativo', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='author-dropdown',
        placeholder='Selecione um Autor',
        style={'width': '50%', 'margin': 'auto'}
    ),
    html.Img(id='wordcloud-image', style={'display': 'block', 'margin': 'auto'})
])

@app.callback(
    Output('author-dropdown', 'options'),
    Input('author-dropdown', 'id')
)
def update_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    authors = df['autor'].unique()  # Supondo que 'autor' é a coluna com os nomes dos autores
    options = [{'label': 'Todos', 'value': 'Todos'}] + [{'label': author, 'value': author} for author in authors]
    return options

@app.callback(
    Output('wordcloud-image', 'src'),
    Input('author-dropdown', 'value')
)
def update_wordcloud(selected_author):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    if selected_author and selected_author != 'Todos':
        df = df[df['autor'] == selected_author]
    text = ' '.join(df['resumo'])  # Supondo que 'resumo' é a coluna com texto das monografias
    image_base64 = generate_wordcloud(text)
    return 'data:image/png;base64,{}'.format(image_base64)
