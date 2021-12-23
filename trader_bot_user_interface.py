from tkinter import *
from tkinter import ttk
from tkinter import Entry as entry
import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox


import pandas as pd
import pandas_datareader as web
import matplotlib as plt
import datetime as dt







#------------------------------------ZONA DE SETTINGS INICIALES-----------------------------------------------------#

#Creamos la ventana --- una raíz sino estoy mal

main = Tk()

#Le damos un tamaño específico al GUI

main.geometry("800x500")

#Ingresamos una imagen del proyecto como icono al programa

main.iconbitmap("C:/Users/Financiero/Documents/python3/trading.ico")



#Agregamos un título a la ventana emergente que aparece en la esquina superior izquierda

main.title("Enhancing Trade Machine")

#------------------------------------FIN ZONA DE SETTINGS INICIALES---------------------------------------------------#




#------------------------------------ZONA DE LABELS-------------------------------------------------------------------#

label0 = Label(main, text = "Trade Ticker: ")
label0.grid(row = 2, column = 0, sticky = W, pady = 2)

label1 = Label(main, text = "Trailing SL and TP ", font='Helvetica 14 bold')
label1.grid(row = 1, column = 0, sticky = W, pady = 2, columnspan= 2)

label2 = Label(main, text = "Trade Ticker: ")
label2.grid(row = 4, column = 0, sticky = W, pady = 2)

label3 = Label(main, text = "Volatility Detector " , font='Helvetica 14 bold')
label3.grid(row = 3, column = 0, sticky = W, pady = 2)



#------------------------------------FIN ZONA DE LABELS---------------------------------------------------------------#

#------------------------------------ZONA DE ENTRYS-------------------------------------------------------------------#


entry0 = entry(main)
entry0.insert(END,"FB")
entry0.grid(row = 2, column =1, pady = 2, sticky = S)

entry1 = entry(main)
entry1.insert(END,"FB")
entry1.grid(row = 4, column =1, pady = 2, sticky = S)


#------------------------------------FIN ZONA DE ENTRYS----------------------------------------------------------------#

#------------------------------------ZONA DE DESARROLLO DETECTOR DE VOLATILIDAD----------------------------------------#

#Utilizamos pandas_datareader para obtener los datos de precios de cierre de cierta acción

anchor_date_2 = dt.datetime.now() - dt.timedelta(days= 6)

def vol_detector():

    ticker = entry1.get()

    start = anchor_date_2

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

        messagebox.showinfo(message="Señal de entrada posicion larga", title="Título")


    else:

        print("Not a Significant Delta Price.")



#------------------------------------FIN ZONA DE DESARROLLO DETECTOR DE VOLATILIDAD------------------------------------#

#------------------------------------ZONA DE DESARROLLO TRAIL SL, TP---------------------------------------------------#

anchor_date = dt.datetime.now() - dt.timedelta(days= 2)

#Clase que permite actualizar la fecha para el cálculo de las ganancias o perdidas

class Update_datetime:


    def __init__(self, init_date):

        self.init_date = init_date

    def change_date(self):
        
        if dt.datetime.now() > self.init_date:


            return self.init_date + dt.timedelta(days = 1)

    

def dates():

    Fecha = Update_datetime(anchor_date)

    print(Fecha.init_date)

    Object_2 = Fecha.change_date()

    print(Object_2)

    
    




           
#Modulo de alimentación de la variable GAIN_OR_LOSS:




    ticker = entry0.get()
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

    #Si la Función RelU nos muestra 0, es decir una señal de bajada en el precio de los ultimos dos días, acortamos el TP para salir de la posición
    #ganando

    if Object1 == 0:

        messagebox.showinfo(message="Señal de Recorte del TP", title="Título")



#------------------------------------FIN ZONA DE DESARROLLO SL, TP------------------------------------------------------#

#------------------------------------ZONA DE BOTONES-------------------------------------------------------------------#

boton0 = ttk.Button(text="Submitt", command= dates)
boton0.grid(row = 3, column = 2, pady = 2)

boton1 = ttk.Button(text="Submitt", command= vol_detector)
boton1.grid(row = 5, column = 2, pady = 2)


#------------------------------------FIN ZONA DE BOTONES---------------------------------------------------------------#



main.mainloop()