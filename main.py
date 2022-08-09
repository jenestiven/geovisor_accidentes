
# importar las librerias necesarias para el dashboard
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input,Output
import plotly.express as px
import dash_daq as daq 
import dash_mantine_components as dmc

# leer los datos csv o excel necesarios
data_heridos_opt = pd.read_csv('data\dataset_heridos.csv')
data_muertos_opt = pd.read_csv('data\dataset_muertos.csv')
sexo= pd.read_excel('data\sexoJH.xlsx',sheet_name='Hoja1')
sexoh= pd.read_excel('data\sexohJH.xlsx',sheet_name='Hoja1')

# Al no poder importar estas listas del modulo 'codigo_estadisticas' por problema tecnico
# las repliqué aca en el 'main' 
ejeyHistograma = [208, 113, 105, 126, 133, 137, 178] #datos tomados manualmente 
ejexHistograma= ["LUN","MAR","MIER","JUE","VIE","SAB","DOM"]#datos tomados manualmente

ejeyHoras = [29, 26, 22, 32, 29, 35, 38, 29, 39, 36, 35, 35, 35, 41, 46, 43, 45, 49, 48, 26, 43, 37, 30]#datos tomados manualmente
ejexHoras = ["1 am ","2 am ","3 am ","4 am ","5 am ","6 am ","7 am ","8 am ","9 am ","10 am ","11 am ","12 pm","1 pm",
"2 pm","3 pm","4 pm","5 pm","6 pm","7 pm","8 pm","9 pm","10 pm","11 pm"]#datos tomados manualmente

# el token necesario para leer las diferentes cartográfias
token = 'pk.eyJ1IjoiamVuZXN0aXZlbiIsImEiOiJjbDZpOGo0OGgxNTg2M2RrZXh2endtaTNxIn0._4TgQS_XY2QaJpix0HhtpA'


# comenzar la aplicaion 
app = dash.Dash(__name__)
app.title = 'Geoportal Accidentalidad' #titulo

