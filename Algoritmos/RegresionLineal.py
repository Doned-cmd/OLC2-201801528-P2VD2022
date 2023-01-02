import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression;
import streamlit
from sklearn.metrics import mean_squared_error, r2_score;
from PIL import Image
import pydot
from pathlib import Path

def regresionLineal(data, prediccionx,ejex, ejey, st:streamlit):
    
    X = np.asarray(data[ejex]).reshape(-1,1)
    Y = data[ejey]

    regresionlinealvar = LinearRegression()
    regresionlinealvar.fit(X,Y)
    prediccion = regresionlinealvar.predict(X)
    r2 = r2_score(Y, prediccion)
    coeficiente = regresionlinealvar.coef_
    error_medio = mean_squared_error(Y, prediccion, squared=True)
    intercepto = regresionlinealvar.intercept_

    formato_funcion_lineal  = "Y = "+  str(round(coeficiente[0],3)) + "x " + str(round(intercepto, 3))

    writethis = '''digraph G { edge [fontname="Helvetica,Arial,sans-serif"]\n
subgraph cluster1 {fillcolor="blue:green"'''+'''label='''+'''\"'''+ formato_funcion_lineal + "\n Error Medio:"+ str(error_medio) + "\n R2:" + str(r2) +'''\"''' +'''fontcolor="white" style="filled" gradientangle="270"\n
 node [shape=box fillcolor="red:yellow" style="filled" gradientangle=90]Funcion;\n
}}\n  '''
    
    #graf = open("./Images/funcion.dot", 'w', encoding='utf-8')
    #graf.close()
    
    #dot_txt = 'digraph G {\n    start -> end;\n}'
        
    poli_png_path = Path.joinpath(Path('./img').resolve(), 'linealreg.png')
    
    graphs = pydot.graph_from_dot_data(writethis)
    graph = graphs[0]
    graph.write_png(poli_png_path)

    
    
    
    Y_point = regresionlinealvar.predict([[int(prediccionx)]])
    
    st.write(Y_point)
    
    titulo = 'Prediccion = {}; Coeficiente = {}; R2 = {}; Y = {}'.format(round(Y_point[0], 3), round(coeficiente[0],2), round(r2,2), formato_funcion_lineal)
    plt.title("Grafico de " + str(ejex) + " en funcion del " +str(ejey)+"\n" + titulo, fontsize=10)
    
    plt.scatter(X, Y)
    plt.plot(X,Y)
    url_img = './img/Regresion.png'
    plt.savefig(url_img)
    
    image = Image.open(url_img)
    st.image(image, caption='Grafico I: Regresion lineal.')
    
    image2 = Image.open(poli_png_path)
    st.image(image2, caption='Grafico II: Funcion Diseñada.')