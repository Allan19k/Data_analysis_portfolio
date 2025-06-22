# 🧪 Generación de Datos Ficticios con Faker – Python

Esta sección del portafolio presenta el uso de la librería **`Faker`** para generar datos sintéticos en español (`es_MX`) con fines de prueba, simulación, visualización o análisis. Se desarrollaron tres scripts funcionales que permiten exportar los registros generados a distintos formatos, simulando estructuras realistas de una base de datos de personas.

---

## 🎯 Objetivo del proyecto

- Generar datos ficticios estructurados para usarlos en pruebas de análisis de datos, desarrollo backend o visualización.
- Exportar los datos generados a archivos `.csv` y `.xlsx`.
- Demostrar el uso de `Faker` en diferentes niveles: desde el básico hasta exportaciones listas para producción.

---

## 📁 Estructura del repositorio

```
Faker_for_Dummy_Data/
├── faker_basico.py                  ← Versión básica que imprime datos en consola
├── generar_dummy_data_en_CSV/
│   ├── dummy_data_CSV.py            ← Script que genera y exporta datos a CSV
│   └── registros_ficticios.csv      ← Archivo de salida generado
├── generar_dummy_data_en_xlsx/
│   ├── dummy_data_xlsx.py           ← Script que genera y exporta datos a Excel con openpyxl
│   └── registros_ficticios.xlsx     ← Archivo de salida generado
└── README.md                        ← Este archivo

```

---

## 🧩 Descripción de los scripts
### 1. faker_basico.py
Genera datos aleatorios y los imprime directamente en consola. Es ideal como introducción rápida al uso de la librería Faker.

2. generar_csv.py

Genera 50 registros ficticios (nombre, correo, dirección, etc.) y los guarda en un archivo datos_ficticios.csv. Utiliza la librería estándar de Python csv.

3. generar_excel.py

Genera los mismos datos que los scripts anteriores, pero los exporta directamente a un archivo Excel .xlsx utilizando la librería openpyxl, sin necesidad de pandas.

### 📝 ¿Qué es openpyxl?

openpyxl es una librería de Python que permite crear, leer y modificar archivos de Excel (.xlsx). En este proyecto se usa para:

    Crear un libro de Excel desde cero

    Agregar encabezados y registros de forma controlada

    Guardar el archivo como si fuera generado manualmente en Excel

Esto es útil en entornos donde se requiere generar reportes automatizados que pueden abrirse directamente en Microsoft Excel u otras herramientas compatibles.


---

## 📊 Campos generados en el faker_basico.py

    Nombre

    Email

    Direccion

    Teléfono

    Texto aleatorio 

    Fecha de nacimiento

    Trabajo

    Compañia

    País

    
Puedes usar los campos que nececites para generar los datos ficticios (en el de CSV solo puse nombre,edad e email y en el de excel le agregue teléfono)
---

## 🧠 Importancia de generar dummy data

En contextos como el análisis de datos, inteligencia artificial o desarrollo de software, la generación de datos ficticios permite:

    Realizar pruebas sin comprometer datos reales o sensibles

    Simular tráfico o bases de datos de usuarios

    Poblar prototipos de dashboards o sistemas backend

    Entrenar modelos de IA con estructuras de datos realistas

🔍 En empresas como Black Labs, esta técnica es fundamental para construir entornos controlados de prueba, crear datasets sintéticos o proteger la privacidad en ambientes de desarrollo.


---

## 🛠️ Tecnologías utilizadas

    Faker – para generación de datos ficticios realistas

    csv – para exportar datos a formato estructurado

    openpyxl – para creación de archivos Excel .xlsx desde cero

    Python 3.10+


---

## 📄 Licencia

Este proyecto es de uso académico, educativo y técnico. Todos los datos generados son completamente ficticios y no corresponden a personas reales. Puedes reutilizar el contenido siempre que se otorgue el crédito correspondiente.
