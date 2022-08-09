
import pandas as pd
import csv
from csv import reader
from statistics import mean 

import matplotlib.pyplot as plt

Muertos= pd.read_excel('data\heridosJH.xlsx')
sexo= pd.read_excel('data\sexoJH.xlsx') 
#dia = pd.read_excel('DIAS.xlsx')
i=0 
sumaf = 0
sumam = 0
sumaf2007 = 0 
sumam2007 = 0
sumaf2008 = 0
sumam2008 = 0
sumaf2009 = 0 
sumam2009 = 0
sumaf2010 = 0
sumam2010 = 0
sumaf2011 = 0 
sumam2011 = 0
sumaf2012 = 0
sumam2012 = 0
sumaf2013 = 0 
sumam2013 = 0
LUN = 0
MAR = 0
MIE = 0
JUE = 0
VIE = 0
SAB = 0
DOM = 0


h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
h7 = 0
h8 = 0
h9 = 0
h10 = 0
h11 = 0
h12 = 0
h13 = 0
h14 = 0
h15 = 0
h16 = 0
h17 = 0
h18 = 0
h19 = 0
h20 = 0
h21 = 0
h22 = 0
h23 = 0
h24 = 0



yG=[]
y07=[]
y08=[]
y09=[]
y10=[]
y11=[]
y12=[]
y13=[]


while i<len(sexo):
  sexo1  = sexo.loc[i][0]
  año=sexo.loc[i][1]
  dia1=sexo.loc[i][2]
  hora =sexo.loc[i][3]

  if sexo1 == 1:
    
    sumaf += 1

  if sexo1 == 0:

    sumam += 1


  if sexo1 == 1 and año ==2007:

    sumaf2007 += 1

  if sexo1 == 0 and año ==2007:

    sumam2007 += 1


  if sexo1 == 1 and año ==2008:

    sumaf2008 += 1    

  if sexo1 == 0 and año ==2008:

    sumam2008 += 1


  if sexo1 == 1 and año ==2009:

    sumaf2009 += 1

  if sexo1 == 0 and año ==2009:

    sumam2009 += 1



  if sexo1 == 1 and año ==2010:

    sumaf2010 += 1

  if sexo1 == 0 and año ==2010:

    sumam2010 += 1



  if sexo1 == 1 and año ==2011:

    sumaf2011 += 1    

  if sexo1 == 0 and año ==2011:

    sumam2011 += 1



  if sexo1 == 1 and año ==2012:

    sumaf2012 += 1
    
  if sexo1 == 0 and año ==2012:

    sumam2012 += 1


  if sexo1 == 1 and año ==2013:

    sumaf2013 += 1

  if sexo1 == 0 and año ==2013:

    sumam2013 += 1

  if dia1 == 1:
    LUN += 1

  if dia1 == 2:
    MAR += 1

  if dia1 == 3:
    MIE += 1

  if dia1 == 4:
    JUE += 1

  if dia1 == 5:
    VIE += 1

  if dia1 == 6:
    SAB += 1    

  if dia1 == 7:
    DOM += 1   



  if hora == 1:
    h1 += 1

  if hora  == 2:
    h2  += 1

  if hora  == 3:
    h3 += 1

  if hora  == 4:
    h4  += 1

  if hora  == 5:
    h5 += 1

  if hora == 6:
    h6 += 1    

  if hora  == 7:
    h7  += 1  

  if hora == 8:
    h8  += 1

  if hora  == 9:
    h9  += 1

  if hora  == 10:
    h10 += 1

  if hora  == 11:
    h11  += 1

  if hora  == 12:
    h12 += 1

  if hora == 13:
    h13 += 1    

  if hora  == 14:
    h14   += 1          

  if hora == 15:
    h15 += 1

  if hora  == 16:
    h16  += 1

  if hora  == 17:
    h17 += 1

  if hora  == 18:
    h18  += 1

  if hora  == 19:
    h19 += 1

  if hora == 20:
    h20 += 1    

  if hora  == 21:
    h21  += 1 

  if hora == 22:
    h22  += 1

  if hora  == 23:
    h23  += 1

  if hora  == 0:
    h24 += 1

  i +=1


LIST = [LUN,MAR,MIE,JUE,VIE,SAB,DOM] #reemplazar esta lista por ejeyHostograma
#esta lista guarda los valores de las muertes que hubieron cada dia de la semana 


