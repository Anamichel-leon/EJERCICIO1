import random

numero_aleatorio = random.randint(1, 10)
adivina=input(input("Adivina el numero entre 1 y 10: "))
print(f"El número aleatorio es {numero_aleatorio}.")
if adivina == numero_aleatorio:
     print("¡Correcto1! Has adivinado el numero .")

else: print(f"Incorrecto. El número era {numero_aleatorio}.")

