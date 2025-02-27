import subprocess

def interactuar():
    print(":) Bienvenido al menú de programas implementados. .:( ")

    while True:
        print("\n************* MENÚ DE PROGRAMAS ***************")
        print("\n¿Qué programas deseas visualizar?")
        print("1. Programas imprimir Datos.")
        print("2. Entradas de datos.")
        print("3. Entrada de datos suma")
        print("4. Ejercicio de resta y multiplicación.")
        print("5. Calcular el Área de un radio")
        print("6. Numeros mayor ")
        print("7. Nmero par o impar")
        print("8. Mayor que 10 menor que 10")
        print("9. Numero positivo y negativo ")
        print("10. Numero Aleatorio")
        print("11. Ingrese la calificacion")
        print("12. Ejercicio Ingresar el nombre ")
        print("13. Ticket de compra")
        print("14. Datos temperatura")
        print("15. Simulando un proceso de toma de desiciones")
        print("16. Simulando un sistema multiagente basico")
        print("17. Papel de la heuristica")
        print("18. Algoritmos de exploracion DFS")
        print("19. Algoritmos de exploracion BFS")
        print("20. Algoritmo A")
        print("21. Algoritmo local")
        print("22. Salir")

        opcion = input("Selecciona una opción (1-22): ")
       

        if opcion == "1":
            print("Ejecutando el archivo Ejercicio1.py...\n")
            print("\n************* :) PROGRAMA EJECUTADO CORRECTAMENTE :) ***************")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\EJERCICIO2Declarar variables.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        
        if opcion == "2":
            print("Ejecutando el archivo Ejercicio2.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\entrada de Datos suma.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")


        if opcion == "3":
            print("Ejecutando el archivo Ejercicio5.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\EJERCICIO.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")


        if opcion == "4":
            print("Ejecutando el archivo Ejercicio4.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\restaymultiplicacion.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        

        if opcion == "5":
            print("Ejecutando el archivo Ejercicio5.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio4.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "6":
            print("Ejecutando el archivo Ejercicio6.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio7.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "7":
            print("Ejecutando el archivo Ejercicio7.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\EJERCICIO8.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "8":
            print("Ejecutando el archivo Ejercicio8.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio10.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        
        if opcion == "9":
            print("Ejecutando el archivo Ejercicio9.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio11.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "10":
            print("Ejecutando el archivo Ejercicio10.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio12.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "11":
            print("Ejecutando el archivo Ejercicio11.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio14.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "12":
            print("Ejecutando el archivo Ejercicio12.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\EJERCICIO15.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "13":
            print("Ejecutando el archivo Ejercicio13.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejer15.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "14":
            print("Ejecutando el archivo Ejercicio14.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejercicio333.py"], check=True)
              
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")


        if opcion == "15":
            print("Ejecutando el archivo Ejercicio15.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\Ejercicio4simulandounproceso.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        if opcion == "16":
            print("Ejecutando el archivo Ejercicio16.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\ejerciciosimulandounsistemamultiagente.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        if opcion == "17":
            print("Ejecutando el archivo Ejercicio17.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\algoritmosdeexploración.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        
        if opcion == "18":
            print("Ejecutando el archivo Ejercicio18.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\algoritmosdeexploración.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        
        if opcion == "19":
            print("Ejecutando el archivo Ejercicio19.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\algoritmosdeexploraciondealternativas.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        if opcion == "20":
            print("Ejecutando el archivo Ejercicio20.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\Algoritmo A.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        
        if opcion == "21":
            print("Ejecutando el archivo Ejercicio21.py...\n")
            try:
                subprocess.run(["python", r"C:\Users\anale\Documents\8US\INTELIGENCIA ARTIFICIAL\CODIGO\algoritmolocal.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

        
        elif opcion == "22":
            print("¡Hasta Luego :)!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamar a la función para ejecutar el menú
interactuar()
