# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# y luego visite el sitio 
# http://127.0.0.1:8050/ 
# en su navegador.

import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas 
df = pd.DataFrame({
    "Tipo de persona": ["Gallo", "Gallo", "Normal", "Normal", "Buho", "Buho"],
    "Numero de personas": [6, 7, 8, 9, 4, 3],
    "Tipo de colchon": ["Fuerte", "Suave", "Fuerte", "Suave", "Fuerte", "Suave"]
})

fig = px.bar(df, x="Tipo de persona", y="Numero de personas", color="Tipo de colchon", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Mi primer tablero en Dash Modificado'),

    html.Div(children='''
        Histograma de casos según tipo de persona y tipo de colchon
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children='''
        En este gráfico se observa el numero de personas que prefieren un colchon fuerte o sauve dependiendo de la cantidad de horas que duermen
    '''),
    html.Div(
        className="Columnas",
        children=[
            html.Ul(id='my-list', children=[html.Li(i) for i in df.columns])
        ],
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
