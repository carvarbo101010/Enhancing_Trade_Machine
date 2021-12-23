#Librerias importadas

import pandas as pd
import pandas_datareader as web
import matplotlib as plt
import datetime as dt


#Clase que permite actualizar la fecha para el cálculo de las ganancias o perdidas

anchor_date = dt.datetime.now() - dt.timedelta(days= 2)

class Update_datetime:


    def __init__(self, init_date):

        self.init_date = init_date

    def change_date(self):
    
       if dt.datetime.now() > self.init_date:


           return self.init_date + dt.timedelta(days = 1)


Fecha = Update_datetime(anchor_date)

print(Fecha.init_date)

Object_2 = Fecha.change_date()

print(Object_2)


           
#Modulo de alimentación de la variable GAIN_OR_LOSS:




ticker = 'GOOGL'
start = Object_2
end =  dt.datetime.now()

data = web.DataReader(ticker, 'yahoo', start, end)

#Comprobacion de la data descargada desde Yahoo, imprimiendo en la terminal la data obtenida

print(data)



datos1 = data.iat[1, data.columns.get_loc('Adj Close')]

datos2 = data.iat[0, data.columns.get_loc('Adj Close')]

#Comprobacion de la data extraida de la matriz de precios, fechas, etc, imprimiendo en la termianl la data obtenida

print(datos1 - datos2)




#Variable que alimenta la función RelU

GAIN_OR_LOSS = int(datos1 - datos2)




#Clase Activation_RelU que permite convertir los resultados positivos en su equivalente y los resultados negativos en 0



def forward_RelU(input):

        
        if input > 0:
            return input
        else:
            return 0

Object1 = forward_RelU(GAIN_OR_LOSS)

#Comprobacion de el funcionamiento e la función Relu

print(Object1)


