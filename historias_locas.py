# Concatenar cadenas de caracteres
# Queremos crear una cadena que diga:
# Aprende a programar con _______ .

# organizacion = "freeCodeCamp"

# print("Aprende a programas con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") # f-string

# Mad Libs (Historias Locas)

adj = input("Ingresa un adjetivo: ")
verbo1 = input("Ingresa un verbo: ")
verbo2 = input("Ingresa un segundo verbo: ")
sustantivo_plural = input("Ingresa un sustantivo plural: ")

madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}."

print(madlib)