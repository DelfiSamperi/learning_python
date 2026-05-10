temperatura = float(input("Ingrese temperatura: "))
escala = input("Es Fahrenheit(F) o Celcius(C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print("Equivale a ", celsius, "en escala Celsius.")
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print("Equivale a ", fahrenheit, "en escala Fahrenheit.")
else:
    print("Escala incorrecta")

