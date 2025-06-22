from faker import Faker
import openpyxl
import os

fake = Faker('es_ES')

columnas = ['id', 'nombre', 'edad', 'email', 'telefono']  # Encabezados del Excel

# Crear un libro y una hoja de Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Registros"

# Escribir encabezados
ws.append(columnas)

# Escribir los registros ficticios
for i in range(1, 51):
    nombre = fake.name()
    edad = fake.random_int(min=18, max=65)
    email = fake.email()
    telefono = fake.phone_number()
    ws.append([i, nombre, edad, email, telefono])

# Guardar el archivo en la misma carpeta
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_xlsx = os.path.join(directorio_actual, 'registros_ficticios.xlsx')
wb.save(ruta_xlsx)

print(f'Archivo Excel creado en: {ruta_xlsx}')