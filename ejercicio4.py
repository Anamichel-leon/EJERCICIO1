import math

#pedir el radio del circulo
radio = float(input("Introduce el radio del círculo en metros:\n"))

#Calcular el area del círculo
area = math.pi * (radio**2)

#Mostrar el resultado
print(f"\nEl area del círculo con radio {radio} metro es: {area:.2f} metros cuadrados.")