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
        # ^: Indica el inicio de la cadena.
        # [a-zA-Z0-9._%+-]+: Nombre del correo, permite una o más letras, números y los caracteres . _ % + -.
        # @: Arroba obligatoria que separa el nombre del correo y el dominio.
        # [a-zA-Z0-9-]+: Dominio, formado por una o más letras, números o guiones.
        # \.: Punto literal que separa el dominio de la extensión.
        # [a-zA-Z]{2,}: Extensión obligatoria de al menos 2 letras.
        # (?:\.[a-zA-Z]{2})?: Grupo de no captura opcional para una segunda extensión de exactamente 2 letras.
        # $: Indica el final de la cadena.
    texto = input("Ingresa el correo a validar: ")

    if re.fullmatch(expresion, texto):
        return "El correo es válido"    
    return "El correo NO es válido"

def evaluacionMoneda():
    expresion = r"^\$?\d+\.\d{2}$"
        # ^: Indica el inicio de la cadena.
        # \$?: Signo de dólar literal opcional.
        # \d+: Parte entera formada por uno o más dígitos.
        # \.: Punto decimal literal obligatorio.
        # \d{2}: Centavos, formados por exactamente 2 dígitos.
        # $: Indica el final de la cadena.
    texto = input("Ingrese la cantidad a validar (los centavos son obligatorios, '$' es opcional): ")

    if re.fullmatch(expresion, texto):
        return "Cantidad válida"    
    return "Cantidad NO válida"

def evaluacionPass():
    expresion = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).{8,}$"
        # ^: Indica el inicio de la cadena.
        # (?=.*[A-Z]): Verifica que exista al menos una letra mayúscula.
        # (?=.*\d): Verifica que exista al menos un número.
        # (?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]): Verifica que exista al menos un carácter especial permitido.
        # .{8,}: Permite cualquier carácter y exige una longitud mínima de 8 caracteres.
        # $: Indica el final de la cadena.
    texto = input("Valide si su contraseña es segura, esta debe contener"
    "\n8 caracteres, 1 mayusula, 1 caracter especial, 1 numero: \n\n")

    if re.fullmatch(expresion, texto):
        return "Contraseña Segura"    
    return "Contraseña NO Segura"

def evaluacionTel():
    expresion = r"^\+52[\s]?\d{10}$"
        # ^: Indica el inicio de la cadena.
        # \+52: Lada +52 obligatoria; \+ representa el signo más literal.
        # [\s]?: Permite de manera opcional un espacio en blanco después de la lada.
        # \d{10}: Número telefónico formado por exactamente 10 dígitos.
        # $: Indica el final de la cadena.
    texto = input("Valide su numero de telefono, debe tener lada +52, este SOLO puede tener un espacio despues de la lada: ")

    if re.fullmatch(expresion, texto):
        return "Número valido"    
    return "Número NO válido"

def evaluacionNombre():
    expresion = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}(?:\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,})*\s[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}$"
        # ^: Indica el inicio de la cadena.
        # [a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}: Primer nombre, obligatorio, mínimo 3 letras.
        # (?: ... )*: Grupo de no captura repetido cero o más veces (*):
        # \s: Espacio en blanco separador.
        # [a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,}: Palabra intermedia con un mínimo de 2 letras (cubre "María", "De", "La").
        # \s[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}: Espacio final y el último apellido, obligatorio, mínimo 3 letras.
        # $: Indica el final de la cadena.
    texto = input("Valide su nombre completo: ")

    if re.fullmatch(expresion, texto):
        return "Nombre válido"    
    return "Nombre NO válido"

def evaluacionMatricula():
    expresion = r"^([01]\d|2[0-6])(\d{2})([0-2])((?!000)\d{3})$"
        # ^: Indica el inicio de la cadena.
        # ([01]\d|2[0-6]): Bloque de año de ingreso, permite valores desde 00 hasta 26.
        # (\d{2}): Segundo bloque formado por el numero de plantel,   2 dígitos.
        # ([0-2]): Tercer bloque, periodo, formado por un dígito entre 0 y 2.
        # ((?!000)\d{3}): Último bloque, numero de alumno de 3 dígitos, con la condición de que no sea 000.
        # $: Indica el final de la cadena.
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


