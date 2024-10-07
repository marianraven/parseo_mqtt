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
        # Pruebas de conexión y publicación
        ("CONECTAR MQTT dispositivo_1", "1-Conexión básica"),
        ("PUBLICAR mensaje_hola A topic_casa CON KEY \"saludo\"", "2-Publicar mensaje simple"),
        ("PUBLICAR mensaje_prueba A topic_prueba CON KEY \"clave\"", "3-Publicar mensaje de prueba con clave"),
        
        # Pruebas de suscripción , en la prueba 5, comienza con la suscripcion por defecto QOS 0, pero al indicarle qos 1, cambia la predeterminada
        ("SUSCRIBIRSE A topic_casa", "4-Suscripción simple a topico"),
        ("SUSCRIBIRSE A topic_prueba QoS 1", "5-Suscripción a topic_prueba con QoS 1"),
        
        # Pruebas de autenticación
        ("AUTH \"usuario1\" \"clave123\"", "6-Habilitar autenticación para usuario1, se indica usario y clave"),
        ("AUTH \"usuario2\" ", "7-Habilitar autenticación para usuario2, solo se indica usuario, por lo cual no es correcto que autentique"),
        
        # Pruebas de encriptación
        ("ENCRIPTADO A true", "8-Habilitar encriptación"),
        ("PUBLICAR mensaje_hola A topic_secreto CON KEY \"clave_secreta\"", "9-Publicar mensaje encriptado"),
        ("ENCRIPTADO A false", "10-Deshabilitar encriptación"),
        ("PUBLICAR mensaje_hola A topic_secreto CON KEY \"clave_secreta\"", "11-Publicar mensaje al quitar la encriptación, este es el mismo mensaje que la prueba 9, y comprueba el funcionamiento completo de la encriptacion"),
        
        # Pruebas de múltiples conexiones y mensajes
        ("CONECTAR MQTT dispositivo_2", "12-Conexión de dispositivo_2"),
        ("PUBLICAR mensaje_dos A topic_casa CON KEY \"clave2\"", "13-Publicar mensaje de dispositivo_2"),
        ("SUSCRIBIRSE A topic_casa QoS 2", "14-Dispositivo_2 suscrito a topic_casa con QoS 2"),
        
        # Pruebas de mensajes con QoS
        ("PUBLICAR mensaje_qos_1 A topic_casa QoS 1", "15-Publicar mensaje con QoS 1 a topico existente, la publicacion no tiene nivel de qos"),
        ("PUBLICAR mensaje_qos_2 A topic_casa QoS 2", "16-Publicar mensaje con QoS 2, no importa el nivel de qos en publicar, solo esta vigente en suscribir"),
        
        # Pruebas de reintentos
        ("PUBLICAR mensaje_fallido A topic_fallido QoS 5; REINTENTAR;", "17-Reintentar publicación en topic_fallido(NOTA: ESTA PRUEBA DEBE FALLAR, REINTENTAR NO ES UN TOKEN VALIDO, y QoS 5 TAMPOCO)"),
        
        # Pruebas de mensajes encriptados y autenticados
        ("AUTH \"admin\" \"supersecret\"", "18-Habilitar autenticación para admin"),
        ("ENCRIPTADO A true", "19-Habilitar encriptación para admin"),
        ("PUBLICAR mensaje_admin A topic_admin CON KEY \"admin_key\"", "20-Publicar mensaje admin en topic_admin"),
        

        # Pruebas de mensajes grupales
        ("PUBLICAR mensaje_grupal A topic_grupo CON KEY \"grupo_key\"", "21-Publicar mensaje grupal"),
        ("SUSCRIBIRSE A topic_grupo QoS 1", "22-Suscribirse a topic_grupo"),
        
        # Pruebas de autenticación y encriptación combinadas
        ("AUTH \"dispositivo_3\" \"clave_secreta3\"", "23-Habilitar autenticación para dispositivo_3"),
        ("ENCRIPTADO A true", "24-Habilitar encriptación para dispositivo_3"),
        ("PUBLICAR mensaje_secreto A topic_secreto CON KEY \"clave_secreta3\"", "25-Publicar mensaje secreto desde dispositivo_3"),
        
    ]

    # Ejecutar todas las pruebas
    for codigo, descripcion in pruebas:
        ejecutar_test(codigo, descripcion)

if __name__ == "__main__":
    main()
