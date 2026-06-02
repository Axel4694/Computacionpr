# Pedir palabras al usuario
sustantivo = input("Ingresa un sustantivo: ")
verbo = input("Ingresa un verbo: ")
adjetivo = input("Ingresa un adjetivo: ")
lugar = input("Ingresa un lugar: ")

# Crear oración con f-string
oracion = f"El {sustantivo} {verbo} {adjetivo} en el {lugar}."

# Mostrar resultado
print(oracion)