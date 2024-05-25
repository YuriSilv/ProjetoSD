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

def request_info_monografia(url_path: str, with_data_field=True):
    headers = {
        'Authorization': 'Token aedd2a38c8a14db09b3af52d868254ba682ee976',
        'Content-Type': 'application/json',
    }
    response = requests.get(url_path, headers=headers)
    response.raise_for_status()
    if with_data_field:
        return response.json()['data']
    
    return response.json()

def load_dataframe(url, with_data_field=True):
    data = request_info_monografia(url, with_data_field)
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
    html.H1('Dashboard Interativo', style={
        'textAlign': 'center',
        'color': '#007BFF',
        'margin-bottom': '40px'
    }),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='keys-dropdown',
                placeholder='Selecione as Keys',
                style={'width': '100%'}
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([
            dcc.Dropdown(
                id='area-dropdown',
                placeholder='Selecione uma Área de Concentração',
                style={'width': '100%'}
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([
            dcc.Dropdown(
                id='advisor-dropdown',
                placeholder='Selecione um Orientador',
                style={'width': '100%'}
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin-bottom': '40px'}),
    html.Div([
        html.Div([
            html.Img(id='wordcloud-image', style={'max-width': '100%', 'border': '1px solid #007BFF', 'border-radius': '10px'})
        ], style={'flex': '1', 'margin-right': '20px'}),
        html.Div([
            dcc.Graph(id='grade-histogram')
        ], style={'flex': '1'})
    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'margin-bottom': '40px'}),
    html.Div([
        dcc.Graph(id='advisor-bar-chart', style={'width': '100%'})
    ])
], style={'max-width': '1200px', 'margin': 'auto', 'font-family': 'Arial, sans-serif'})

@app.callback(
    Output('keys-dropdown', 'options'),
    Input('keys-dropdown', 'id')
)
def update_keys_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    keys = df['palavras_chave'].unique()
    options = [{'label': key, 'value': key} for key in keys]
    return options

@app.callback(
    Output('area-dropdown', 'options'),
    Input('area-dropdown', 'id')
)
def update_area_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    areas = df['area_concentração'].unique()
    options = [{'label': 'Todas', 'value': 'Todas'}] + [{'label': area, 'value': area} for area in areas]
    return options

@app.callback(
    Output('advisor-dropdown', 'options'),
    Input('advisor-dropdown', 'id')
)
def update_advisor_dropdown_options(_):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    df_pesquisadores = load_dataframe('http://127.0.0.1:8000/api/pesquisadores/', False)
    advisors_ids = df['orientador'].unique()

    advisors = []
    for advisor_id in advisors_ids:
        advisor_name = df_pesquisadores.loc[df_pesquisadores['id'] == advisor_id, 'nome'].values[0]
        advisors.append(advisor_name)
    
    df['nome_orientador'] = df['orientador'].map(dict(zip(advisors_ids, advisors)))

    options = [{'label': 'Todos', 'value': 'Todos'}] + [{'label': advisor, 'value': advisor} for advisor in advisors]
    return options

@app.callback(
    [Output('wordcloud-image', 'src'),
     Output('grade-histogram', 'figure'),
     Output('advisor-bar-chart', 'figure')],
    [Input('keys-dropdown', 'value'),
     Input('area-dropdown', 'value'),
     Input('advisor-dropdown', 'value')]
)
def update_visualizations(selected_key, selected_area, selected_advisor):
    df = load_dataframe('http://127.0.0.1:8000/api/monografias/')
    df_pesquisadores = load_dataframe('http://127.0.0.1:8000/api/pesquisadores/', False)

    advisors_ids = df['orientador'].unique()
    advisors = []
    for advisor_id in advisors_ids:
        advisor_name = df_pesquisadores.loc[df_pesquisadores['id'] == advisor_id, 'nome'].values[0]
        advisors.append(advisor_name)

    df['nome_orientador'] = df['orientador'].map(dict(zip(advisors_ids, advisors)))
    
    if selected_key and selected_key != 'Todos':
        df = df[df['palavras_chave'] == selected_key]
    if selected_area and selected_area != 'Todas':
        df = df[df['area_concentração'] == selected_area]
    if selected_advisor and selected_advisor != 'Todos':
        df = df[df['nome_orientador'] == selected_advisor]
    
    #Wordcloud
    text = ' '.join(df['resumo'])
    clean_text = utils.clean_text(text)
    image_base64 = generate_wordcloud(clean_text)
    
    #Histograma
    fig_histogram = px.histogram(df, x='nota_final', nbins=20, title='Distribuição das Notas Finais',
                                 color_discrete_sequence=['#007BFF'])
    fig_histogram.update_layout(title_font=dict(size=20), xaxis_title='Nota Final', yaxis_title='Frequência')

    #Barras
    df_mean_grade = df.groupby('nome_orientador')['nota_final'].mean().reset_index()
    fig_bar_chart = px.bar(df_mean_grade, x='nome_orientador', y='nota_final', title='Média das Notas Finais por Orientador',
                           color='nota_final', color_continuous_scale=px.colors.sequential.Tealgrn)
    fig_bar_chart.update_layout(title_font=dict(size=20), xaxis_title='Orientador', yaxis_title='Nota Média')

    return f'data:image/png;base64,{image_base64}', fig_histogram, fig_bar_chart
