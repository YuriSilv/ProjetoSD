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
from . import utils

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
    dcc.Dropdown(
        id='area-dropdown',
        placeholder='Selecione uma Área de Concentração',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Dropdown(
        id='advisor-dropdown',
        placeholder='Selecione um Orientador',
        style={'width': '50%', 'margin': 'auto'}
    ),
    html.Div([
        html.Div([
            html.Img(id='wordcloud-image', style={'max-width': '100%'})
        ], style={'flex': '1', 'max-width': '50%', 'margin-right': '10px'}),
        html.Div([
            dcc.Graph(id='grade-histogram', style={'max-width': '100%'})
        ], style={'flex': '1', 'max-width': '50%'})
    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'flexWrap': 'wrap'})
], style={'max-width': '1200px', 'margin': 'auto'})

@app.callback(
    Output('author-dropdown', 'options'),
    Input('author-dropdown', 'id')
)
def update_author_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    authors = df['autor'].unique()  # Supondo que 'autor' é a coluna com os nomes dos autores
    options = [{'label': 'Todos', 'value': 'Todos'}] + [{'label': author, 'value': author} for author in authors]
    return options

@app.callback(
    Output('area-dropdown', 'options'),
    Input('area-dropdown', 'id')
)
def update_area_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    areas = df['area_concentração'].unique()  # Supondo que 'area_concentracao' é a coluna com as áreas de concentração
    options = [{'label': 'Todas', 'value': 'Todas'}] + [{'label': area, 'value': area} for area in areas]
    return options

@app.callback(
    Output('advisor-dropdown', 'options'),
    Input('advisor-dropdown', 'id')
)
def update_advisor_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    advisors = df['orientador'].unique()  # Supondo que 'orientador' é a coluna com os nomes dos orientadores
    options = [{'label': 'Todos', 'value': 'Todos'}] + [{'label': advisor, 'value': advisor} for advisor in advisors]
    return options

@app.callback(
    [Output('wordcloud-image', 'src'),
     Output('grade-histogram', 'figure')],
    [Input('author-dropdown', 'value'),
     Input('area-dropdown', 'value'),
     Input('advisor-dropdown', 'value')]
)
def update_visualizations(selected_author, selected_area, selected_advisor):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    if selected_author and selected_author != 'Todos':
        df = df[df['autor'] == selected_author]
    if selected_area and selected_area != 'Todas':
        df = df[df['area_concentração'] == selected_area]
    if selected_advisor and selected_advisor != 'Todos':
        df = df[df['orientador'] == selected_advisor]
    
    # Gerar Wordcloud
    text = ' '.join(df['resumo'])  # Supondo que 'resumo' é a coluna com texto das monografias
    clean_text = utils.clean_text(text)
    image_base64 = generate_wordcloud(clean_text)
    
    # Gerar Histograma
    fig = px.histogram(df, x='nota_final', nbins=20, title='Distribuição das Notas Finais')
    
    return 'data:image/png;base64,{}'.format(image_base64), fig
