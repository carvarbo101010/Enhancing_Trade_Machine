#ALGORITMO DE VARIACION DE PRECIOS

#Importación de librerías



import pandas as pd
import pandas_datareader as web
import matplotlib as plt
import datetime as dt


#------------------------------------------------

#Utilizamos pandas_datareader para obtener los datos de precios de cierre de cierta acción

ticker = "FB"

start = dt.datetime(2021,12,16)

end =  dt.datetime.now()

data = web.DataReader(ticker, 'yahoo', start, end)

print(data)

#De tabla obtenida de pandas-datareader tomamos de la columna correspondiente cada precio

datos1 = data.iat[0, data.columns.get_loc('Adj Close')]

datos2 = data.iat[1, data.columns.get_loc('Adj Close')]

datos3 = data.iat[2, data.columns.get_loc('Adj Close')]

datos4 = data.iat[3, data.columns.get_loc('Adj Close')]

datos5 = data.iat[4, data.columns.get_loc('Adj Close')]

#Comprobacion de la data extraida de la matriz de precios, fechas, etc, imprimiendo en la termianl la data obtenida

print(datos1)

print(datos2)

print(datos3)

print(datos4)

print(datos5)

#Guardamos cada precio historico obtenido en una tupla


precio = [int(datos1), int(datos2), int(datos3), int(datos4), int(datos5)]


#Calculamos la variación de los ultimos 5 días


variacion_precio = ((precio[4]-precio[0])/(precio[0])) * 100

print(precio)

print("la variacion del precio en 5 periodos es de : ",variacion_precio , "%")

#Si la variación del precio en los ultimos 5 dias representa una caida mayor al 3% en su valor
#damos una señal de que hay un delta en el precio significativo, lo que nos indica que podemos
#hacer una operación larga (de compra).

if variacion_precio < -3.0:

    print("Significant Delta Price!!")

else:

    print("Not a Significant Delta Price.")







