import math

# Definición de la función para calcular la circunferencia
def calcular_circunferencia(radio):
    pi = round(math.pi, 6)  # Determina trabajar con 6 decimales
    circunferencia = 2 * pi * radio # Fórmula para calcular la circunferencia
    return circunferencia

# Ejemplo de uso
radio = float(input("Ingrese el radio para calcular la circunferencia: "))  # Solicita al usuario que ingrese el valor del radio
resultado = calcular_circunferencia(radio) # Llamada a la función para calcular la circunferencia
print("La circunferencia es:", resultado) # Imprime el resultado por pantalla
