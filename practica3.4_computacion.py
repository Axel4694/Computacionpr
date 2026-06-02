texto = "Python"

# Índices (comienzan en 0)
primer_caracter = texto[0]
segundo_caracter = texto[1]
ultimo_caracter = texto[-1]

# Slicing (rebanadas)
# sintaxis: [inicio:fin:paso]
primeras_tres = texto[0:3]
ultimos_tres = texto[-3:]
cada_segundo = texto[::2]
reverso = texto[::-1]

# Longitud de la cadena
longitud = len(texto)

texto = "Python"
texto[:3]
texto[3:]

def nombre_de_la_funcion(parametro1, parametro2):
    """
    Documentación de la función (opcional pero recomendado)
    Explica qué hace la función y qué parámetros espera
    """
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado


def saludar(nombre):
    """
    Muestra un saludo personalizado

    Args:
        nombre (str): El nombre de la persona a saludar

    Returns:
        str: Un mensaje de saludo
    """
    mensaje = f"¡Hola, {nombre}! Bienvenido al curso de Python."
    return mensaje


# Llamando a la función
print(saludar("Axel"))