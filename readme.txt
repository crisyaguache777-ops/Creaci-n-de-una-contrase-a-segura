Generador de Contraseñas Seguras

Información del Proyecto

Objetivo: Desarrollar una herramienta interactiva en Python que permita la creación de contraseñas personalizadas mediante la selección precisa de diferentes tipos de caracteres, garantizando la integridad de la estructura y la aleatoriedad del resultado final.

Fecha: 22 de diciembre de 2025

Lenguaje: Python 3.14.0

Librerías utilizadas: random, string

Institución: Universidad internacional del Ecuador

Materia: Lógica de programación

Funcionalidades Principales

Ingreso y Validación de Longitud: El programa solicita al usuario la cantidad total de caracteres. Implementa un bucle de control que solo permite avanzar si la entrada es un número entero positivo, gestionando errores de tipo de dato mediante excepciones.

Definición de Componentes: El usuario debe especificar la cantidad exacta de caracteres para cuatro categorías:

Caracteres especiales (puntuación y símbolos).

Letras minúsculas.

Letras mayúsculas.

Números.

Verificación Lógica de Coherencia: El sistema suma los componentes ingresados y los compara con el total definido inicialmente. Si las cifras no coinciden, el programa informa el error y solicita los datos nuevamente hasta que la suma sea exacta.

Generación Basada en Plantillas de String: Se utilizan las constantes de la librería "string" (ascii_lowercase, ascii_uppercase, digits y punctuation) para asegurar que se utilicen todos los caracteres estándar aceptados.

Mezcla de Caracteres (Shuffling): Una vez seleccionados los caracteres, se utiliza el método random.shuffle(). Esta función es crítica ya que desordena la lista de caracteres para que la contraseña no siga el orden en que fueron ingresados los datos, aumentando significativamente la seguridad ante ataques de diccionario.

Instrucciones de Uso
Ejecutar el script desde una terminal de Python.

Ingresar la longitud total deseada.

Desglosar dicha longitud entre los tipos de caracteres disponibles.

Al finalizar, el sistema mostrará la contraseña generada y confirmará la longitud final de la misma.




Elaborado por Cristopher Jeremías Yaguache, github: crisyaguache777-ops