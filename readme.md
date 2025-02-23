# App Chistes - Aplicación de Chistes

## Descripción

App Chistes es una aplicación que arroja chistes en inglés o español desde [JokeAPI](https://sv443.net/jokeapi/v2/).  
La aplicación muestra los chistes en ventanas emergentes, proporciona chistes tanto de una sola línea como de dos partes.

---

## Características

- Chistes en dos idiomas: inglés y español.
- Manejo de chistes de una sola línea y de dos partes (setup y delivery).
- Uso de JokeAPI para obtener contenido dinámico.
- Visualización de chistes mediante ventanas emergentes.

---

## Instalación y Ejecución

Este proyecto puede instalarse utilizando **Pipenv** o **pip** con **venv**.

### Opción 1: Usando Pipenv (Recomendado)

1. Instalar Pipenv (si no está instalado):

   `pip install pipenv`

2. Instalar las dependencias:

    `pipenv install --deploy`

3. Activar el entorno virtual:

    `pipenv shell`

4. Ejecutar la aplicación:

    `python app_chistes.py`

### Opción 2: Usando pip y venv

1. Crear un entorno virtual:

    `python -m venv venv`

2. Activar el entorno virtual:

    - En Windows:

        `venv\Scripts\activate`

    - En Linux/macOS:

        `source venv/bin/activate`

3. Instalar las dependencias:

    `pip install -r requirements.txt`

4. Ejecutar la aplicación:

    `python app_chistes.py`