app.layout = html.Div(
    style={'background':'#F8F8FF'}, # color de fondo 
    children=[

        html.Div(    #html.Div crea una division de html en el layout donde se van a mostrar los items del layout
            className="pkcalc-banner", #clase importada desde los assets
            children=[
                html.A(
                    id = "geo-logo",
                    children=[html.Img(src="assets\globo.png")] #logo
                ),
                html.H2("Geoportal de accidentalidad en Cali")  
            ]),
        html.Div(
            className="pkcalc-bannerder",
            children=[
                html.A(
                    id = "derecha-logo",
                    children=[html.Img(src="assets\logoUV_Oficial_Rojo.jpg")]
                )
            ]),
            html.Div(
            className="p",
            children=[
                html.P('PROBLEMATICA: ')
            ]),
            html.Div(
            className="p",      # division de tipo p, para poder ingresar texto 
            children=[
                html.P(
                        '''
                        En Cali, el número de personas que tienen un vehículo propio ha aumentado, a partir
                        de esto se han evidenciado diversos cambios en el tránsito de la ciudad, uno de los
                        campos que se ha visto afectado es el de la accidentalidad, existen diversas clases de
                        accidentes y con ellas distintas causas.
                        Para este proyecto se tomaron las causas más generales, las cuales son: exceso de
                        velocidad, servicio del vehículo, hora del día, temporada del año (meses). Aún no existia
                        un geovisor de accidentes en la ciudad de Cali, donde se muestre zonas críticas, dado
                        que se quiere realizar un geovisor que contenga estadísticas como histogramas,
                        gráficos de barras, gráficos de pastel, con distintas variables en los análisis como años,
                        horas pico, sexo, clase accidente. Esto para brindar una información completa a las
                        personas que se movilizan por la ciudad.
                        
                        ''')
        ]),
        html.Br(),
        html.Br(), # espacios en el layout
        html.Br(),
        html.Br(),
        html.Div(
            className="container-radio",
            children=[
                html.Div([
                    dcc.RadioItems(                 #creo los radioitems en los cuales se puede escoger si ver el mapa
                        id='radio-items',           # de muertos o de heridos
                        options=['Muertes','Heridos'],
                        value='Muertes', 
                        inline=True),
                    html.Div(id='output-radio')
                ])
            ]),
            html.Br(),
            html.Div(
            className="container-radio",
            children=[                       # radiotem para escoger la cartográfia
                html.Div([                      
                    dcc.RadioItems(
                        id='radio-itemscapas',
                        options=['streets','dark','open-street-map','satellite','light'],
                        value='dark', 
                        inline=True),
                    html.Div(id='output-radiocapas')
                ])
            ]),
        html.Br(),
        html.Div(
            className="map",
            children=[
                html.Div([
                    dcc.Graph(                      # se crea el primer grafico donde ira el mapa interactivo
                        id='my-map',
                        figure={})
                ])
        ]),
        html.Div(
            className="container",
            children=[
                html.Div([                          #se crea el dropdown donde se puede escoger que estadisticas de muertos quieres ver
                    dcc.Dropdown(
                        id='dropdown-deaths',
                        options = [
                            {'label': 'AÑO','value':'AÑO'},
                            {'label': 'SERVICIO','value':'SERVICIO'},
                            {'label': 'SEXO','value':'SEXO'},
                            {'label': 'ESTADO CIVIL','value':'ESTADO CIVIL'},
                            {'label': 'CONDICION VICTIMA','value':'CONDICION VICTIMA'},
                            {'label': 'CLASE ACCIDENTE','value':'CLASE ACCIDENTE'}],
                        value='SEXO',
                        multi=False,
                        clearable=False),
                    html.Div(id='output-container')
            ])
        ]),
        html.Br(),
        html.Div(                                  #se crea otra figura, esta  vez que alberge los diagramas de torta de muertos
            className="map",
            children=[
                html.Div([
                    dcc.Graph(
                        id='death-stats',
                        figure={})
                ])
        ]),
        html.Div(
            className="container",
            children=[                             #este es el dropdown para escoger las estadisticas de heridos
                html.Div([
                    dcc.Dropdown(
                        id='dropdown-hurts',
                        options = [
                            {'label': 'AÑO','value':'AÑO'},
                            {'label': 'SERVICIO','value':'SERVEH1'},
                            {'label': 'SEXO','value':'SEXO'},
                            {'label': 'ESTADO CIVIL','value':'ESTADO CIVIL'},
                            {'label': 'CONDICION VICTIMA','value':'CONDICION VICTIMA'},
                            {'label': 'CLASE ACCIDENTE','value':'CLASE ACCIDENTE'},],
                            value='CLASE ACCIDENTE',
                            multi=False,
                            clearable=False),
                    html.Div(id='output-container2')
            ])
        ]),
        html.Br(),
        html.Div(
            className="map",
            children=[                          #se crea otra figura, esta vez para los graficos de pie de heridos
                html.Div([
                    dcc.Graph(
                        id='hurts-stats',
                        figure={})
                ])
        ]),
        html.Br(),
        html.Div(
            className="container",
            children=[
                html.Div([                         #este ultimo dropdown muestra las opciones de los histogramas
                    dcc.Dropdown(
                        id='dropdown-histogramas',
                        options = [
                            {'label': 'MUERTES DIA','value':'MUERTES DIA'},
                            {'label': 'MUERTES HORA','value':'MUERTES HORA'},
                            {'label': 'MUERTES EDAD','value':'MUERTES EDAD'},
                            {'label': 'HERIDOS EDAD','value':'HERIDOS EDAD'}],
                            value='MUERTES HORA',
                            multi=False,
                            clearable=False),
                    html.Div(id='output-container3')
            ])
        ]),
        html.Br(),
        html.Div(
            className="histogramas",
            children=[                          #y en este grafico se muestra cada histograma
                html.Div([
                    dcc.Graph(
                        id='histogramas',
                        figure={})
                ])
        ]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            className="pkcalc-banner-footer",
            children=[                               # por ultimo en el layout se crea el footer que estara delegado a ser estetica lo mas bajo posible en el layout
                html.Footer(
                    children=[
                        html.H2("Geoportal de accidentalidad en Cali - Universidad del Valle")
                ])
        ]),
])

