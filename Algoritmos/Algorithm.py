import streamlit


class Algorithm:

    def __init__(self, name, data, streamLitInstance: streamlit):
        self.st = streamLitInstance
        self.name = name
        self.data = data

    def execute(self):
        pass
