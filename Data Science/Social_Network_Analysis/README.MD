# 📘 Practica Introductoria – Social Network Analysis

Esta práctica introductoria de la materia **Data Science** fue desarrollada en Google Colab utilizando el libro *Data Science from Scratch* como referencia.  

El objetivo principal fue aplicar estructuras de datos en Python para resolver preguntas relacionadas con una pequeña red social ficticia de empleados.  

---

## 📝 Preguntas resueltas

1. **¿Cuántos amigos tienen Kata, Thor, Chi y Clive?**  
   
kate_friends = number_of_friends(users[8]) # ID de Kate es 8
thor_friends = number_of_friends(users[4]) # ID de Thor es 4
chi_friends = number_of_friends(users[3])  # ID de Chi es 3
clive_friends = number_of_friends(users[5]) # ID de Clive es 5

print(f"Kate tiene {kate_friends} amigos.")
print(f"Thor tiene {thor_friends} amigos.")
print(f"Chi tiene {chi_friends} amigos.")
print(f"Clive tiene {clive_friends} amigos.")

➡️ Cada usuario tiene un conteo de amigos calculado automáticamente.

2. **¿Cuál empleado es el más popular?**

most_popular_user_id, most_popular_num_friends = num_friends_by_id[0]

most_popular_user_name = None
for user in users:
    if user["id"] == most_popular_user_id:
        most_popular_user_name = user["name"]
        break

print(f"El empleado más popular es: {most_popular_user_name} con {most_popular_num_friends} amigos.")

➡️ El empleado con más conexiones en la red social.

3. **¿Cuántos amigos tiene Klein que conozca Chi?**

# Amigos de Klein (id 9)
klein_friends = friendships[9]

# Amigos de Chi (id 3)
chi_friends = friendships[3]

# Encuentra los amigos en común encontrando la intersección de las dos listas.
mutual_friends = set(klein_friends).intersection(chi_friends)

num_mutual_friends = len(mutual_friends)

print(f"Klein and Chi tienen {num_mutual_friends} amigo(s) mutuos.")

➡️ Obtenemos cuantos amigos en común tienen Klein y Chi a traves de la intersección de las 2 listas de amigos

4. **¿Cuáles son los 3 intereses más frecuentes en los empleados?**

top_3_interests = words_and_counts.most_common(3)

print("Top 3 intereses de los empleados:")
for interest, count in top_3_interests:
  print(f"{interest}: {count}")

➡️ Se obtienen los 3 interes que más se repiten entre los empleados 

5. **¿Cuales son los 3 empleados con el mejor salario? ¿Qué tienen en común?**

Para resolver este ejercicio se hizo lo siguiente 

- Combinar datos: Combinar los datos de users con salaries_and_tenures para que cada usuario tenga el salario y su tenencia

user_salary_tenure = []
for i, user in enumerate(users):
  salary, tenure = salaries_and_tenures[i]
  user_salary_tenure.append({
      "id": user["id"],
      "nombre": user["name"],
      "salario": salary,
      "tenura": tenure
  })

display(user_salary_tenure)

- Organizar por salario: Ordenar los datos por salario en orden descendente para obtener los empleados con el salario más alto

user_salary_tenure.sort(key=lambda x: x['salario'], reverse=True)
display(user_salary_tenure)

top_3_employees = user_salary_tenure[:3]
display(top_3_employees)

- Obtener los intereses: Obtener los intereses de los 3 empleados con el salario mas alto de  `interests`

top_3_employee_interests = []
for employee in top_3_employees:
  employee_id = employee["id"]
  for interest in interests:
    if interest[0] == employee_id:
      top_3_employee_interests.append(interest)

display(top_3_employee_interests)

- Obtener los intereses comúnes: Analizar los intereses de cada uno de los 3 empleados y ver que tienen en común

interest_strings = [interest[1] for interest in top_3_employee_interests]
interest_counts = Counter(interest_strings)

common_interests = {interest: count for interest, count in interest_counts.items() if count > 1}

print("Intereses comunes entre los 3 empleados:")
for interest, count in common_interests.items():
    print(f"{interest}: {count}")

print("Los 3 empleados con el salario más alto:")

for employee in top_3_employees:
    print(f"Nombre: {employee['nombre']}, ${employee['salario']}")

print("\nIntreses en común:")

if common_interests:
    for interest, count in common_interests.items():
        print(f"{interest}: {count}")
else:
    print("No se encontraron intereses en común.")


➡️  Los 3 empleados con el salario más alto son Dunn ($88,000), Hero ($83,000), y Devin ($83,000).
    Dentro de los 3 empleados lo único en común que tienen es "HBase" que solo a 2 empleados les gusta


## 🛠️ Herramientas y conceptos aplicados

- Google Colab para la ejecución de código.

- Python como lenguaje principal.

- Uso de listas, diccionarios y estructuras de datos para simular redes sociales.

- Counter de collections para ranking de intereses.


## 🎯 Aprendizaje

Esta práctica permitió reforzar:

- Pensamiento lógico y analítico en Python.

- Conceptos básicos de redes sociales y popularidad en análisis de datos.

- Introducción a cómo los datos de relaciones pueden responder preguntas clave en organizaciones.

