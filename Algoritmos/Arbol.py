from Algoritmos.Algorithm import Algorithm
import streamlit
from sklearn import preprocessing
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as mat
from PIL import Image


class Arbol(Algorithm):
    def __init__(self, name, data, streamLitInstance: streamlit, columnas, ranges):
        super().__init__(name, data, streamLitInstance)
        self.columna = columnas
        self.range:str = ranges

    def execute(self):
        array_features = []
        tree = preprocessing.LabelEncoder()
        
        separar = self.range.split("-")
        Iniciosep = int(separar[0])
        Finalsep = int(separar[1])
        
        self.st.write(self.columna)
        pred = np.asarray(self.data[self.columna]).reshape(-1, 1)
        label = tree.fit_transform(pred)
        for i in range(Iniciosep, Finalsep+1):
            temp = self.data.iloc[:, i].values.reshape(-1, 1)
            temporal = tree.fit_transform(temp)
            array_features.append(temporal)

        features = list(zip(*array_features))
        clf = DecisionTreeClassifier().fit(features, label)
        plot_tree(clf, filled=True)
        
        mat.savefig("Arbol_Supervisado.png")
        image = Image.open('Arbol_Supervisado.png')
        self.st.image(image, caption='Sunrise by the mountains')
        mat.clf()