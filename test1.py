from mqtt_parser import analizar

def ejecutar_test(codigo, descripcion):
   print(f"\nEjecutando prueba: {descripcion}")
   try:
       resultado = analizar(codigo)
       if resultado is not None:
           print(f"Resultado: {resultado}")
   except Exception as e:
       print(f"Se produjo un error: {e}")

def main():
   # Código a analizar
   pruebas = [
       # Pruebas sin autenticación y encriptación
       ("CONECTAR MQTT dispositivo_1", "Conexión básica"),
       ("PUBLICAR mensaje_hola A topic_casa CON KEY \"saludo\"", "Publicar mensaje simple"),
       # Pruebas con autenticación
       ("AUTH \"usuario\" \"clave123\"", "Habilitar autenticación"),
       ("SUSCRIBIRSE A topic_casa", "Suscripción simple (con autenticación)"),
       # Prueba de encriptación
       ("ENCRIPTADO A true", "Habilitar encriptación"),
       ("PUBLICAR mensaje_hola A topic_secreto CON KEY \"clave\"", "Publicar mensaje encriptado"),
       ("ENCRIPTADO A false", "Deshabilitar encriptación"),
       ("PUBLICAR mensaje_adios A topic_casa CON KEY \"clave\"", "Publicar mensaje sin encriptación"),
   ]

   # Ejecutar todas las pruebas
   for codigo, descripcion in pruebas:
       ejecutar_test(codigo, descripcion)

if __name__ == "__main__":
   main()