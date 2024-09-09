import re

text = "Hola Mundo, este es un ejemplo usand la libreria re de Python."

pattern = r"mundo"

match = re.search(pattern, text, re.IGNORECASE)

if match:
    print(f"Se encontró '{match.group()}' en la posición: {match.start()}")
else:
    print("No se encontró la palabra 'mundo'")
