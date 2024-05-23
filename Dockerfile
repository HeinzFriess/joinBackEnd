# Dockerfile

# Verwende ein offizielles Python-Runtime als Basis-Image
FROM python:3.10.

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen-Datei ins Arbeitsverzeichnis
COPY requirements.txt /app/

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Anwendungsquellcodes
COPY . /app/

# Setze die Umgebungsvariablen
ENV PYTHONUNBUFFERED 1

# Starte die Django-Anwendung
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
