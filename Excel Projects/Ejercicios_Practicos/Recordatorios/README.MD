# 📅 Tabla de Recordatorios con Formato Condicional Avanzado

## 🎯 Objetivo
Crear una tabla dinámica de recordatorios que permita visualizar, de manera automática y clara, cuántos días faltan para que se cumpla una fecha límite o cuántos días han pasado desde que venció.

## 📝 Descripción
En este ejercicio de Excel, se construyó una **tabla de tareas** con su **fecha final** y un cálculo automático que determina si la tarea está:
- **En tiempo** ✅
- **Vence hoy** 📅
- **Atrasada** ❌

Esto se logra restando la fecha actual (`HOY()`) de la fecha final y usando un formato de número personalizado con colores y texto.

## ⚙️ Funciones y Herramientas Utilizadas
- **Función `HOY()`**: para obtener la fecha actual del sistema.
- **Resta de Fechas**: `= [Fecha Final] - HOY()`.
- **Formato de Número Personalizado**: [Verde]# " Días faltantes";[Rojo]# " Días tarde";[Azul]# " Hoy"
- **Tablas en Excel**: para organizar y manejar mejor los datos.

## 📌 Resultado
- Los valores en **verde** indican días que faltan para la fecha límite.
- Los valores en **rojo** muestran cuántos días han pasado desde que venció la tarea.
- Los valores en **azul** indican que la fecha límite es **hoy**.

Este tipo de tabla es ideal para **gestión de proyectos, control de entregas** o **seguimiento de pendientes**.

---

