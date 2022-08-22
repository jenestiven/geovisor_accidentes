
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output
from texto import mensaje 
from funciones import salida,update_graph,update_output1,update_output
from dash.exceptions import PreventUpdate



app = dash.Dash(__name__)
app.title = 'Geovisor Accidentalidad' 

app.layout = html.Div(
    style={'background':'#F8F8FF'}, 
    children=[

        html.Div(  
            className="pkcalc-banner", 
            children=[
                html.A(
                    id = "geo-logo",
                    children=[html.Img(src="assets\globo.png")] 
                ),
                html.H2("Geovisor de accidentalidad en Cali")  
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
            className="p",     
            children=[
                html.P(
                    mensaje
                )
        ]),
        html.Br(),
        html.Br(), 
        html.Br(),
        html.Br(),
        html.Div(
            className="container-radio",
            children=[
                html.Div([
                    dcc.RadioItems(            
                        id='radio-items',          
                        options=['Muertes','Heridos'],
                        value='Muertes', 
                        inline=True),
                    html.Div(id='output-radio')
                ])
            ]),
            html.Br(),
            html.Div(
            className="container-radio",
            children=[                
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
                    dcc.Graph(             
                        id='my-map',
                        figure={})
                ])
        ]),
        html.Div(
            className="container",
            children=[
                html.Div([                  
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
        html.Div(                            
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
            children=[                 
                html.Div([
                    dcc.Dropdown(
                        id='dropdown-hurts',
                        options = [
                            {'label': 'AÑO','value':'AÑO'},
                            {'label': 'SERVICIO','value':'SERVICIO'},
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
            children=[                         
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
                html.Div([                  
                    dcc.Dropdown(
                        id='dropdown-histogramas',
                        options = [
                            {'label': 'MUERTES DIA','value':'MUERTES DIA'},
                            {'label': 'MUERTES HORA','value':'MUERTES HORA'},
                            {'label': 'MUERTES AÑO','value':'MUERTES AÑO'},
                            {'label': 'MUERTES SEXO','value':'MUERTES SEXO'},
                            {'label': 'MUERTES EDAD','value':'MUERTES EDAD'},
                            {'label': 'HERIDOS EDAD','value':'HERIDOS EDAD'},
                            {'label': 'HERIDOS SEXO','value':'HERIDOS SEXO'},
                            {'label': 'HERIDOS AÑO','value':'HERIDOS AÑO'}],
                            value='MUERTES HORA',
                            multi=False,
                            clearable=False),
                    html.Div(id='output-container3')
            ])
        ]),
        html.Br(),
        html.Div(
            className="histogramas",
            children=[                 
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
            children=[                               
                html.Footer(
                    children=[
                        html.H2("Geoportal de accidentalidad en Cali - Universidad del Valle")
                ])
        ]),
])

@app.callback(
    [Output('output-container3','children'),
    Output('histogramas','figure')],
    Input('dropdown-histogramas','value') 
)
def c_salida(value):
    if value is None:
        raise PreventUpdate
    else:
        return salida(value)

@app.callback(
    [Output('output-radio','children'),
    Output('output-radiocapas','children'),
    Output('my-map','figure')],
    [Input('radio-items','value'),
    Input('radio-itemscapas','value')]
)
def c_update_graph(option_selected,valuecap):
    if option_selected and valuecap is None:
        raise PreventUpdate
    else:
        return update_graph(option_selected,valuecap)
         
@app.callback(
    [Output('output-container','children'),
    Output('death-stats','figure')],
    Input('dropdown-deaths','value'),
)
def c_update_output1(value):
    if value is None:
        raise PreventUpdate
    else:
        return update_output1(value)
    
@app.callback(
    [Output('output-container2','children'),
    Output('hurts-stats','figure')],
    Input('dropdown-hurts','value')
)
def c_update_output(value):
    if value is None:
        raise PreventUpdate
    else:
        return update_output(value)

if __name__ == '__main__':
    app.run_server(debug=True)
    