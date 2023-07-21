# solicita al usuario el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo: ")

# inicializa la suma y el contador
suma = 0
contador = 0

# intenta abrir el archivo en modo lectura
try:
    with open(nombre_archivo, 'r') as archivo:
        # lee cada línea del archivo
        for linea in archivo:
            # verifica si la línea comienza con "X-DSPAM-Confidence:"
            if linea.startswith('X-DSPAM-Confidence:'):
                # extrae el número decimal de la línea
                confianza_spam = float(linea[linea.find(':')+1:].strip())
                # suma la confianza al total acumulado y aumenta el contador
                suma += confianza_spam
                contador += 1

    # imprime el valor medio de "spam confidence"
    if contador > 0:
        valor_medio = suma / contador
        print("El valor medio de spam confidence es:", valor_medio)
    else:
        print("No se encontraron líneas con 'X-DSPAM-Confidence:'")
# maneja el error si el archivo no existe
except FileNotFoundError:
    print("El archivo no existe.")
