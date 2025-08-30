# 📊 Power BI – Santander Open Academy  

Este curso de **Fundamentos de Power BI** (nivel básico-intermedio) fue impartido por **Santander Open Academy** y cubrió los aspectos esenciales para el análisis de datos y creación de reportes interactivos en Power BI Desktop.  

## ✅ Temas principales del curso
1. Introducción a Power BI: qué es y cómo instalarlo.  
2. Primer vistazo a la interfaz de Power BI Desktop.  
3. Importación de datos desde **Excel**, **CSV** y **TXT**.  
4. Formatos básicos y personalizados en columnas y datos.  
5. Creación de **primeros informes** y operaciones básicas en ellos.  
6. Interacción con informes: segmentación y navegación.  
7. Uso de **tarjetas y gráficos** para visualización.  
8. Panel de filtros: filtros básicos, filtros en campos totalizados y **TOP N**.  
9. **Formatos condicionales**: barras de datos, iconos, colores.  
10. Introducción a **Power Query**:  
    - Cambio de origen de datos.  
    - Operaciones básicas y transformaciones.  
    - Carga de datos a Power BI.  

---

## 📂 Ejercicios realizados

### Practica 1: Del fichero BD FACTURAS.xlsx  que es una base de datos en la que vamos registrando diferentes facturas realizadas a clientes, de distintos conceptos, y que tiene las siguientes columnas:

    NUMERO FACTURA CLIENTE: se indica el número de la factura.
    CONCEPTO: el concepto que estamos facturando.
    CLIENTE: el cliente al que le emitimos la factura.
    PROVINCIA: provincia en la que está el cliente al que le facturamos.
    SECTOR: sector al que pertenece el cliente al que facturamos.
    IMPORTE CLIENTE: importe que facturamos al cliente.
    FECHA FACTURA CLIENTE: fecha de emisión de la factura.
    PAGADA CLIENTE: indicamos si el cliente ha pagado o no la factura.
    PROVEEDOR: cada factura que hacemos es un servicio que contratamos a un proveedor, por tanto, en esta columna indicamos el nombre del proveedor que estamos contratando para dar el servicio que estamos facturando.
    ZONA: la zona que cubre el proveedor.
    TIPO: qué tipo de proveedor es.
    IMPORTE PROVEEDOR: el importe que nos cobra el proveedor por darnos el servicio contratado.

Realizar las siguientes operaciones:

    Inserta una tabla en el fichero BD FACTURAS con el nombre T_FACTURAS
    Guardar los cambios y cerrar el fichero.
    Abrir un Power BI en blanco
    Importar la tabla T_FACTURAS del fichero BD FACTURAS
    Expandir los campos en el panel de datos
    Ir a la vista tabla
    Guardar el fichero con el nombre BD FACTURAS

### Practica 2: Del fichero BD FACTURAS.txt (que tiene los mismos datos que el ejercicio anterior solo que en .txt). Realiza las siguientes operaciones: 

    Abrir un POWER BI en blanco
    Importar el fichero de texto BD FACTURAS
    Ir a la vista tabla
    Guardar el fichero con el nombre BD FACTURAS TXT

### Practica 2.1: En el fichero de Power BI BD FACTURAS, guardado anteriormente.

1. Ir a la vista tabla y cambiar los formatos de los siguientes campos:

    IMPORTE CLIENTE: personalizar un formato con separador de miles y dos posiciones decimales que termine con el texto: Eur. (por ejemplo, un importe de 1250,25 se mostrará como: 1.250,25 Eur.).
    IMPORTE PROVEEDOR: aplicar un formato moneda con el símbolo del €.
    FECHA FACTURA CLIENTE: aplicar un formato de fecha: dd/mm/yyyy.
    Cambiar la función predeterminada del campo NUMERO FACTURA CLIENTE a RECUENTO.
    Ocultar los campos: FECHA FACTURA CLIENTE y ZONA.

2. Ir a la vista informe e insertar una tabla que de cada CLIENTE muestre: RECUENTO DEL NUMERO FACTURA CLIENTE, SUMA IMPORTE CLIENTE, % DEL TOTAL GENERAL SOBRE LA SUMA DEL IMPORTE CLIENTE. Cambiar en dicha tabla el nombre de los siguientes campos:

    RECUENTO DE NUMERO FACTURA CLIENTE: TOTAL FACTURAS
    SUMA DE IMPORTE CLIENTE: TOTAL CLIENTE
    % TG SUMA DE IMPORTE CLIENTE: % TOTAL CLIENTE

3. Ordenar la tabla por el campo TOTAL FACTURAS de menor a mayor. Insertar una tabla que cuente en cada PROVINCIA el número diferente de CLIENTES que hay (APLICAR AL CAMPO CLIENTE EL RECUENTO DISTINTIVO). Cambiar el campo RECUENTO CLIENTE por NUM CLIENTES.

 4. Insertar una matriz, que muestre:

    FILA: CONCEPTO
    COLUMNA: TIPO
    VALORES: RECUENTO DE NUMERO FACTURA CLIENTE

Guardar los cambios y cerrar el fichero.


### Practica 3: Modificar el nombre de los otros dos campos de valores de la tabla:

    PROMEDIO DE DURACION: mostrarlo como MEDIA HORAS
    % TG SUMA DE DURACION: mostrarlo como % HORAS

### Practica 4: Abrir el fichero de Power BI BD FACTURAS.

1. Seleccionar la tabla de clientes y cambiar los siguientes formatos:

    Poner los encabezados en negrita y centrados.
    Poner los valores en cursiva.
    Poner en la fila de totales el texto: TOTALES CLIENTE

2. Seleccionar la tabla de clientes y cambiar los siguientes formatos:

    Seleccionar la matriz y cambiar los siguientes formatos:
    Poner los encabezados de columna en negrita.
    Poner los encabezados de fila en negrita y cursiva.
    Filtrar los informes de la página por la provincia de ALICANTE.

Guardar los cambios y cerrar el fichero.

### Practica 5: 

1. Abrir el fichero BD FACTURAS e ir a la vista informe.

2. Agregar una nueva página de informe y nombrarla como GRAFICOS. Insertar un gráfico de barras 100 % apiladas que muestre:

    EJE Y: CONCEPTO
    EJE X: RECUENTO DE NUMERO FACTURA CLIENTE
    LEYENDA: SECTOR

3. Mostrar las etiquetas de datos.

4. Insertar un gráfico de anillos que muestre:

    LEYENDA: SECTOR
    VALORES: RECUENTO DE NUMERO FACTURA CLIENTE

5. Cambiar el color del segmento CONTRUCCION a color GRIS

6. Insertar una tarjeta que haga el RECUENTO DE NUMERO FACTURA CLIENTE.

    Cambiar el texto de la etiqueta por TOTAL FACTURAS.
    Dar un color de fondo azul y una sombra amarilla.

7. Insertar una segmentación de datos del campo PROVINCIA y filtrar por la provincia de MADRID.

Guardar los cambios y cerrar el fichero.

### Practica 6: 


### Practica 7: 


---

## 🎓 Certificación
Este curso fue concluido exitosamente y cuento con el **certificado oficial de Santander Open Academy**, el cual forma parte de mi **portafolio de herramientas de análisis de datos**.  