# viene lo mas importante en el dashboard y son los callbacks
#estos toman los valores de entrdas y salidas y por medio de la funcion que le sigue decide que se va a hacer en ese espacio de layout
@app.callback(
    [Output('output-container3','children'),
    Output('histogramas','figure')],
    Input('dropdown-histogramas','value') #tomo el valor del dropdown de histogramas 
)
def salida(value):

    container4 = "Has seleccionado: {}".format(value)   #creo el label justo debajo del dropdown que muestra que valor fue escodigo

    if value == 'MUERTES DIA':
        fig3 = px.bar(
        hover_name=ejexHistograma,
        y = ejeyHistograma,
        x = ejexHistograma,               #creo el diagrama de barras dependiendo que valor toma 'value'
        height=400,
        color=ejeyHistograma)
    elif value == 'MUERTES HORA':
        fig3 = px.bar(
        hover_name = ejexHoras,
        y = ejeyHoras,
        x = ejexHoras,
        height=400,
        color = ejeyHoras)
    elif value == 'MUERTES EDAD':
        fig3 = px.bar(data_muertos_opt,
        x = 'EDAD',
        height=400,
        color ='EDAD')
    elif value == 'HERIDOS EDAD':
        fig3 = px.bar(data_heridos_opt,
        x = 'EDAD',
        height=400,
        color = 'EDAD'
        )

    fig3.update_layout(xaxis_type='category')

    return container4,fig3

#en este callback recibo 2 entrdas (dos valores) y retorno 3 salidas en la funcion siguiente (container1,container2 y fig1)
@app.callback(
    [Output('output-radio','children'),
    Output('output-radiocapas','children'),
    Output('my-map','figure')],
    [Input('radio-items','value'),
    Input('radio-itemscapas','value')]
)
def update_graph(option_selected,valuecap):
    
    container1 = "Has seleccionado: {}".format(option_selected)
    container2 = "Has seleccionado la cartográfia: {}".format(valuecap)

    if option_selected == "Muertes":
        fig1 = px.scatter_mapbox(data_muertos_opt,
        lat="lat",
        lon="long",
        hover_name="ID",                                               #creo los mapas interactivos en esta funcion con scatter_mapbox
        hover_data=["CONDICION VICTIMA","SEXO","EDAD","AÑO"],
        color="CLASE ACCIDENTE",
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=8,
        height=350)
    elif option_selected == "Heridos":
        fig1 = px.scatter_mapbox(data_heridos_opt,
        lat="lat",
        lon="long",
        hover_name="ID",
        hover_data=["CONDICION VICTIMA","SEXO","EDAD","AÑO"],
        color="CLASE ACCIDENTE",
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=8,
        height=350)

    fig1.update_layout(mapbox_style=valuecap,mapbox_accesstoken=token)
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return container1,container2,fig1


@app.callback(
    [Output('output-container','children'),
    Output('death-stats','figure')],
    Input('dropdown-deaths','value'),
)
def update_output1(value):

    container3 = f'has seleccionado: {value}'

    M = data_muertos_opt                 #creo los diagramas de torta
    fig2 = px.pie(
        title='Datos de Muertos desde el 2007 al 2013 en Cali',
        data_frame = M,
        names = value,
        hole=.3)
    
    return container3,fig2

@app.callback(
    [Output('output-container2','children'),
    Output('hurts-stats','figure')],
    Input('dropdown-hurts','value')
)
def update_output(value):

    container4 = f'has seleccionado: {value}'

    H = data_heridos_opt

    fig3 = px.pie(
        title='Datos de Heridos desde el 2007 al 2014 en Cali',
        data_frame = H,
        names = value,
        hole=.3)
        
    return container4,fig3

#esta ultima parte ejecuta todo el codigo en el servidor y mantiene debugiando(corriendo en el servidor) mientras hago cambios
if __name__ == '__main__':
    app.run_server(debug=True)

#NOTA: siempre que halla un callback debe inmediatamente haber una funcion que ejecute esos valores de entrada(inputs) en eso valores de salidas(outputs)