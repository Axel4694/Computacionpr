# Pedir el nombre completo
nombre = input("Ingresa tu nombre completo: ")

# Obtener iniciales
palabras = nombre.split()
iniciales = ""

for palabra in palabras:
    iniciales += palabra[0].upper() + " "

# Mostrar diseño artístico
print("*************")
print(f"* {iniciales}*")
print("* *")
print("* *")
print("*************")