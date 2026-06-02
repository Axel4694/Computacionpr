def nombre_de_la_funcion(parametro1, parametro2):
    """
    Documentación de la función (opcional pero recomendado)
    Explica qué hace la función y qué parámetros espera
    """
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado # Opcional: devuelve un valor

def saludar(nombre):
    """
    Muestra un saludo personalizado

    Args:
        nombre (str): El nombre de la persona a saludar

    Returns:
        str: Un mensaje de saludo
    """
    mensaje = f"¡Hola, {nombre}! Veo que tienes 17 y vives en Torreón ¡Bienvenido!."
    return mensaje


# Llamando a la función
print(saludar("santi")) 