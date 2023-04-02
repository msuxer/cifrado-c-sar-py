def cifrar(mensaje, desplazamiento):
    cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            cifrado += chr((ord(letra) + desplazamiento - 65) % 26 + 65)
        else:
            cifrado += letra
    return cifrado

def descifrar(mensaje, desplazamiento):
    descifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            descifrado += chr((ord(letra) - desplazamiento - 65) % 26 + 65)
        else:
            descifrado += letra
    return descifrado

opcion = input("¿Quieres cifrar o descifrar un mensaje? (cifrar/descifrar): ")
desplazamiento = int(input("Introduce el número de desplazamientos: "))
mensaje = input("Introduce el mensaje: ")

if opcion == "cifrar":
    resultado = cifrar(mensaje, desplazamiento)
    print("El mensaje cifrado es:", resultado)
elif opcion == "descifrar":
    resultado = descifrar(mensaje, desplazamiento)
    print("El mensaje descifrado es:", resultado)
else:
    print("Opción inválida. Por favor, introduce 'cifrar' o 'descifrar'.")
