#importa modulos originarios de python
import random
import string
#importar elemento de un modulo
from ahorcado.palabras import palabras
from ahorcado.ahorcado_diagramas import vidas_diccionario_visual

def get_valid_word(palabras):
    #seleccionar palabra al azar de la lista de palabras validas
    palabra = random.choice(palabras)

    #verificar que las palabras no tengan un caracter que no queremos
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("=================================")
    print("Bienvenidx al juego del Ahorcado!")
    print("=================================")

    palabra = get_valid_word(palabras)

    letras_adivinadas = set() # set guarda elemento sin repetir
    abecedario = set(string.ascii_uppercase) # no trae ñ
    letras_por_adivinar = set(palabra)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        

        #Mostrar estado actual de la palabra
        #list comprehension
        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]
        #Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        #si la letra no ha sido adivinada aun
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #si letra esta en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra {letra_usuario} no está en la palabra.")
        #si la letra ya habia sido ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Elije una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")    
    #cuando se adivinaron todas la letras de la palabra o se acabaron las vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print("Ahorcado! Perdiste... :(\n")
        print(f"La palabra era: {palabra}")
    else:
       print(f"Adivinaste! La palabra era {palabra}")
     
    
ahorcado() 

                    