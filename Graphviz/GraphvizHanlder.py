from pathlib import Path
import pydot


class GraphvizHanlder:

    def __init__(self, dot_script):
        self.dot_script = dot_script

    def toPng(self, output_path):
        poli_png_path = Path(output_path)

        graphs = pydot.graph_from_dot_data(self.dot_script)
        graph = graphs[0]
        graph.write_png(poli_png_path)

        return poli_png_path
