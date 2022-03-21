import csv
import sys
import os
import json
import pickle


# sprawdzenie danych wejściowych z std
plik_wejsciowy = sys.argv[1]
if os.path.splitext(plik_wejsciowy)[1] != ".csv":
    print("Błąd - nieobsługiwany typ pliku wejściowego")
elif not os.path.isfile(plik_wejsciowy):
    print("Podano błądny plik wejściowy")
    print("Dostępne pliki w bieżącym katalogu:")
    pliki = os.system("ls")

else:
    # otwieranie pliku csv
    lista = []
    with open(plik_wejsciowy, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            lista.append(line)

    # modyfikacja pliku csv
    for idx in sys.argv[3:]:
        Y, X, wartosc = idx.split(",")
        lista[int(Y)][int(X)] = wartosc

    # wyświetlenie na ekranie
    for element in lista:
        print(','.join(element))

    # zapisanie do pliku
    plik_exit = sys.argv[2]
    rozszerzenie_wyjscia = os.path.splitext(plik_exit)
    if rozszerzenie_wyjscia[1] == ".csv":
        with open(sys.argv[2], "w", newline="") as f:
            writer = csv.writer(f)
            for linia in lista:
                writer.writerow(linia)
    elif rozszerzenie_wyjscia[1] == ".json":
        with open(sys.argv[2], "w") as f:
            json.dump(lista, f)
    elif rozszerzenie_wyjscia[1] == ".pickle":
        with open(sys.argv[2], "wb") as f:
            pickle.dump(lista, f)
    else:
        print("Bład - zapis do nieobsługiwanego rozszerzenia pliku")
