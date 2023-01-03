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


class PrediccionNeuronal(Algorithm):
    def __init__(self, name, data, streamLitInstance: streamlit, ejexs, ejeys, prediccions):
        super().__init__(name, data, streamLitInstance)
        self.ejex = ejexs
        self.ejey = ejeys
        self.prediccion = prediccions

    def execute(self):
        X = np.asarray(self.data[self.ejex]).reshape(-1,1)
        Y = self.data[self.ejey]
        xpru, xval, ypru, yval = train_test_split(X,Y)
        net = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(3,3), random_state=1)
        net.fit(xpru, ypru)
        pred = net.predict(np.array([int(self.prediccion)]).reshape(1,-1))
        self.st.write(pred)
        writethis = '''
        digraph G { edge [fontname="Helvetica,Arial,sans-serif"]\n
        subgraph cluster1 {fillcolor="blue:cyan"'''+'''label='''+'''\"'''+ str(pred[0]) +'''\"''' +'''fontcolor="white" style="filled" gradientangle="270"\n
        node [shape=box fillcolor="red:yellow" style="filled" gradientangle=90]Prediccion;\n
        }}\n
        '''
        
        poli_png_path = Path.joinpath(Path('./img').resolve(), 'Neuronal.png')
        
        graphs = pydot.graph_from_dot_data(writethis)
        graph = graphs[0]
        graph.write_png(poli_png_path)
        
        image4 = Image.open(poli_png_path)
        self.st.image(image4, caption='Grafico II: Prediccion Neuronal.')
    
