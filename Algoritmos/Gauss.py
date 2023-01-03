from Algoritmos.Algorithm import Algorithm
import streamlit 


class Gauss(Algorithm):
    def __init__(self, name, data, streamLitInstance: streamlit, ):
        super().__init__(name, data, streamLitInstance)
        