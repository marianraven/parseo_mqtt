from mqtt_parser import analizar

def main():
    # Leer código desde un archivo de entrada
    with open('entrada.txt', 'r') as archivo:
        codigo = archivo.read()
    
    # Analizar el código
    resultado = analizar(codigo)
    if resultado:
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()