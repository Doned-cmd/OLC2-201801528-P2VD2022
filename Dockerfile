FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

RUN apt-get update \
  && apt-get install -y --no-install-recommends graphviz \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir pyparsing pydot

COPY . .
RUN pip3 install -r requirements.txt

# Comandos para
# Construir la imagen: docker build -t olc .
# Crear el contenedor: docker run -p 8501:8501 -d .
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]