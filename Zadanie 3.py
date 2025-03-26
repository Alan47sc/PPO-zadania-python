print("Kalkulator Średniej Ocen")

n = int(input("Podaj liczbę ocen do wprowadzenia: "))
oceny = []


for i in range(n):
    ocena = float(input("Podaj kolejno oceny: "))
    oceny.append(ocena)

srednia = sum(oceny)/n

if  3 <= srednia <= 6:
    print("średnia ocen ucznia:", sum(oceny)/n)
    print("Uczeń zdał")

elif srednia < 3:
    print("Średnia ocen ucznia:", sum(oceny)/n)
    print("Uczeń nie zdał.")

else:
    print("Niepoprawne dane.")
