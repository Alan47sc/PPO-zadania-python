wyborZadania = int(input("""Wybierz zadanie do którego chcesz przejść:
1. Prosty kalkulator dwóch liczb
2. Konwerter temperatur (Celsjusz <-> Fahrenheit)
3. Kalkulator średniej ocen ucznia
: """))

match wyborZadania:
    case 1:
        print("Prosty Kalkulator Dwóch Liczb")

        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        print("""Co chcesz zrobić z podanymi liczbami:
        1. Dodać
        2. Odjąć
        3. Pomnożyć
        4. Podzielić """)

        wybor = int(input())

        if wybor == 1:
            print(liczba1, " + ", liczba2, " = ", liczba1 + liczba2)
        elif wybor == 2:
            print(liczba1, " - ", liczba2, " = ", liczba1 - liczba2)
        elif wybor == 3:
            print(liczba1, " * ", liczba2, " = ", liczba1 * liczba2)
        elif wybor == 4 and liczba2 != 0:                               #Brak dzielenia przez 0
            print(liczba1, " / ", liczba2, " = ", liczba1 / liczba2)
        else:
            print("Nieprawidłowy wybór.")

    case 2:
        print("Konwerter Temperatur (Celsjusz <-> Fahrenheit)")

        wybor = input("""Wybierz rodzaj konwersji: 
            C - Stopnie Celsjusza na Fahrenheita
            F - Stopnie Fahrenheita na Celsjusza
            : """)

        if wybor == "C" or wybor == "c":
            celsjusz = float(input("Podaj temperaturę w skali Celsjusza: "))
            print(celsjusz, "°C to", celsjusz * 1.8 + 32, "°F.")                #Obliczenia w print statemencie dla kompaktowości kodu

        elif wybor == "F" or wybor == "f":
            fahren = float(input("Podaj temperaturę w skali Fahrenheita: "))
            print(fahren, "°F to", (fahren - 32) / 1.8, "°C.")

        else:
            print("Nieprawidłowy wybór.")

    case 3:
        print("Kalkulator Średniej Ocen")

        n = int(input("Podaj liczbę ocen do wprowadzenia: "))
        oceny = []

        for i in range(n):
            wpis = float(input("Podaj kolejno oceny: "))
            oceny.append(wpis)

        srednia = sum(oceny) / n        #Średnia w zmiennej dla zwiększenia czytelności

        if 3 <= srednia <= 6:       #Średnia maksymalnie może wynosić 6
            print("średnia ocen ucznia:", sum(oceny) / n)
            print("Uczeń zdał")

        elif  1 <= srednia < 3:     #Średnia minimalna może wynieść 1
            print("Średnia ocen ucznia:", sum(oceny) / n)
            print("Uczeń nie zdał.")

        else:
            print("Niepoprawne dane.")