'''

etiquetas=("FEMENINO", "MASCULINO")
colores= ("blue", "pink")
yG = [sumaf,sumam]
pie = plt.pie(yG, labels= etiquetas, colors= colores, autopct='%1.2f%%' )
plt.title("Muertes entre 2007-2013")
y07 = [sumaf2007,sumam2007]
plt.pie(y07, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2007")

y08 = [sumaf2008,sumam2008]
plt.pie(y08, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2008")

y09 = [sumaf2009,sumam2009]
plt.pie(y09, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2009")

y10 = [sumaf2010,sumam2010]
plt.pie(y10, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2010")

y11 = [sumaf2011,sumam2011]
plt.pie(y11, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2011")

y12 = [sumaf2012,sumam2012]
plt.pie(y12, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2012")

y13 = [sumaf2013,sumam2013]
plt.pie(y13, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Muertes 2013")




x = Muertos['EDAD']
histograma_M_e = plt.hist(abs(x), bins=range(0,100,5), density=True,linewidth=0.5, edgecolor="white")
plt.title("Histograma-Muertes por edad")
plt.xlabel('Edades')
plt.ylabel('Frecuencia')


histograma_M_d = plt.bar(ejex,ejey)
plt.title("Muertes generadas por accidentes de transito por dias  ")
plt.xlabel('DIA DE LA SEMANA')
plt.ylabel('NUMERO DE MUERTES')

'''

ejex1= ["1 am ","2 am ","3 am ","4 am ","5 am ","6 am ","7 am ","8 am ","9 am ","10 am ","11 am ","12 pm","1 pm",
"2 pm","3 pm","4 pm","5 pm","6 pm","7 pm","8 pm","9 pm","10 pm","11 pm"]
ejey1= [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23]

'''
print(ejey1)
histograma_M_h = plt.bar(ejex1,ejey1)
plt.title("Muertes generadas por accidentes de transito por hora ")
plt.xlabel('HORA')
plt.ylabel('NUMERO DE MUERTES')

Prom = mean(abs(x))
print("La edad media de muertes es : ", int(Prom))

'''

#---------------------------heridos------------------------------------------------

Heridos= pd.read_excel('data\heridosJH.xlsx')
sexo= pd.read_excel('data\sexohJH.xlsx')
i=0 
sumaf = 0
sumam = 0
sumaf2007 = 0 
sumam2007 = 0
sumaf2008 = 0
sumam2008 = 0
sumaf2009 = 0 
sumam2009 = 0
sumaf2010 = 0
sumam2010 = 0
sumaf2011 = 0 
sumam2011 = 0
sumaf2012 = 0
sumam2012 = 0
sumaf2013 = 0 
sumam2013 = 0

yG=[]
y07=[]
y08=[]
y09=[]
y10=[]
y11=[]
y12=[]
y13=[]


while i<len(sexo):
  sexo1  = sexo.loc[i][0]
  año = sexo.loc[i][1]

  if sexo1 == 1:
    
    sumaf += 1

  if sexo1 == 0:

    sumam += 1




  if sexo1 == 1 and año ==2007:

    sumaf2007 += 1

  if sexo1 == 0 and año ==2007:

    sumam2007 += 1


  if sexo1 == 1 and año ==2008:

    sumaf2008 += 1    

  if sexo1 == 0 and año ==2008:

    sumam2008 += 1


  if sexo1 == 1 and año ==2009:

    sumaf2009 += 1

  if sexo1 == 0 and año ==2009:

    sumam2009 += 1



  if sexo1 == 1 and año ==2010:

    sumaf2010 += 1

  if sexo1 == 0 and año ==2010:

    sumam2010 += 1



  if sexo1 == 1 and año ==2011:

    sumaf2011 += 1    

  if sexo1 == 0 and año ==2011:

    sumam2011 += 1



  if sexo1 == 1 and año ==2012:

    sumaf2012 += 1
    
  if sexo1 == 0 and año ==2012:

    sumam2012 += 1


  if sexo1 == 1 and año ==2013:

    sumaf2013 += 1

  if sexo1 == 0 and año ==2013:

    sumam2013 += 1

  i +=1




'''
etiquetas=("FEMENINO", "MASCULINO")
colores= ("blue", "pink")
yG1 = [sumaf,sumam]
plt.pie(yG, labels= etiquetas, colors= colores, autopct='%1.2f%%' )
plt.title("Heridos entre 2007-2013")

y071 = [sumaf2007,sumam2007]
plt.pie(y07, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2007")

y081 = [sumaf2008,sumam2008]
plt.pie(y08, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2008")

y091 = [sumaf2009,sumam2009]
plt.pie(y09, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2009")

y101 = [sumaf2010,sumam2010]
plt.pie(y10, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2010")

y111 = [sumaf2011,sumam2011]
plt.pie(y11, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2011")

y121 = [sumaf2012,sumam2012]
plt.pie(y12, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2012")

y131 = [sumaf2013,sumam2013]
plt.pie(y13, labels= etiquetas, colors= colores, autopct='%1.2f%%')
plt.title("Heridos 2013")


x = Heridos['EDAD']
histograma_H_d = plt.hist(abs(x), bins=range(0,100,5), density=True,linewidth=0.5, edgecolor="white")
plt.title("Histograma-Heridos por edad")
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

Prom = mean(abs(x))
print("La edad media de Heridos es : ", int(Prom))

'''