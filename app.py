import pandas as pd
import streamlit as st

# from Algoritmos.RegresionLineal import *
from Algoritmos.RegresionLineal import regresionLineal
from Algoritmos.RegresionPolinomial import RegresionPolinomial
from Algoritmos.Redes import PrediccionNeuronal
from Algoritmos.Redesclas import RedesClas
from Algoritmos.Arbol import Arbol


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
    rp = regresionLineal(data=data, ejexs= eje_x, ejeys= eje_y, name= "Regresion Lineal", prediccionxs=forecast, streamLitInstance=st)
    rp.execute()




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
                             eje_x=eje_x, eje_y=eje_y, degree=degree)
    rp.execute()


st.title('Prediccion Neuronal')
file_Redneuronal = st.file_uploader("Subir documento",key="10")

data3 = ""
if file_Redneuronal is not None:
    data3 = pd.read_csv(file_Redneuronal)
    st.write(data3)
    eje_x = st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(data3.columns.values), key="11")
    eje_y = st.selectbox(label='Escriba la columna que se tomara como eje y:', options=list(data3.columns.values), key="12")
    forecast = st.number_input('Ingrese el valor de x que desea predecir:',  key="13")
    rp = PrediccionNeuronal(data=data3, ejexs=eje_x, ejeys=eje_y, name="Prediccion Neuronal", prediccions=forecast, streamLitInstance=st)
    rp.execute()

dataclasneuronal = ""
st.title('Clasificacion por red Neuronal')
file_clasRedneuronal = st.file_uploader("Subir documento",key="15")
if file_clasRedneuronal is not None:
    dataclasneuronal = pd.read_csv(file_clasRedneuronal)
    st.write(dataclasneuronal)
    Columna = st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(dataclasneuronal.columns.values), key="16")
    Columnas = st.text_input("Escriba el rango de columnas(0-9): ", key="17")
    RedesClas(data=dataclasneuronal, ejexs=Columna, ejeys=Columnas,name="Clasificacion por red Neuronal", streamLitInstance=st).execute()

dataarb = ""  
st.title('Clasificacion por Arbol de Decision')
file_arbol = st.file_uploader("Subir documento",key="20")
if file_arbol is not None:
    dataarb = pd.read_csv(file_arbol)
    st.write(dataarb)
    Columna = st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(dataarb.columns.values), key="21")
    Columnas = st.text_input("Escriba el rango de columnas(0-9): ", key="22")
    
    Arbol(columnas=Columna,ranges=Columnas,data=dataarb,name="Clasificacion por Arbol de Decision",streamLitInstance=st).execute()
    
