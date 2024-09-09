import subprocess

command = ["cmd", "/c", "dir"]

try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)

    print("Salida del comando:")
    print(result.stdout)

    if result.stderr:
        print("Error:")
        print(result.stderr)

except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando: {e}")
    print(f"Código de retorno: {e.returncode}")
