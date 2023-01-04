from Algoritmos.Algorithm import Algorithm
import streamlit 
import numpy as np
import re
from sklearn.naive_bayes import GaussianNB

class Gauss(Algorithm):
    def __init__(self, name, data, streamLitInstance: streamlit, ):
        super().__init__(name, data, streamLitInstance)
        
    def execute(self):    
        select_valxlist = self.st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(self.data.columns.values), key="50")
        select_valylist = self.st.selectbox(label='Escriba la columna que se tomara como eje x: ', options=list(self.data.columns.values), key="51")

        x = np.asarray(self.data[select_valxlist])#.reshape(-1, 1)
        y = np.asarray(self.data[select_valylist])
        self.st.write("Valores X")
        self.st.write(x)
        self.st.write("Valores Y")
        self.st.write(y)

        self.st.sidebar.subheader("Valores de Interes")
        vals = self.st.sidebar.text_input("Los valores se separan por coma")
        List_Val = lambda x : [int(i) for i in re.split(",",x) if i!=""]

        arraylist = List_Val(vals)
        valInit= list(map(float,arraylist))
    
        clf = GaussianNB()
    # Adaptación de datos
        clf.fit(x,y)
        self.st.write("Prediccion:")
        self.st.write(clf.predict([valInit]))
  