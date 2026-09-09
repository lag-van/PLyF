# En este programa se realizará la validación por medio de regex de las siguientes cadenas
#
# Correo Electronico
# Dato moneda
# Contraseña segura: 8 caracteres, 1 mayusula, 1 caracter especial, 1 numero
# Telefono con lada +52
# Nombre
# Matricula

import re

menu = """¿Qué cadena desea evaluar?
1. Correo Electronico
2. Dato moneda
3. Contraseña segura
4. Telefono con lada +52
5. Nombre
6. Matricula
7. Salir"""

def evaluacionCorreo():
    expresion = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2})?$"
    texto = input("Ingresa el correo a validar: ")

    if re.fullmatch(expresion, texto):
        return "El correo es válido"    
    return "El correo NO es válido"

def evaluacionMoneda():
    expresion = r"^\$?\d+\.\d{2}$"
    texto = input("Ingrese la cantidad a validar (los centavos son obligatorios, '$' es opcional): ")

    if re.fullmatch(expresion, texto):
        return "Cantidad válida"    
    return "Cantidad NO válida"

def evaluacionPass():
    expresion = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).{8,}$"
    texto = input("Valide si su contraseña es segura, esta debe contener"
    "\n8 caracteres, 1 mayusula, 1 caracter especial, 1 numero: \n\n")

    if re.fullmatch(expresion, texto):
        return "Contraseña Segura"    
    return "Contraseña NO Segura"

def evaluacionTel():
    expresion = r"^\+52[\s]?\d{10}$"
    texto = input("Valide su numero de telefono, debe tener lada +52, este SOLO puede tener un espacio despues de la lada: ")

    if re.fullmatch(expresion, texto):
        return "Número valido"    
    return "Número NO válido"

def evaluacionNombre():
    expresion = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}(?:\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,})*\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}$"
    texto = input("Valide su nombre completo: ")

    if re.fullmatch(expresion, texto):
        return "Nombre válido"    
    return "Nombre NO válido"

def evaluacionMatricula():
    expresion = r"^([01]\d|2[0-6])(\d{2})([0-2])((?!000)\d{3})$"
    texto = input("Valide su matricula: ")

    if re.fullmatch(expresion, texto):
        return "Matricula válida"    
    return "Matricula NO válida"

while True:
    print(menu)
    opcion = input("\n\n¿Qué desea hacer?:  ").strip()

    match opcion:
        case "1":
            print(evaluacionCorreo())
            input("\nPresione Enter para continuar...")
        case "2":
            print(evaluacionMoneda())
            input("\nPresione Enter para continuar...")
        case "3":
            print(evaluacionPass())
            input("\nPresione Enter para continuar...")
        case "4":
            print(evaluacionTel())
            input("\nPresione Enter para continuar...")
        case "5":
            print(evaluacionNombre())
            input("\nPresione Enter para continuar...")
        case "6":
            print(evaluacionMatricula())
            input("\nPresione Enter para continuar...")
        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida, intenta de nuevo.\n")



