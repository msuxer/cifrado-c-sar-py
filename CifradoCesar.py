def cifrado_cesar(mensaje, desplazamiento):
    cifrado = ""
    # Recorremos el mensaje letra por letra
    for letra in mensaje:
        # Si la letra es una letra mayúscula, la ciframos
        if letra.isupper():
            cifrado += chr((ord(letra) + desplazamiento - 65) % 26 + 65)
        # Si la letra es una letra minúscula, la ciframos
        elif letra.islower():
            cifrado += chr((ord(letra) + desplazamiento - 97) % 26 + 97)
        # Si la letra no es una letra, la dejamos tal cual
        else:
            cifrado += letra
    return cifrado

def descifrado_cesar(mensaje, desplazamiento):
    descifrado = ""
    # Recorremos el mensaje letra por letra
    for letra in mensaje:
        # Si la letra es una letra mayúscula, la desciframos
        if letra.isupper():
            descifrado += chr((ord(letra) - desplazamiento - 65) % 26 + 65)
        # Si la letra es una letra minúscula, la desciframos
        elif letra.islower():
            descifrado += chr((ord(letra) - desplazamiento - 97) % 26 + 97)
        # Si la letra no es una letra, la dejamos tal cual
        else:
            descifrado += letra
    return descifrado

# Pedimos al usuario que elija entre cifrar o descifrar
opcion = input("¿Quieres cifrar o descifrar un mensaje? (cifrar/descifrar): ")

# Pedimos el mensaje y el desplazamiento por cifrado al usuario
palabra = input("Introduce el mensaje que quieres cifrar/descifrar: ")
desplazamiento = int(input("Introduce el desplazamiento por cifrado: "))

# Realizamos el cifrado o descifrado según la opción elegida por el usuario
if opcion == "cifrar":
    resultado = cifrado_cesar(mensaje, desplazamiento)
    print("El mensaje cifrado es:", resultado)
elif opcion == "descifrar":
    resultado = descifrado_cesar(mensaje, desplazamiento)
    print("El mensaje descifrado es:", resultado)
else:
    print("Opción inválida. Por favor, introduce 'cifrar' o 'descifrar'.")
