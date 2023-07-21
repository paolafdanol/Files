# pide al usuario el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo: ")

# intenta abrir el archivo en modo lectura
try:
    with open(nombre_archivo, 'r') as archivo:
        # lee cada línea del archivo
        for linea in archivo:
            # convierte la línea a mayúsculas y la imprime
            print(linea.upper())
# maneja el error si el archivo no existe
except FileNotFoundError:
    print("El archivo no existe.")

