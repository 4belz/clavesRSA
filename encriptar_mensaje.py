from generador_claves import generar_claves, generar_primo_pequeno, comprobar_primo



def mensaje_a_ASCII (mensaje):				# Convertir el mensaje a una lista de números (ASCII)
	
	mensaje_ascii = [] 						# Creamos lista vacia.

	for caracter in mensaje:
		valor_ascii = ord(caracter)				# la funcion ord() devuelve el valor Unicode de ese carcter
		mensaje_ascii.append(valor_ascii)
	
	return mensaje_ascii


####################################### Cifrado con Clave Pública C = Me mod n   ################################


def encriptar_mensaje (clave_pub, mensaje):			# Encripta el mensaje pasandole una clave publica y el mensaje en ASCII
	
	e, n = clave_pub
	mensaje_encriptado = []				# Creamos lista vacia.
	
	for numascii in mensaje:
		mensaje_encriptado.append(pow(numascii, e, n))
	
	return mensaje_encriptado





mensaje = input("Escribe el mensaje: ")

clave_publica_entrada = input("Introduce la clave publica en formato (135, 125) por ejemplo: ")
clave_publica = tuple(int(num) for num in clave_publica_entrada.strip('()').split(','))					 #convertimos la entrada que es un string en una tupla



print("El mensaje en ascii es: ", mensaje_a_ASCII(mensaje))

print(f"El mensaje encriptado con la clave publica {clave_publica} es: ", encriptar_mensaje(clave_publica, mensaje_a_ASCII(mensaje)))

#Imprimir por pantalla claves pública y privada