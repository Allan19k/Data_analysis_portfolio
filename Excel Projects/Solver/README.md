# 📊 Investigación de Operaciones I - Modelos de Programación Lineal en Excel Solver

Este proyecto contiene la resolución de **dos problemas clásicos de programación lineal** del libro *"Investigación de Operaciones"* de Hamdy A. Taha, utilizando la herramienta **Solver de Excel**. Ambos modelos están enfocados en **optimización de recursos** para maximizar beneficios bajo restricciones prácticas.

---

## 📌 Problema 1: Producción de Pinturas - Reddy Mikks

### 📝 Descripción

La compañía **Reddy Mikks** produce pinturas para **interiores** y **exteriores**, utilizando dos materias primas: M1 y M2. El objetivo es **maximizar la utilidad diaria**, sujeta a la disponibilidad de materias primas y la demanda del mercado.

### ⚙️ Variables de decisión

- `x1`: Toneladas de pintura para exteriores.
- `x2`: Toneladas de pintura para interiores.

### 🎯 Función objetivo

Maximizar la utilidad:  
**Z = 5x1 + 4x2** *(en miles de dólares)*

### 🔒 Restricciones

1. 6x1 + 4x2 ≤ 24   *(Materia prima M1 disponible)*
2. x1 + 2x2 ≤ 6     *(Materia prima M2 disponible)*
3. x2 - x1 ≤ 1      *(Límite de mercado)*
4. x2 ≤ 2        *(Demanda máxima interior)*
5. x1, x2 ≥ 0      *(No negatividad)*

### 💻 Implementación

El modelo fue resuelto usando **Excel Solver**. Se usaron fórmulas con `SUMPRODUCT` para automatizar la función objetivo y restricciones, estableciendo como objetivo la celda de utilidad y cambiando las variables `x1` y `x2`.

---

## 📌 Problema 2: Planeación de Producción - Ropa de Invierno

### 📝 Descripción

Una empresa de ropa desea planificar la producción de chamarras, pantalones y guantes durante la temporada invernal. Existen capacidades limitadas por departamento y penalizaciones por no cumplir con la demanda. El objetivo es **maximizar la utilidad neta** (ganancia - penalización).

### ⚙️ Variables de decisión

- `x1`: Chamarras de piel
- `x2`: Chamarras con relleno de plumas
- `x3`: Pantalones
- `x4`: Guantes

Variables de escasez:
- `s1` a `s4`: Unidades faltantes de cada producto.

### 🎯 Función objetivo

Maximizar la utilidad neta:  
**Z = 30x1 + 40x2 + 20x3 + 10x4 - 15s1 - 20s2 - 10s3 - 8s4**

### 🔒 Restricciones

- Restricciones de capacidad en 4 departamentos (corte, aislamiento, costura, empaque).
- Restricciones de demanda:
  - x1 + s1 = 800
  - x2 + s2 = 750
  - x3 + s3 = 600
  - x4 + s4 = 500
- No negatividad para `x` y `s`.

### 💻 Implementación

El modelo fue implementado y resuelto en Excel utilizando Solver. Se establecieron las restricciones de capacidad, demanda y no negatividad, maximizando la utilidad neta en función de las unidades producidas y las penalizaciones aplicadas por la escasez.

---

## 🧠 Conclusiones

- **Excel Solver** es una herramienta poderosa y accesible para resolver modelos clásicos de programación lineal.
- El proyecto refuerza habilidades clave en:
  - Formulación matemática de problemas reales.
  - Traducción de modelos a hojas de cálculo.
  - Uso del complemento Solver para encontrar soluciones óptimas.
- Este tipo de práctica es fundamental para roles de **optimización, logística, operaciones y análisis de datos**.

---

## 📄 Licencia

Este proyecto académico es de uso libre con fines educativos.

---

## 🙋 Autor

**[Allan Hall Solorio 358909]**  
Estudiante de Ingeniería en ciencias de la computación, *Investigación de Operaciones I*, Docente: Olanda Prieto Ordaz
