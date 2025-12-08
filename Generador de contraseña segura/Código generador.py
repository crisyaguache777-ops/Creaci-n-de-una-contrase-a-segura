import random
import string

def generar_contrasena_segura():
    
    while True:
        try:
            cantCaracteres = int(input("Ingrese la **cantidad total de caracteres** que debe tener su contraseña: "))
            if cantCaracteres <= 0:
                print("La cantidad total debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    while True: # Estructura Repetitiva (Controla el reingreso de datos en caso de fallo de validación)
        print("\n--- Definición de Componentes ---")
        
        try:
            cantCaracteresEsp = int(input("Ingrese la cantidad de **caracteres especiales** (ej:!@#$) que necesita: "))
            cantMinus = int(input("Ingrese la cantidad de **letras minúsculas** que necesita: "))
            cantMayus = int(input("Ingrese la cantidad de **letras mayúsculas** que necesita: "))
            cantNum = int(input("Ingrese la cantidad de **números** (0-9) que necesita: "))

        except ValueError:
            print("\nError: Una de las entradas no fue un número válido. Inténtelo de nuevo.")
            continue 
        
        cantTotal = cantMayus + cantMinus + cantCaracteresEsp + cantNum
        
        if cantTotal == cantCaracteres: # Estructura Lógica (Validación)
            break
        else:
            print("\n🚨 ¡ATENCIÓN! La cantidad de caracteres que ingresaste **NO** concuerda con el total requerido.")
            print(f"Total requerido: {cantCaracteres}. Suma de componentes ({cantMayus}+{cantMinus}+{cantCaracteresEsp}+{cantNum}): {cantTotal}.")
            print("Por favor, inténtalo de nuevo para que la suma sea igual al total.")

    caracteres_especiales = string.punctuation
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    numeros = string.digits

    password_parts = []
    
    # Se utiliza una expresión generadora para garantizar la cuota exacta de cada tipo de carácter.
    password_parts.extend(random.choice(caracteres_especiales) for _ in range(cantCaracteresEsp))
    password_parts.extend(random.choice(letras_minusculas) for _ in range(cantMinus))
    password_parts.extend(random.choice(letras_mayusculas) for _ in range(cantMayus))
    password_parts.extend(random.choice(numeros) for _ in range(cantNum))
    
    # random.shuffle() es crucial para la seguridad, ya que mezcla los caracteres y elimina patrones.
    random.shuffle(password_parts) 
    
    contrasena_final = "".join(password_parts)

    print("\n✅ ¡Contraseña aleatoria creada! ✅")
    print(f"Su nueva contraseña segura es: **{contrasena_final}**")
    print(f"Longitud: {len(contrasena_final)}")


if __name__ == "__main__":
    generar_contrasena_segura()