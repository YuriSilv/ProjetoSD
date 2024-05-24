from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__, suppress_callback_exceptions=True)

# Layout
app.layout = html.Div([
    html.H1("Exemplo de Dash com Plotly Express"),

    dcc.Graph(id='scatter-plot'),

    # Adicione outros componentes HTML ou Dash conforme necessário
])

# Callback para atualizar o gráfico com base na seleção do usuário
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown', 'value')]  # Substitua 'dropdown' pelo ID do componente que deseja usar como entrada
)
def update_graph(selected_year):
    filtered_df = df[df['year'] == selected_year]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', color='continent', size='pop', hover_name='country',
                     log_x=True, size_max=60)
    return fig