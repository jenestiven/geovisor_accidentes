
import plotly.express as px
from data import data_heridos_opt,data_muertos_opt,años_heridos,años_muertos,sexo_heridos,sexo_muertos,dias_muertos,horas_muertos



token = 'pk.eyJ1IjoiamVuZXN0aXZlbiIsImEiOiJjbDZpOGo0OGgxNTg2M2RrZXh2endtaTNxIn0._4TgQS_XY2QaJpix0HhtpA'

def salida(value):
    container4 = "_Has seleccionado: {}".format(value)   

    if value == 'MUERTES DIA':
        fig3 = px.bar(
            dias_muertos,
            title='Muertes por dia entre los años 2007-2013',
            hover_name='Dias',
            y = 'Cantidad',
            x = 'Dias',             
            color='Cantidad',
            labels={'Dias':'Dias de la semana'},
            height=410)
    elif value == 'MUERTES HORA':
        fig3 = px.bar(
            horas_muertos,
            title='Muertes por hora entre los años 2007-2013',
            hover_name = 'Horas',
            y = 'Cantidad',
            x = 'Horas',
            color = 'Cantidad',
            height=410)
    elif value == 'MUERTES SEXO':
        fig3 = px.bar(
            sexo_muertos,
            title='Muertes por sexo entre los años 2007-2013',
            hover_name = 'Sexo',
            y = 'Cantidad',
            x = 'Sexo',
            color = 'Sexo',
            labels={'Sexo':'Genero'},
            height=410)
    elif value == 'MUERTES AÑO':
        fig3 = px.bar(
            años_muertos,
            title='Muertes por año entre los años 2007-2013',
            hover_name = 'Años',
            y = 'Cantidad',
            x = 'Años',
            color = 'Cantidad',
            height=410)
    elif value == 'MUERTES EDAD':
        fig3 = px.histogram(
            data_muertos_opt,
            title='Muertes por edad entre los años 2007-2013',
            x = 'EDAD',
            height=410,
            color ='EDAD')
    elif value == 'HERIDOS EDAD':
        fig3 = px.histogram(
            data_heridos_opt,
            title='Heridos por edad entre los años 2007-2014',
            x = 'EDAD',
            height=410,
            color ='EDAD')
    elif value == 'HERIDOS SEXO':
        fig3 = px.bar(
            sexo_heridos,
            hover_name = 'Sexo',
            title='Heridos por sexo entre los años 2007-2014',
            y = 'Cantidad',
            x = 'Sexo',
            height=410,
            labels={'Sexo':'Genero'},
            color = 'Sexo')
    elif value == 'HERIDOS AÑO':
        fig3 = px.bar(
            años_heridos,
            hover_name = 'Años',
            title='Heridos por año entre los años 2007-2014',
            y = 'Cantidad',
            x = 'Años',
            height=410,
            color = 'Cantidad')

    fig3.update_layout(xaxis_type='category')

    return container4,fig3


def update_graph(option_selected,valuecap):
    container1 = "_Has seleccionado: {}".format(option_selected)
    container2 = "_Has seleccionado la cartográfia: {}".format(valuecap)

    if option_selected == "Muertes":
        fig1 = px.scatter_mapbox(
            data_muertos_opt,
            lat="lat",
            lon="long",
            hover_name="ID",                                             
            hover_data=["CONDICION VICTIMA","SEXO","EDAD","AÑO"],
            color="CLASE ACCIDENTE",
            labels={'CLASE ACCIDENTE':'CLASE DE ACCIDENTE'},
            size= 'AÑO',
            center={"lat": 3.43722, "lon": -76.5225},
            zoom=10,
            height=493)
    elif option_selected == "Heridos":
        fig1 = px.scatter_mapbox(
            data_heridos_opt,
            lat="lat",
            lon="long",
            hover_name="ID",
            hover_data=["CONDICION VICTIMA","SEXO","EDAD","AÑO"],
            color="CLASE ACCIDENTE",
            labels={'CLASE ACCIDENTE':'CLASE DE ACCIDENTE'},
            size= 'EDAD',
            center={"lat": 3.43722, "lon": -76.5225},
            zoom=10,
            height=493)

    fig1.update_layout(mapbox_style=valuecap,mapbox_accesstoken=token)
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return container1,container2,fig1


def update_output1(value):
    container3 = f'_Has seleccionado: {value}'
               
    fig2 = px.pie(
        data_frame = data_muertos_opt,
        names = value,
        height=410,
        hole=.5)
    
    return container3,fig2


def update_output(value):
    container4 = f'_Has seleccionado: {value}'

    fig3 = px.pie(
        data_frame = data_heridos_opt,
        names = value,
        height=410,
        hole=.5)
        
    return container4,fig3

