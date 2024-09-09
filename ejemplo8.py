import argparse

parser = argparse.ArgumentParser(description='Hola mundo de argparse')

parser.add_argument('nombre', type=str, help='Tu nombre')
parser.add_argument('edad', type=int, help='Tu edad')

args = parser.parse_args()

print(f"Hola {args.nombre}, tienes {args.edad} años.")
