def limpiar_texto(cadena):

    # Convertir a minúsculas
    cadena = cadena.lower()

    # Eliminar espacios al inicio y final
    cadena = cadena.strip()

    # Reemplazar múltiples espacios por uno solo
    cadena = " ".join(cadena.split())

    # Capitalizar la primera letra
    cadena = cadena.capitalize()

    return cadena


# Ejemplo
texto = " hola MUNDO "
print(limpiar_texto(texto))