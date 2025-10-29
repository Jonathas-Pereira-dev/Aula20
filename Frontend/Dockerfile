FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copia todo o conteúdo (o volume montado em dev sobrescreverá isso)
COPY . /app

# Expõe a porta usada no docker-compose
EXPOSE 8501

# Se você tiver uma app (ex: Streamlit) troque o CMD abaixo.
# Por enquanto iniciamos um servidor HTTP simples para servir a pasta /app
CMD ["python", "-m", "http.server", "8501", "--bind", "0.0.0.0"]
