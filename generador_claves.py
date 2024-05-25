import random
from math import gcd



def comprobar_primo(numero):

	"""Comprueba si el numero que le pasas es primo, si lo es devuelve TRUE sino FALSE"""

	primo = True
	for cont in range(2,numero):
		if numero % cont == 0:
			primo = False
  
	if primo:
		return True
	
	return False

##########################################################################################################################################################
	
def generar_primo_pequeno (num1, num2):

	"""Genera un numero primo aleatorio entre los numeros que le pases como parametros"""

	numero_aleatorio = random.randint(num1, num2)
	while not comprobar_primo(numero_aleatorio):
		numero_aleatorio = random.randint(num1, num2)
	return numero_aleatorio

##########################################################################################################################################################

def generar_claves():									# Funcion que devuelve dos tuplas que son inmutables primero la clave publica, y luego la clave privada
		
	# Generar primos p y q
    p = generar_primo_pequeno(10, 99)
    q = generar_primo_pequeno(10, 99)

    # Calcular n y phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Elegir e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calcular d (inverso multiplicativo de e mod phi(n))
    d = pow(e, -1, phi)

    # Devolver claves pública y privada en dos tuplas que son inmutables
    return "Clave publica: ", (e, n), "Clave privada", (d, n)


print(generar_claves())





