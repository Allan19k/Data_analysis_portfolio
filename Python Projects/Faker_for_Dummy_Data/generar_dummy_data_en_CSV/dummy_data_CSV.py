from faker import Faker
import csv
import os

fake = Faker('es_ES') # Generar datos en español

columnas = ['id', 'nombre', 'edad', 'email'] # Encabezados del CSV
# Generar 50 registros ficticios

registros = []
for i in range(1, 51):
    nombre = fake.name()
    edad = fake.random_int(min=18, max=65)
    email = fake.email()
    registros.append([i, nombre, edad, email])

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(directorio_actual, 'registros_ficticios.csv')

with open(ruta_csv, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(columnas)
    escritor.writerows(registros)

print(f'Archivo CSV creado en: {ruta_csv}')

