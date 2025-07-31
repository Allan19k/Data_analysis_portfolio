# 📊 Fundamentos de Excel (Básico a Intermedio)

Este directorio contiene las prácticas y ejercicios realizados durante el curso **"Excel"** impartido por **Santander Open Academy**, diseñado para reforzar conocimientos desde nivel básico hasta intermedio en el manejo de datos con Excel.

## ✅ Temas Abordados

- 📌 **Rangos y Tablas**
  - Diferencias clave entre ambos
  - Conversión de rango a tabla y viceversa
  - Cambio de nombre y tamaño de tablas

- 🔍 **Filtrado y Segmentación**
  - Filtros en rangos y tablas
  - Uso de segmentadores para exploración dinámica

- 📂 **Ordenamiento de Datos**
  - Orden ascendente/descendente
  - Criterios personalizados

- 📎 **Referencias**
  - Relativas y absolutas
  - Referencias entre hojas

- 🔧 **Funciones Utilizadas**
  - `SI`, `BUSCARV`, `CONTAR`, `CONTAR.SI`
  - Aplicaciones en tablas, rangos y hojas vinculadas

- 📈 **Tablas Dinámicas**
  - Creación, filtrado y modificación de áreas
  - Exploración y análisis dinámico de datos

- 🧩 **Complementos**
  - Guía rápida de instalación y uso de complementos en Excel

## 🧪 Ejercicios Realizados

### Ejercicio 1: [`Fila de totales`](./Fila_de_totales.xlsx) 
- **Instrucción**: Configurar la fila de totales totalizando las siguientes columnas con las funciones indicadas:

    `CURSO: Recuento`

    `DURACIÓN: Suma`

    `IMPORTE CLIENTE: Suma`

    `IMPORTE PROFESOR: Promedio`

    `FECHA CURSO: Mínimo`

- **Herramientas**: Tabla y fila de totales.

### Ejercicio 2: [`Filtrar datos I`](./Filtrar_datos_I.xlsx) 
- **Instrucción**:  Configurar el filtro aplicado en la columna CURSO (DISEÑO, PROGRAMACIÓN y WORD). Luego filtrar las columnas de la siguiente manera:

    `JORNADA CURSO: MAÑANA Y TARDE`

    `PAGADO CLIENTE: NO`

    `PAÍS: ITALIA`

- **Herramientas**: Tabla y filtos.

### Ejercicio 3: [`Filtrar datos I_2`](./Filtrar_datos_I_2.xlsx)
- **Instrucción**: Eliminar todos los filtros y filtrar las siguientes columnas:

    `CURSO: WORD, EXCEL Y ACCESS`

    `IMPORTE CLIENTE: MENOR QUE 1000`

    `PAÍS: ITALIA`

    `JORNADA CURSO: MAÑANA Y NOCHE`

- **Herramientas**: Tabla y filtros.

### Ejercicio 4: [`Filtrar datos II`](./Filtrar_datos_II.xlsx)
- **Objetivo**: Quitar todos los filtros y realizar el siguiente filtro

     `CLIENTE: CLIENTE-001, CLIENTE-003, CLIENTE-005 y CLIENTE-008`

     `FECHA CURSO: SEIS PRIMEROS MESES DE LOS AÑOS 2019 Y 2021`

     `DURACION: MAYOR QUE 20`

     `PAIS: ESPAÑA e ITALIA`

     `PAGADO CLIENTE: NO`

Consultar los resultados de la fila de totales

- **Herramientas**: Tabla, filtros y fila de totales

### Ejercicio 5: [`Mini practica`](./Mini_practica_1.xlsx)

