# 🐉 Scraper de Pokémon con Hilos

Este script utiliza la API pública [PokeAPI](https://pokeapi.co/) para obtener información de Pokémon específicos.  
Se implementa concurrencia con **`threading`** para hacer múltiples consultas de forma simultánea.

## 📌 Descripción

- Consulta datos de Pokémon desde la API (ejemplo: Bulbasaur en la ruta `/api/v2/pokemon/1/`).
- Extrae información como:
  - Nombre
  - Altura
  - Peso
  - Habilidades
- Imprime los resultados en consola.

## ⚙️ Librerías utilizadas

- `requests` → para realizar peticiones HTTP a la API.  
- `threading` → para realizar múltiples consultas concurrentes.  

## 🎯 Objetivo

Mostrar cómo usar hilos para hacer scraping/consultas concurrentes a una API de datos abiertos, en este caso PokeAPI.
