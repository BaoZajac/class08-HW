import csv
import sys
import os


# sprawdzenie danych wejściowych z std
plik_wejsciowy = sys.argv[1]
# if not os.path.exists(plik_wejsciowy) or ...:   #TODO: napisać warunek
# #     print("Podano błądny plik wejściowy")
# #     print("Podany plik wejściowy nie istnieje")
# # elif...:
# #     print("Podano błędny plik wejściowy (folder, a nie plik")
# else:
#     print("Podany plik wejściowy to:", plik_wejsciowy)

# rozszerzenie_pliku = plik_wejsciowy.


# otwieranie pliku csv
lista = []
print("wersja pierwotna:")
with open(plik_wejsciowy, "r") as f:
    reader = csv.reader(f)
    for line in reader:
        lista.append(line)

print(lista)

# modyfikacja pliku csv
print("modyfikacja:")
for idx in sys.argv[3:]:
    Y, X, wartosc = idx.split(",")
    lista[int(Y)][int(X)] = wartosc

print(lista)

# zapisanie do pliku
plik_exit = sys.argv[1]
with open("plik.csv", "w") as f:
    writer = csv.writer(f)
    for linia in lista:
        writer.writerow(linia)
