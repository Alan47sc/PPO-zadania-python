print("**Prosty Kalkulator Dwóch Liczb**")

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

print("""Co chcesz zrobić z podanymi liczbami:
 1. Dodać
 2. Odjąć
 3. Pomnożyć
 4. Podzielić """)

wybor = int(input())

if wybor == 1:
    print(liczba1, " + ", liczba2, " = ", liczba1+liczba2)
elif wybor == 2:
    print(liczba1, " - ", liczba2, " = ", liczba1-liczba2)
elif wybor == 3:
    print(liczba1, " * ", liczba2, " = ", liczba1*liczba2)
elif wybor == 4:
    print(liczba1, " / ", liczba2, " = ", liczba1/liczba2)
else:
    print("Nieprawidłowy wybór.")