En esta base de datos se registran diferentes facturas y posee las siguientes columnas:

     NUMERO FACTURA CLIENTE: se indica el número de la factura.
     CONCEPTO: el concepto que estamos facturando.
     CLIENTE: el cliente al que le emitimos la factura
     PROVINCIA: provincia en la que reside el cliente al que le facturamos.
     SECTOR: sector de actividad empresarial al que pertenece el cliente al que facturamos.
     IMPORTE CLIENTE: importe que facturamos al cliente.
     FECHA FACTURA CLIENTE: fecha de emisión de la factura.
     PAGADA CLIENTE: indicamos si el cliente ha pagado o no la factura.
     PROVEEDOR: cada factura que hacemos es un servicio que contratamos a un proveedor, por tanto, en esta columna indicamos el nombre del proveedor que estamos contratando para dar el servicio que estamos facturando.
     ZONA: la zona geográfica que cubre el proveedor.
     TIPO: qué tipo de proveedor es.
     IMPORTE PROVEEDOR: el importe que nos cobra el proveedor por darnos el servicio contratado

- **Objetivo**: Realizar las siguientes acciones y configuraciones en los datos del documento:

  - `1. Insertar una tabla sobre el rango`
  - `2. Nombrar la tabla con el nombre T_FACTURAS`
  - `3. Ordenar la tabla por las columnas: concepto e importe cliente ambas columnas en orden ascendente`
  - `4. Mostrar la fila de totales con la siguiente configuración:`

    `NUMERO FACTURA CLIENTE: recuento`

    `IMPORTE CLIENTE: suma`

    `IMPORTE PROVEEDOR: suma`

  - `5. Mostrar las segmentaciones de las columnas: PROVINCIA y TIPO`
  - `6. Filtrar las facturas en las provincias MADRID y BARCELONA, con FECHA FACTURA de los 4 primeros meses de los años 2019 y 2020 de TIPO INTERNO e IMPORTE CLIENTE MAYOR de 1000`
  - `7. Consultar el resultado de la fila de totales`
  - `8. Quitar todos los filtros aplicados`
  - `9. Ocultar la fila de totales`
  - `10. Eliminar la segmentación del campo PROVINCIA`

- **Herramientas**: Tabla, nombre de tabla, ordenar tabla, filtros, fila de totales, segmentaciones

### Ejercicio 6: [`Referencias Relativas y Absolutas I`](./Referencias_Relativas_y_Absolutas_I.xlsx)
- **Objetivo**: Calcular la columna % BENEFICIO del ejercicio que sería: % BENEFICIO = MARGEN BENEFICIO / PRECIO COMPRA

     `Ajustar el formato de número para que se vea como porcentaje (%)`

     `Copiar la fórmula al resto de productos`

- **Herramientas**: referencias relativas, operaciones aritmeticas, formato

### Ejercicio 7: [`Referencias Relativas y Absolutas II`](./Referencias_Relativas_y_Absolutas_II.xlsx)
- **Objetivo**: Calcular las columnas SUELDO BRUTO, IMPORTE RETENCION y SUELDO NETO con las siguientes fórmulas:

     `SUELDO BRUTO: SALARIO BASE + IMPORTE COMISION`

     `IMPORTE RETENCION: SUELDO BRUTO * RETENCION`

     `SUELDO NETO: SUELDO BRUTO – IMPORTE RETENCION`

Ajusta bien la referencia en cada fórmula para copiarla al resto de vendedores

- **Herramientas**: referencias absolutas, operaciones aritmeticas, formato

### Ejercicio 8: [`Referencias Relativas y Absolutas III`](./Referencias_Relativas_y_Absolutas_III.xlsx)
- **Objetivo**: Calcular las columnas BENEFICIO y % BENEFICIO con las siguientes fórmulas:

     `Beneficio: importe cliente – gasto`

     `% beneficio: beneficio / importe cliente. Aplica a esta columna un formato %`


- **Herramientas**: tabla, referencias relativas, operaciones aritmeticas, formato

