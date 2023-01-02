import numpy as np
import streamlit 
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from PIL import Image
import pydot
from pathlib import Path
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

def PrediccionNeuronal(data,ejex, ejey, prediccion, st:streamlit):
    X = np.asarray(data[ejex]).reshape(-1,1)
    Y = data[ejey]
    xpru, xval, ypru, yval = train_test_split(X,Y)
    net = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(3,3), random_state=1)
    net.fit(xpru, ypru)
    pred = net.predict(np.array([int(prediccion)]).reshape(1,-1))
    st.write(pred)
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
    
    image4 = Image.open('Neuronal.png')
    st.image(image4, caption='Grafico II: Prediccion Neuronal.')
    
def ClasificacioNeuronal(data, ejex, ejey, st:streamlit):
    encoder = LabelEncoder()
    new_x = ejex.replace("\"", "")
    Separador_x = new_x.split(",")
    tama = len(Separador_x)
    X = data[[]]
    if tama == 1:
          temporal = encoder.fit_transform(data[Separador_x[0]].values)
          X = data[[temporal]]
    elif tama == 2: 
        X = data[[Separador_x[0],Separador_x[1]]]
    elif tama == 3: 
        data[str(Separador_x[0])] = encoder.fit_transform(data[Separador_x[0]].values)
        data[str(Separador_x[1])] = encoder.fit_transform(data[Separador_x[1]].values)
        data[str(Separador_x[2])] = encoder.fit_transform(data[Separador_x[2]].values)
        X = data[[str(Separador_x[0]),str(Separador_x[1]),str(Separador_x[2])]]
    elif tama == 4: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3]]]  
    elif tama == 5: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4]]] 
    elif tama == 6: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4],Separador_x[5]]]
    elif tama == 7: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4],Separador_x[5],Separador_x[6]]]
    elif tama == 8: 
        X = data[[Separador_x[0],Separador_x[1],Separador_x[2],Separador_x[3],Separador_x[4],Separador_x[5],Separador_x[6],Separador_x[7]]]
    
    
    y = data[ejey]
    X_train, X_test, y_train, y_test = train_test_split(X,y)
    scaler = StandardScaler()
    scaler.fit(X_train)
    print("**************************************************")
    print(X_train)
    print("**************************************************")
    X_train = scaler.transform(X_train)

    X_test = scaler.transform(X_test)
    net = MLPClassifier(hidden_layer_sizes = (100,), max_iter=500000, alpha=0.0001, solver='adam',
                    random_state=21, tol=0.000000001)
    net.fit(X_train, y_train)
    predictions=net.predict(X_test)
    st.write(classification_report(y_test,predictions))
    