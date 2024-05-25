


def desencriptar_mensaje(clave_priv, mensaje_encriptado):
    """Desencripta el mensaje encriptado utilizando la clave privada."""
    
    d, n = clave_priv
    mensaje_desencriptado = []

    for num_encriptado in mensaje_encriptado:
        num_desencriptado = pow(num_encriptado, d, n)
        mensaje_desencriptado.append(chr(num_desencriptado))

    return ''.join(mensaje_desencriptado)


mensaje_entrada = input("Introduce el mensaje encriptado en formato lista, por ejemplo [456, 45, 454, 687] : ")
mensaje_encriptado = [int(num) for num in mensaje_entrada.strip('[]').split(',')]

# Obtener clave privada como una tupla de enteros
clave_privada_entrada = input("Introduce la clave privada en formato (135, 125) por ejemplo: ")
clave_privada = tuple(int(num) for num in clave_privada_entrada.strip('()').split(','))

# Desencriptar mensaje e imprimirlo
print("El mensaje desencriptado sería:", desencriptar_mensaje(clave_privada, mensaje_encriptado))