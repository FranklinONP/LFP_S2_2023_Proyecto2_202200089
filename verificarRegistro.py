def verificar_string(cadena):
    # Verificar si la cadena comienza y termina con llaves
    if cadena.startswith("{") and cadena.endswith("}"):
        # Eliminar las llaves del principio y del final
        cadena = cadena[1:-1]
        
        # Dividir la cadena por comas
        elementos = cadena.split(",")
        
        # Verificar la cantidad de elementos
        if len(elementos) == 5:
            # Verificar las condiciones de cada elemento
            if elementos[0].strip().isdigit() and any(caracter.isalpha() for caracter in elementos[1].strip()[1:-1]) and any(caracter.isdigit() or caracter.replace('.', '', 1).isdigit() for caracter in elementos[2].strip()) and any(caracter.isdigit() or caracter.replace('.', '', 1).isdigit() for caracter in elementos[3].strip()) and any(caracter.isdigit() for caracter in elementos[4].strip()):
                return True
    
    return False

# Ejemplo de uso
cadena1 = '{1, 33"Barbacoa", @10.50,? 20.00,h 6}'
cadena2 = '{7,"ddffd"6, 87,8hgjjfg,k9k}'
c3='{4, "Mostaza", 14.00, 16.0.0, 8}'

print(verificar_string(cadena1))  # True
print(verificar_string(cadena2))  # False
print(verificar_string(c3))