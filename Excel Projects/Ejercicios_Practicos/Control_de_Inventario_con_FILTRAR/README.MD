# 📦 Control de Inventario usando `FILTRAR()` en Excel

Este ejercicio práctico consiste en la creación de un **sistema básico de control de inventario** utilizando la función `FILTRAR()` de Excel para clasificar productos según su disponibilidad de stock.  
Forma parte de mi sección de Excel **Ejercicios Practicos** para demostrar habilidades intermedias y en un futuro de tipo Avanzadas en Excel.

---

## 🎯 Objetivo

Desarrollar una hoja de control donde, de forma dinámica, se puedan visualizar:
- Productos **con stock** (cantidad > 0)
- Productos **sin stock** (cantidad = 0)

El listado se actualiza automáticamente conforme se modifican las cantidades.

---

## 📝 Descripción

El archivo contiene:
- Una tabla de productos con su cantidad actual
- Dos listas automáticas:
  - ✅ **Con stock** → productos disponibles para venta
  - ❌ **Sin stock** → productos agotados o fuera de existencia

Se utilizó la fórmula:
```
=FILTRAR(matriz, incluir, [si_vacio])
```
en donde:

- matriz: son las celdas donde estan los productos que queremos clasificar
- incluir: son las celdas donde estan las cantidades de stock de cada producto y allí mismo se coloca el condicional correspondiente (>=1 para "con stock" y =0 para "sin stock") 
- [si_vacio]: en caso de que no se cumpla dicha condicion, se deja la celda resultante en blanco con dobles comillas " "

Esto permite una automatización sencilla y eficiente del seguimiento de inventario sin necesidad de macros o VBA.


## 🛠️ Habilidades aplicadas
- Manejo de rangos y tablas de datos
- Uso de la función FILTRAR() para generar listas dinámicas
- Aplicación de formato condicional y diseño profesional
- Automatización básica de tareas repetitivas


