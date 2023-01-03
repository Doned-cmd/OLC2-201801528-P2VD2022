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
        ejex = ejexs
        ejey = ejeys
        
    def execute(self):
        encoder = LabelEncoder()
        new_x = self.ejex.replace("\"", "")
        Separador_x = new_x.split(",")
        tama = len(Separador_x)
        X = self.data[[]]
        
        if tama == 1:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            X = self.data[[str(Separador_x[0])]]
        elif tama == 2:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1])]]
        elif tama == 3:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            Separador_x[2] = Separador_x[2].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            self.data[str(Separador_x[2])] = encoder.fit_transform(self.data[Separador_x[2]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1]), str(Separador_x[2])]]
        elif tama == 4:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            Separador_x[2] = Separador_x[2].replace(" ", "")
            Separador_x[3] = Separador_x[3].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            self.data[str(Separador_x[2])] = encoder.fit_transform(self.data[Separador_x[2]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1]), str(Separador_x[2]), str(Separador_x[3])]]
        elif tama == 5:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            Separador_x[2] = Separador_x[2].replace(" ", "")
            Separador_x[3] = Separador_x[3].replace(" ", "")
            Separador_x[4] = Separador_x[4].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            self.data[str(Separador_x[2])] = encoder.fit_transform(self.data[Separador_x[2]].values)
            self.data[str(Separador_x[3])] = encoder.fit_transform(self.data[Separador_x[3]].values)
            self.data[str(Separador_x[4])] = encoder.fit_transform(self.data[Separador_x[4]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1]),str(Separador_x[2]), str(Separador_x[3]), str(Separador_x[4])]]
        elif tama == 6:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            Separador_x[2] = Separador_x[2].replace(" ", "")
            Separador_x[3] = Separador_x[3].replace(" ", "")
            Separador_x[4] = Separador_x[4].replace(" ", "")
            Separador_x[5] = Separador_x[5].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            self.data[str(Separador_x[2])] = encoder.fit_transform(self.data[Separador_x[2]].values)
            self.data[str(Separador_x[3])] = encoder.fit_transform(self.data[Separador_x[3]].values)
            self.data[str(Separador_x[4])] = encoder.fit_transform(self.data[Separador_x[4]].values)
            self.data[str(Separador_x[5])] = encoder.fit_transform(self.data[Separador_x[5]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1]), str(Separador_x[2]),str(Separador_x[3]), str(Separador_x[4]), str(Separador_x[5])]]
        elif tama == 7:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            Separador_x[2] = Separador_x[2].replace(" ", "")
            Separador_x[3] = Separador_x[3].replace(" ", "")
            Separador_x[4] = Separador_x[4].replace(" ", "")
            Separador_x[5] = Separador_x[5].replace(" ", "")
            Separador_x[6] = Separador_x[6].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            self.data[str(Separador_x[2])] = encoder.fit_transform(self.data[Separador_x[2]].values)
            self.data[str(Separador_x[3])] = encoder.fit_transform(self.data[Separador_x[3]].values)
            self.data[str(Separador_x[4])] = encoder.fit_transform(self.data[Separador_x[4]].values)
            self.data[str(Separador_x[5])] = encoder.fit_transform(self.data[Separador_x[5]].values)
            self.data[str(Separador_x[6])] = encoder.fit_transform(self.data[Separador_x[6]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1]), str(Separador_x[2]),str(Separador_x[3]), str(Separador_x[4]), str(Separador_x[5]), str(Separador_x[6])]]
        elif tama == 8:
            Separador_x[0] = Separador_x[0].replace(" ", "")
            Separador_x[1] = Separador_x[1].replace(" ", "")
            Separador_x[2] = Separador_x[2].replace(" ", "")
            Separador_x[3] = Separador_x[3].replace(" ", "")
            Separador_x[4] = Separador_x[4].replace(" ", "")
            Separador_x[5] = Separador_x[5].replace(" ", "")
            Separador_x[6] = Separador_x[6].replace(" ", "")
            Separador_x[7] = Separador_x[7].replace(" ", "")
            self.data[str(Separador_x[0])] = encoder.fit_transform(self.data[Separador_x[0]].values)
            self.data[str(Separador_x[1])] = encoder.fit_transform(self.data[Separador_x[1]].values)
            self.data[str(Separador_x[2])] = encoder.fit_transform(self.data[Separador_x[2]].values)
            self.data[str(Separador_x[3])] = encoder.fit_transform(self.data[Separador_x[3]].values)
            self.data[str(Separador_x[4])] = encoder.fit_transform(self.data[Separador_x[4]].values)
            self.data[str(Separador_x[5])] = encoder.fit_transform(self.data[Separador_x[5]].values)
            self.data[str(Separador_x[6])] = encoder.fit_transform(self.data[Separador_x[6]].values)
            self.data[str(Separador_x[7])] = encoder.fit_transform(self.data[Separador_x[7]].values)
            X = self.data[[str(Separador_x[0]), str(Separador_x[1]), str(Separador_x[2]),str(Separador_x[3]), str(Separador_x[4]), str(Separador_x[5]), str(Separador_x[6]), str(Separador_x[7])]]
        
        Y = self.data[self.ejey]
        
        X_train, X_test, y_train, y_test = train_test_split(X,Y)
        scaler = StandardScaler()
        scaler.fit(X_train)
        print("**************************************************")
        print(X_train)
        print("**************************************************")
        X_train = scaler.transform(X_train)

        X_test = scaler.transform(X_test)
        net = MLPClassifier(
            hidden_layer_sizes = (100,), 
            max_iter=500000, 
            alpha=0.0001, 
            solver='adam',
            random_state=21, 
            tol=0.000000001)
        
        net.fit(X_train, y_train)
        predictions=net.predict(X_test)
        self.st.write(classification_report(y_test,predictions))
        