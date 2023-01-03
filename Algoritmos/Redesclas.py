from Algoritmos.Algorithm import Algorithm
import numpy as np
import streamlit 
from sklearn.preprocessing import StandardScaler


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier

from PIL import Image
import pydot
from pathlib import Path

class RedesClas(Algorithm):
    
    def __init__(self, name, data, streamLitInstance: streamlit,  ejexs, ejeys):
        super().__init__(name, data, streamLitInstance)
        self.ejex = ejexs
        self.ejey = ejeys
        
    def execute(self):
        
        xnoslash = self.ejex.replace("\"", "")
        xnocom = xnoslash.split(",")
        tamano = len(xnocom)
        X = self.data[[]]
        
        self.st.write(xnocom)
        
        encoder = LabelEncoder()
        if tamano == 1:
            xnocom[0] = xnocom[0].replace(" ", "")
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            X = self.data[[str(xnocom[0])]]
        elif tamano == 2:
            xnocom[0] = xnocom[0].replace(" ", "")            
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1])]]
        elif tamano == 3:
            xnocom[0] = xnocom[0].replace(" ", "")
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            xnocom[2] = xnocom[2].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[2]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1]), str(xnocom[2])]]
        elif tamano == 4:
            xnocom[0] = xnocom[0].replace(" ", "")   
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            xnocom[2] = xnocom[2].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[2]].values)
            xnocom[3] = xnocom[3].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[3]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1]), str(xnocom[2]), str(xnocom[3])]]
        elif tamano == 5:
            xnocom[0] = xnocom[0].replace(" ", "") 
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            xnocom[2] = xnocom[2].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[2]].values)
            xnocom[3] = xnocom[3].replace(" ", "")
            self.data[str(xnocom[3])] = encoder.fit_transform(self.data[xnocom[3]].values)
            xnocom[4] = xnocom[4].replace(" ", "")
            self.data[str(xnocom[4])] = encoder.fit_transform(self.data[xnocom[4]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1]),str(xnocom[2]), str(xnocom[3]), str(xnocom[4])]]
        elif tamano == 6:
            xnocom[0] = xnocom[0].replace(" ", "")
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            xnocom[2] = xnocom[2].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[2]].values)
            xnocom[3] = xnocom[3].replace(" ", "")
            self.data[str(xnocom[3])] = encoder.fit_transform(self.data[xnocom[3]].values)
            xnocom[4] = xnocom[4].replace(" ", "")
            self.data[str(xnocom[4])] = encoder.fit_transform(self.data[xnocom[4]].values)
            xnocom[5] = xnocom[5].replace(" ", "")
            self.data[str(xnocom[5])] = encoder.fit_transform(self.data[xnocom[5]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1]), str(xnocom[2]),str(xnocom[3]), str(xnocom[4]), str(xnocom[5])]]
        elif tamano == 7:
            xnocom[0] = xnocom[0].replace(" ", "")
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            xnocom[2] = xnocom[2].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[2]].values)
            xnocom[3] = xnocom[3].replace(" ", "")
            self.data[str(xnocom[3])] = encoder.fit_transform(self.data[xnocom[3]].values)
            xnocom[4] = xnocom[4].replace(" ", "")
            self.data[str(xnocom[4])] = encoder.fit_transform(self.data[xnocom[4]].values)
            xnocom[5] = xnocom[5].replace(" ", "")
            self.data[str(xnocom[5])] = encoder.fit_transform(self.data[xnocom[5]].values)
            xnocom[6] = xnocom[6].replace(" ", "")
            self.data[str(xnocom[6])] = encoder.fit_transform(self.data[xnocom[6]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1]), str(xnocom[2]),str(xnocom[3]), str(xnocom[4]), str(xnocom[5]), str(xnocom[6])]]
        elif tamano == 8:
            xnocom[0] = xnocom[0].replace(" ", "") 
            self.data[str(xnocom[0])] = encoder.fit_transform(self.data[xnocom[0]].values)
            xnocom[1] = xnocom[1].replace(" ", "")
            self.data[str(xnocom[1])] = encoder.fit_transform(self.data[xnocom[1]].values)
            xnocom[2] = xnocom[2].replace(" ", "")
            self.data[str(xnocom[2])] = encoder.fit_transform(self.data[xnocom[2]].values)
            xnocom[3] = xnocom[3].replace(" ", "")
            self.data[str(xnocom[3])] = encoder.fit_transform(self.data[xnocom[3]].values)
            xnocom[4] = xnocom[4].replace(" ", "")
            self.data[str(xnocom[4])] = encoder.fit_transform(self.data[xnocom[4]].values)
            xnocom[5] = xnocom[5].replace(" ", "")
            self.data[str(xnocom[5])] = encoder.fit_transform(self.data[xnocom[5]].values)
            xnocom[6] = xnocom[6].replace(" ", "")
            self.data[str(xnocom[6])] = encoder.fit_transform(self.data[xnocom[6]].values)
            xnocom[7] = xnocom[7].replace(" ", "")
            self.data[str(xnocom[7])] = encoder.fit_transform(self.data[xnocom[7]].values)
            X = self.data[[str(xnocom[0]), str(xnocom[1]), str(xnocom[2]),str(xnocom[3]), str(xnocom[4]), str(xnocom[5]), str(xnocom[6]), str(xnocom[7])]]
        
        Y = self.data[self.ejey]
        
        xval, xprueb, yval, y_test = train_test_split(X,Y)
        scaler = StandardScaler()
        scaler.fit(xval)
        
        xval = scaler.transform(xval)

        xprueb = scaler.transform(xprueb)
        net = MLPClassifier(
            hidden_layer_sizes = (100,), 
            max_iter=500000, 
            alpha=0.0001, 
            solver='adam',
            random_state=21, 
            tol=0.000000001)
        
        net.fit(xval, yval)
        predictions=net.predict(xprueb)
        self.st.write(classification_report(y_test,predictions))
        