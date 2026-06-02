# Variables para los ejemplos
nombre = "Axel"
edad = 18

# Formateo básico
saludo = f"Hola, me llamo {nombre} y tengo {edad} años"

# Expresiones dentro de f-strings
precio = 19.99
cantidad = 3
total = f"Total: {precio * cantidad:.2f}€"

# Llamadas a funciones
f"En mayúsculas: {nombre.upper()}"

# Alineación de texto
f"{nombre:>10}"
f"{nombre:^10}"
f"{nombre:<10}"