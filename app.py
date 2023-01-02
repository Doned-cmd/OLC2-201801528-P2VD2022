import pandas as pd
import streamlit as st

# from Algoritmos.RegresionLineal import *
from Algoritmos.RegresionLineal import regresionLineal
from Algoritmos.RegresionPolinomial import RegresionPolinomial
from Algoritmos.Redes import PrediccionNeuronal

st.title('Proyecto 2 - 201801528')
st.title('Algoritmo regresion lineal')

file_regresionlineal = st.file_uploader("Subir archivo", key="1", type=['csv', 'json', 'xlxs'])
data = ""
if file_regresionlineal is not None:
    data = pd.read_csv(file_regresionlineal)
    st.write(data)
    eje_x = st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(data.columns.values), key="2")
    eje_y = st.selectbox(label='Escriba la columna que se tomara como eje y:', options=list(data.columns.values), key="3")
    forecast = st.number_input('Ingrese el valor de x que desea predecir:',  key="4")
    regresionLineal(data, forecast, eje_x, eje_y, st)




st.title('Algoritmo Regresion Polinomial')
file_regresionpoli = st.file_uploader("Subir archivo", key="5", type=['csv', 'json', 'xlxs'])
data2 = ""
if file_regresionpoli is not None:
    data2 = pd.read_csv(file_regresionpoli)
    st.write(data2)
    
    eje_x = st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(data2.columns.values), key="6")
    eje_y = st.selectbox(label='Escriba la columna que se tomara como eje y:', options=list(data2.columns.values), key="7")
    forecast = st.number_input('Ingrese el valor de x que desea predecir:', key="8")
    degree = st.number_input('Ingrese el grado del polinomio', min_value=1, key="9")
    

    rp = RegresionPolinomial(data=data2, forecast=forecast, streamLitInstance=st,
                             eje_x=eje_x, eje_y=eje_y, degree=3)
    rp.execute()


st.title('Prediccion Neuronal')
file_Redneuronal = st.file_uploader("Choose a file",key="10")

data3 = ""
if file_Redneuronal is not None:
    data3 = pd.read_csv(file_Redneuronal)
    st.write(data3)
    eje_x = st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(data2.columns.values), key="6")
    eje_y = st.selectbox(label='Escriba la columna que se tomara como eje y:', options=list(data2.columns.values), key="7")
    forecast = st.number_input('Ingrese el valor de x que desea predecir:',  key="4")
    PrediccionNeuronal(data3, eje_x, eje_y, forecast)