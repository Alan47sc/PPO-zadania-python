print("**Konwerter Temperatur (Celsjusz <-> Fahrenheit)**")

wybor = input("""Wybierz rodzaj konwersji: 
C - Stopnie Celsjusza na Fahrenheita
F - Stopnie Fahrenheita na Celsjusza
: """)

if wybor == "C" or wybor == "c":
    celsjusz = float(input("Podaj temperaturę w skali Celsjusza: "))
    print(celsjusz, "°C to", celsjusz * 1.8 + 32, "°F.")

elif wybor == "F" or wybor == "f":
    fahren = float(input("Podaj temperaturę w skali Fahrenheita: "))
    print (fahren, "°F to",(fahren - 32)/1.8, "°C.")

else:
    print("Nieprawidłowy wybór.")