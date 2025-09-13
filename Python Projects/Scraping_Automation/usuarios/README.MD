# 👤 Scraper de Usuarios Aleatorios con Hilos

Este script utiliza la API pública [RandomUser](https://randomuser.me/) para generar datos ficticios de usuarios.  
Se aplica **`threading`** para obtener varios perfiles de manera simultánea.

## 📌 Descripción

- Consulta datos de usuarios aleatorios desde la API.  
- Extrae información como:
  - Nombre completo
  - Email
  - País de residencia
- Muestra los resultados en consola.

## ⚙️ Librerías utilizadas

- `requests` → para realizar peticiones HTTP.  
- `threading` → para obtener múltiples usuarios en paralelo.  

## 🎯 Objetivo

Ejercicio práctico para demostrar cómo automatizar la recolección de datos de usuarios desde una API pública, optimizando las consultas con hilos