### Ejercicio 9: [`Funciones vinculando hojas de calculo I`](./Funciones_Vinculando_Hojas_de_Calculo_I.xlsx)
- **Objetivo**: Calcular en la celda B2 la suma de las duraciones de la hoja CURSOS y en la celda B3 la suma del IMPORTE CLIENTE y del IMPORTE COMERCIAL.

- **Herramientas**: función SUMA

### Ejercicio 10: [`Funciones vinculando hojas de calculo II`](./Funciones_Vinculando_Hojas_de_Calculo_II.xlsx)
- **Objetivo**: Inserta una hoja con el nombre: “CALCULOS 2” y realiza los siguientes cálculos en las siguientes celdas de dicha hoja:

     `En B1: contar el número de cursos con importe cliente mayor de 1000`

     `En B2: contar el número de cursos que no estén pagados por el cliente`

     `En B3: contar el número de cursos donde el país no sea España`

- **Herramientas**: función CONTAR.SI

### Ejercicio 11: [`Funciones vinculando hojas de calculo III`](./Funciones_Vinculando_Hojas_de_Calculo_III.xlsx)
- **Objetivo**: Realizar los siguientes cálculos, sobre la TABLA T_CURSOS en las celdas que a continuación se indica:

     `En B2: contar todos los datos de la columna curso`

     `En B3: contar el número de cursos con importe profesor menor de 500`

     `En B4: sumar las duraciones`

- **Herramientas**: función SUMA, CONTARA, CONTAR.SI

### Ejercicio 12: [`Funcion BUSCARV `](./Funcion_BUSCARV.xlsx)
- **Objetivo**: Buscar en las columnas D y F el precio de cada referencia y el proveedor que vende cada referencia

- **Herramientas**: función BUSCARV

### Ejercicio 13: [`Funcion BUSCARV con tablas `](./Funcion_BUSCARV_con_tablas.xlsx)
- **Objetivo**: Usando la misma base de datos de Funciones_BUSCARV.xlsx, ahora con los datos en forma de tabla, buscar en las columnas D y F el precio de cada referencia y el proveedor que vende cada referencia

- **Herramientas**: función BUSCARV

### Ejercicio 14: [`Funcion BUSCARV Verdadero`](./Funciones_BUSCARV_Verdadero.xlsx)
- **Objetivo**: Buscar en la columna H la comisión proporcional a la cantidad de unidades vendidas en cada mes usando en el rango "Verdadero" ya que debe ser una coicidencia aproximada y no exacta. 

- **Herramientas**: función BUSCARV

### Ejercicio 15: [`Funcion SI`](./Funciones_SI.xlsx)
- **Objetivo**: Calcular el importe dto (importe con descuento)  y el importe final de cada uno de los cursos enlistados

    `En importe dto aplicar un descuento del 10% en caso de que la duracion del curso sea mayor a 18, si no, devolver el texto "SIN DTO"`
    
    `En importe final devolver el precio final con el descuento en donde aplique`
    
- **Herramientas**: función SI

### Ejercicio 16: [`Modificar tablas dinamicas`](./Modificaciones_en_las_tablas_dinamicas.xlsx)
- **Objetivo**: En otra tabla dinamica mover los campos tal y como se indica:

    `Filtro: PAIS (filtrar por España)`

    `Fila: CLIENTE`

    `Valores: IMPORTE CLIENTE`

Ordena la tabla dinámica por la suma del importe cliente de menor a mayor
    
- **Herramientas**: tablas dinamicas

## 🧠 Objetivo

Fortalecer la base técnica para el **análisis de datos** con Excel, permitiendo automatizar cálculos, estructurar grandes volúmenes de información y construir reportes útiles para la toma de decisiones.

## 📄 Certificación

El certificado de finalización del curso está disponible en la carpeta raíz de esta sección y también se encuentra referenciado en el portafolio principal.

---

> 🚀 _Este módulo forma parte de mi preparación profesional en análisis de datos para aplicar a prácticas profesionales en Black Labs (Chihuahua)._


