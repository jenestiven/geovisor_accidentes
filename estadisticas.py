
import pandas as pd


sexo_e= pd.read_excel('data\sexoJH.xlsx') 
sexo_e['HORA'] = sexo_e['HORA'].fillna(0) 
sex_e= pd.read_excel('data\sexoh.xlsx') 


mP = [[],[],[],[]]
for i in range(len(sexo_e['SEXO'])):
    sexo = int(sexo_e.loc[i][0])
    mP[0].append(sexo)
    año = int(sexo_e.loc[i][1])
    mP[1].append(año)
    dia = int(sexo_e.loc[i][2])
    mP[2].append(dia)
    hora = int(sexo_e.loc[i][3])
    mP[3].append(hora)


mP_2 = [[],[]]
for i in range(len(sex_e['SEXO'])):
    sexo = int(sex_e.loc[i][0])
    mP_2[0].append(sexo)
    año = int(sex_e.loc[i][1])
    mP_2[1].append(año)

#Muertos
ejeysexo = [mP[0].count(1), mP[0].count(0)]
ejexsexo = ["MASCULINO","FEMENINO"]
d_sexo = {'Cantidad':ejeysexo,'Sexo':ejexsexo}
dfSexo = pd.DataFrame(d_sexo)
#dfSexo.to_csv('Sexo_muertos',index=False)

ejeyaño = [mP[1].count(2007), mP[1].count(2008), mP[1].count(2009), mP[1].count(2010), mP[1].count(2011),
mP[1].count(2012),mP[1].count(2013)]
ejexaño = ["2007","2008","2009","2010","2011","2012","2013"]
d_año = {'Cantidad':ejeyaño,'Años':ejexaño}
dfAño = pd.DataFrame(d_año)
#dfAño.to_csv('Años_muertos',index=False)

ejeyHistograma = [mP[2].count(1), mP[2].count(2), mP[2].count(3), mP[2].count(4), mP[2].count(5), mP[2].count(6), mP[2].count(7)]
ejexHistograma= ["LUN","MAR","MIER","JUE","VIE","SAB","DOM"]
d_dias = {'Cantidad':ejeyHistograma,'Dias':ejexHistograma}
dfDias = pd.DataFrame(d_dias)
#dfDias.to_csv('Dias_muertos',index=False)

ejeyHoras = [mP[3].count(1), mP[3].count(2), mP[3].count(3), mP[3].count(4), mP[3].count(5),
mP[3].count(6), mP[3].count(7), mP[3].count(8), mP[3].count(9), mP[3].count(10), mP[3].count(11),
mP[3].count(12), mP[3].count(13), mP[3].count(14), mP[3].count(15), mP[3].count(16), mP[3].count(17),
mP[3].count(18), mP[3].count(19), mP[3].count(20), mP[3].count(21), mP[3].count(22), mP[3].count(23)]
ejexHoras = ["1 am ","2 am ","3 am ","4 am ","5 am ","6 am ","7 am ","8 am ","9 am ","10 am ","11 am ","12 pm","1 pm",
"2 pm","3 pm","4 pm","5 pm","6 pm","7 pm","8 pm","9 pm","10 pm","11 pm"]
d_horas = {'Cantidad':ejeyHoras,'Horas':ejexHoras}
dfHoras = pd.DataFrame(d_horas)
#dfHoras.to_csv('Horas_muertos',index=False)

#Heridos
ysexo = [mP_2[0].count(1),mP_2[0].count(0)]
xsexo = ["FEMENINO","MASCULINO"]
h_sexo = {'Cantidad':ysexo,'Sexo':xsexo}
dfhSexo = pd.DataFrame(h_sexo)
#dfhSexo.to_csv('Sexo_heridos',index=False)

yaño = [mP_2[1].count(2007), mP_2[1].count(2008), mP_2[1].count(2009), mP_2[1].count(2010), mP_2[1].count(2011),
mP_2[1].count(2012),mP_2[1].count(2013),mP_2[1].count(2014)]
xaño = ["2007","2008","2009","2010","2011","2012","2013","2014"]
h_año = {'Cantidad':yaño,'Años':xaño}
dfhAño = pd.DataFrame(h_año)
#dfhAño.to_csv('Años_heridos',index=False)
