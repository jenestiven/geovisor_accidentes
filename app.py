
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output,State
from texto import mensaje 
import dash_bootstrap_components as dbc
from funciones import salida,update_graph,update_output1,update_output
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
app.title = 'Geovisor Accidentalidad' 
app._favicon = 'logo.png'

app.layout = html.Div(
    children=[

        html.Div(  
            className="header", 
            children=[
                html.A(
                    id = "geo-logo",
                    children=[html.Img(src="assets\logo.png")] 
                ),
                html.A(
                    id = "derecha-logo",
                    href = "https://www.univalle.edu.co/",
                    children=[html.Img(src="assets\logoUV_Oficial_Rojo.jpg")]
                ),
                html.H2("Geovisor de accidentalidad en Cali")  
        ]),
        html.Div(
            className="mapbox",
            children=[
                html.Div([
                    dcc.Graph(             
                        id='my-map',
                        figure={})
                ])
        ]),
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
        html.Div(
            className="infobox",
            children=[
                dbc.Button(
                    id = 'info',
                    n_clicks=0,
                    style={'height':'30px','width':'30px'},
                    children=[html.Img(src="assets\info.png")]
                    ),
                dbc.Offcanvas(
                    html.P(mensaje),
                    id = 'offcanvas',
                    scrollable=True,
                    title = 'Problematica',
                    is_open = False,
                    placement='end'
                )
        ]),
        html.Div(
            className='statisticsbox',
            children = [
                html.Div(
                    className='deathsbox',
                    children=[
                        html.Div(                            
                            className="deaths-pie",
                            children=[
                                html.Div([
                                    dcc.Graph(
                                        id='death-stats',
                                        figure={})
                                ])
                        ]),
                        html.Div(
                            className='label-m',
                            children=[
                                html.P('Datos de Muertos en los años 2007 al 2013')
                        ]),
                ]),
                html.Div(
                    className='hurtsbox',
                    children=[
                        html.Div(
                            className="hurts-pie",
                            children=[                         
                                html.Div([
                                    dcc.Graph(
                                        id='hurts-stats',
                                        figure={})
                                ])
                        ]),
                        html.Div(
                            className='label-h',
                            children=[
                                html.P('Datos de Heridos en los años 2007 al 2014')
                        ]),
                ]),
                html.Div(
                    className='histogrambox',
                    children=[
                        html.Div(
                            className="histogramas",
                            children=[                 
                                html.Div([
                                    dcc.Graph(
                                        id='histogramas',
                                        figure={},
                                        style={'height':'410px'})
                                ])
                        ]),
                ])
        ]),
        html.Div(
            className='labeldeaths',
            children=[
                html.P('Seleccione la estadistica de Muertes:',id='p1')
        ]),
        html.Div(
            className='labelhurts',
            children=[
                html.P('Seleccione la estadistica de Heridos:', id = 'p2')
        ]),
        html.Div(
            className='labelhistogram',
            children=[
                html.P('Seleccione las estadisticas que desea ver: ', id = 'p3')
        ]),
        html.Div(
            className="dropdown-d",
            children=[
                html.Div([                  
                    dcc.Dropdown(
                        id='dropdown-deaths',
                        options = [
                            {'label': 'AÑO','value':'AÑO'},
                            {'label': 'SERVICIO','value':'SERVICIO'},
                            {'label': 'SEXO','value':'SEXO'},
                            {'label': 'ESTADO CIVIL','value':'ESTADO CIVIL'},
                            {'label': 'CONDICION VICTIMA','value':'CONDICION VICTIMA'}],
                        value='SEXO',
                        multi=False,
                        clearable=False),
                    html.Div(id='output-container')
            ])
        ]),
        html.Div(
            className="dropdown-h",
            children=[                 
                html.Div([
                    dcc.Dropdown(
                        id='dropdown-hurts',
                        options = [
                            {'label': 'AÑO','value':'AÑO'},
                            {'label': 'SERVICIO','value':'SERVICIO'},
                            {'label': 'SEXO','value':'SEXO'},
                            {'label': 'ESTADO CIVIL','value':'ESTADO CIVIL'},
                            {'label': 'CONDICION VICTIMA','value':'CONDICION VICTIMA'}],
                            value='CONDICION VICTIMA',
                            multi=False,
                            clearable=False),
                    html.Div(id='output-container2')
            ])
        ]),
        html.Div(
            className="dropdown-his",
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
        html.Div(
            className="footer",
            children=[                               
                html.Footer(
                    children=[
                        html.A(
                            id = "github",
                            href = "https://github.com/jenestiven/geovisor_accidentes",
                            children=[html.Img(src="assets\github.png")]),
                        html.A(
                            id = "facebook",
                            href="https://www.facebook.com/jhonStevenGA",
                            children=[html.Img(src="assets\_facebook.png")]),
                        html.A(
                            id = "twiter",
                            href = "https://twitter.com/Steven38156",
                            children=[html.Img(src="assets\_twiter.png")]),
                        html.H2("Geoportal de accidentalidad en Cali - Universidad del Valle"),
                        html.H3("By @jhonpyDev")
                ])
        ])
]) 

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
    Output("offcanvas", "is_open"),
    Input("info", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open
    
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
    
if __name__ == '__main__':
    app.run_server(debug=True)

