from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import streamlit
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

from Algoritmos.Algorithm import Algorithm
from Graphviz.GraphvizHanlder import GraphvizHanlder


class RegresionPolinomial(Algorithm):

    def __init__(self, data, streamLitInstance: streamlit, eje_x, eje_y,
                 forecast, degree):
        super().__init__('Regresion Polinomial', data, streamLitInstance)
        self.degree = degree
        self.forecast = forecast
        self.eje_y = eje_y
        self.eje_x = eje_x
        self.img_path = Path('./img').resolve()

    def execute(self):
        x = np.asarray(self.data[self.eje_x]).reshape(-1, 1)
        y = np.asarray(self.data[self.eje_y]).reshape(-1, 1)
        plt.scatter(x, y)
        pf = PolynomialFeatures(degree=self.degree)
        print("------------------")
        print(self.degree)
        print("------------------")
        x_transform = pf.fit_transform(x)
        model = LinearRegression().fit(x_transform, y)
        y_new = model.predict(x_transform)
        rmse = np.sqrt(mean_squared_error(y, y_new))
        coeficitentes = model.coef_
        self.st.write(coeficitentes)
        funcion = ""
        contador = 0
        for i in coeficitentes[0]:
            funcion += str(i) + "x^" + str(contador)
            contador += 1

        self.st.write(funcion)
        r2 = r2_score(y, y_new)
        x_new_min = -x.min()
        x_new_max = x.max()
        x_new = np.linspace(x_new_min, x_new_max, 500)
        x_new = x_new[:, np.newaxis]
        x_new_transform = pf.fit_transform(x_new)
        y_new = model.predict(x_new_transform)
        plt.plot(x_new, y_new, color='coral', linewidth=3)
        plt.grid()
        plt.xlim(x.min(), x_new_max)
        plt.ylim(y.min(), y.max())
        pre = y_new[int(self.forecast)-1]
        self.st.write(pre)
        title = 'Degree = {}; RMSE = {}; R2 = {}; Prediccion = {}'.format(self.degree, round(rmse, 2), round(r2, 4),
                                                                          pre)
        plt.title("\n " + title, fontsize=10)
        plt.xlabel(str(self.eje_x))
        plt.ylabel(str(self.eje_y))

        rp_img_path = Path.joinpath(self.img_path, 'RegresionPolinomial.png')
        plt.savefig(rp_img_path)

        image = Image.open(rp_img_path)
        self.st.image(image, caption='Regresion Polinomial')
        plt.clf()

        dot_string = '''
                    digraph G { 
                        edge [fontname="Helvetica,Arial,sans-serif"] 
                        subgraph cluster1 {
                            fillcolor="blue:cyan"label= %s 
                            fontcolor="white" 
                            style="filled" 
                            gradientangle="270" 
                            node [shape=box fillcolor="red:yellow" style="filled" 
                            gradientangle=90]Funcion; 
                        }
                    } 
                    ''' % f'"Y = {str(funcion)}"'

        poli_png_path = Path.joinpath(self.img_path, 'poli.png')
        gh = GraphvizHanlder(dot_string)
        gh.toPng(poli_png_path)
        imagep = Image.open(poli_png_path)
        self.st.image(imagep, caption='Regresion Polinomial')
