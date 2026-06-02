# Pedir peso en kilogramos
peso = float(input("Ingresa tu peso en kg: "))

# Pedir estatura en metros
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular IMC
imc = peso / (estatura * estatura)

# Mostrar resultado con 2 decimales
print(f"Tu IMC es: {imc:.2f}")