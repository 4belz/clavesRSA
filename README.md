# 🛠️ Generador y Encriptador RSA 🔐

Este proyecto implementa un generador de claves RSA y funciones para encriptar y desencriptar mensajes. Está compuesto por tres scripts en Python:

- `generador_claves_rsa.py`: Genera claves pública y privada RSA.
- `encriptar_mensaje.py`: Encripta un mensaje utilizando una clave pública RSA.
- `desencriptar_mensaje.py`: Desencripta un mensaje utilizando una clave privada RSA.

## ✨ Características

- 🔢 Generación de números primos pequeños para las claves RSA.
- 🗝️ Creación de claves pública y privada RSA.
- 🔄 Conversión de mensajes a su representación ASCII para el proceso de encriptación.
- 🔒 Encriptación de mensajes utilizando la clave pública.
- 🔓 Desencriptación de mensajes utilizando la clave privada.

## 🛠️ Instalación

Para utilizar este proyecto, sigue estos pasos:

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/generador_encriptador_rsa.git
Navega al directorio del proyecto:
sh
Copiar código
cd generador_encriptador_rsa
Asegúrate de tener Python 3.x instalado en tu sistema.
🚀 Uso
Generar Claves RSA
Ejecuta el script generador_claves_rsa.py para generar una clave pública y una clave privada:
sh
Copiar código
python generador_claves_rsa.py
Esto imprimirá en la terminal las claves pública y privada generadas.
Encriptar un Mensaje
Ejecuta el script encriptar_mensaje.py:
sh
Copiar código
python encriptar_mensaje.py
Introduce el mensaje que deseas encriptar cuando se te pida.
Introduce la clave pública en el formato (e, n), por ejemplo (135, 125).
El mensaje encriptado se mostrará en la terminal.
Desencriptar un Mensaje
Ejecuta el script desencriptar_mensaje.py:
sh
Copiar código
python desencriptar_mensaje.py
Introduce el mensaje encriptado en formato de lista, por ejemplo [456, 45, 454, 687].
Introduce la clave privada en el formato (d, n), por ejemplo (135, 125).
El mensaje desencriptado se mostrará en la terminal.
📝 Ejemplos
Generar Claves
sh
Copiar código
python generador_claves_rsa.py
Salida esperada:

yaml
Copiar código
Clave publica: (e, n)
Clave privada: (d, n)
Encriptar Mensaje
sh
Copiar código
python encriptar_mensaje.py
Entrada:

yaml
Copiar código
Escribe el mensaje: Hola
Introduce la clave publica en formato (135, 125) por ejemplo: (17, 3233)
Salida esperada:

yaml
Copiar código
El mensaje en ascii es: [72, 111, 108, 97]
El mensaje encriptado con la clave publica (17, 3233) es: [2201, 3183, 1934, 1730]
Desencriptar Mensaje
sh
Copiar código
python desencriptar_mensaje.py
Entrada:

yaml
Copiar código
Introduce el mensaje encriptado en formato lista, por ejemplo [456, 45, 454, 687] : [2201, 3183, 1934, 1730]
Introduce la clave privada en formato (135, 125) por ejemplo: (2753, 3233)
Salida esperada:

css
Copiar código
El mensaje desencriptado sería: Hola
🤝 Contribuciones
¡Contribuciones son bienvenidas! Siéntete libre de abrir issues y enviar pull requests. Para grandes cambios, por favor abre un issue primero para discutir lo que te gustaría cambiar.

Haz un fork del proyecto.
Crea una rama con tu nueva funcionalidad (git checkout -b mi-nueva-funcionalidad).
Haz commit de tus cambios (git commit -am 'Añadí mi nueva funcionalidad').
Haz push a la rama (git push origin mi-nueva-funcionalidad).
Abre un Pull Request.
📜 Licencia
Este proyecto está licenciado bajo la Licencia MIT - mira el archivo LICENSE para más detalles.

✍️ Autores
BelDev4 - Trabajo inicial
🖥️ Requisitos del sistema
Sistema Operativo: Windows, macOS, Linux.
Python 3.10
📬 Contacto
Si tienes alguna pregunta, no dudes en abrir un issue o contactar a los autores del proyecto.