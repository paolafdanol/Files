nombre_archivo = input("Ingresa un nombre de archivo: ")

# Si el nombre del archivo es "na na boo boo", imprime un mensaje divertido y sale del programa
if nombre_archivo == "na na boo boo":
    print("NA NA BOO BOO PARA TI - Te he atrapado!")
else:
    # intenta abrir el archivo en modo lectura
    try:
        with open(nombre_archivo, 'r') as archivo:
            # inicializa el contador de líneas
            contador = 0
            # lee cada línea del archivo
            for linea in archivo:
                contador += 1

            # imprime el número de líneas en el archivo
            print("Hay", contador, "líneas de texto en el archivo", nombre_archivo)
    # maneja el error si el archivo no existe
    except FileNotFoundError:
        print("El archivo no puede ser abierto:", nombre_archivo)


