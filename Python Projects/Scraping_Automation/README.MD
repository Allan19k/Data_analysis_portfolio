# 🕸️ Scraping Automation con Hilos en Python

En esta carpeta documento diferentes **ejercicios prácticos de web scraping y automatización** desarrollados en Python para la materia de Computo Paralelo y Distribuido.
El enfoque principal fue aplicar **concurrencia con hilos (`threading`)** para optimizar las descargas y consultas a diferentes fuentes de datos.

## 📑 Ejercicios incluidos

- [`gatitos/`](./gatitos): 🐈 Descarga concurrente de imágenes de gatos desde [placecats.com](https://www.placecats.com/).  
  Incluye documento detallado y carpeta con los resultados.

- [`pokemon/`](./pokemon): 🐗 Uso de la API pública [PokeAPI](https://pokeapi.co/) para extraer información de Pokémon (nombre, habilidades, peso, etc.) de forma concurrente.

- [`usuarios/`](./usuarios): 👤 Uso de la API pública [RandomUser](https://randomuser.me/) para generar usuarios aleatorios y obtener información como nombre, email, ubicación, etc., de manera concurrente.

## ⚙️ Tecnologías utilizadas

- **Python 3**
- `threading`
- `requests`
- Manejo de archivos (`os`)

## 🎯 Objetivo

Estos ejercicios tienen como finalidad mostrar cómo **automatizar la obtención de datos** desde distintas fuentes (APIs o web scraping) aplicando **hilos** para mejorar el rendimiento.  
Además, son un primer acercamiento para proyectos más complejos donde se requiera **procesar grandes volúmenes de datos en paralelo**.
