import os
from mqtt_parser import analizar

def main():
    ruta = os.path.join(os.path.dirname(__file__), 'entrada.txt')
    with open(ruta, 'r') as archivo:
        codigo = archivo.read()
    
    # Analizar el código
    resultado = analizar(codigo)
    if resultado:
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()