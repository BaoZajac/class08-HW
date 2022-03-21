import csv
import sys
import os


# sprawdzenie danych wejściowych z std
plik_wejsciowy = sys.argv[1]
if not os.path.isfile(plik_wejsciowy):
    print("Podano błądny plik wejściowy")
    print("Dostępne pliki w bieżącym katalogu:")
    pliki = os.system(("ls"))

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

    # zapisanie do pliku csv
    plik_exit = sys.argv[1]
    with open("plik.csv", "w") as f:
        writer = csv.writer(f)
        for linia in lista:
            writer.writerow(linia)   #TODO: jak pozbyć się tych zbędnych enterów wewnątrz pliku?

