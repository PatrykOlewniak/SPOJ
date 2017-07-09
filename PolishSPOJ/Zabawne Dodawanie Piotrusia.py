"""
[Wejście]
Pierwsza linia wejścia zawiera liczbę t (t <= 80), określającą ile liczb znajduje się na kartce Piotrusia. Każda z następnych t linii zawiera dokładnie jedną liczbę naturalną n (1 <= n <= 80), dla której Piotruś musi wykonać obliczenia.

[Wyjście]
Dla kolejnych liczb podanych na kartce wypisz po jednej linijce zawierającej dwie liczby całkowite oddzielone spacją. Pierwsza oznacza palindrom otrzymany przez Piotrusia, druga -- liczbę dodawań wykonanych, by go otrzymać.

[Polecenie]
Piotruś w klasie na lekcji matematyki bardzo się nudził i pani postanowiła dać mu dodatkowe zadanie do rozwiązania. Piotruś otrzymał kartkę, na której napisane były małe liczby. Piotruś ma za zadanie stwierdzić, czy dana liczba jest palindromem (tzn. czy czyta się ją tak samo od lewej do prawej strony, jak od prawej do lewej). Jeżeli nie, Piotruś powinien dodać do siebie wartość liczby czytanej od lewej do prawej oraz wartość liczby czytanej od prawej do lewej, sprawdzić, czy suma jest palindromem, i jeżeli nie -- kontynuować proces, aż otrzyma palindrom.

Przykładowo, mając daną liczbę 28, Piotruś stwierdzi, że nie jest ona palindromem i wykona dodawanie 28 + 82 = 110. Liczba 110 wciąż nie jest palindromem, zatem Piotruś wykona jeszcze dodawanie 110 + 011 = 110 + 11 = 121. Wynik tego dodawania jest już palindromem, więc obliczenia zostaną zakończone.

Twoim zadaniem jest napisać program, który dla każdej liczby rozważanej przez Piotrusia wypisze palindrom (wynik obliczeń Piotrusia), oraz liczbę dodawań prowadzących do wyniku.

"""


import os

ileLiczb = int(raw_input())
tablicaLiczb = []

while (ileLiczb):
    wprowadzonaLiczba = raw_input()
    tablicaLiczb.append(str(wprowadzonaLiczba))
    ileLiczb = ileLiczb - 1

absolutely_unused_variable = os.system('cls')

# for k in range (0,len(tablicaLiczb)):
k = 0
while (k < len(tablicaLiczb)):

    def sprawdz(tablica):  # zwraca 0 jesli rowne
        nierowne = 0
        for k in range(0, (len(str(tablica))) - 1):
            tablica = str(tablica)
            if (tablica[k] != tablica[-k - 1]):
                # print "NIE rowne K: "+str(k) +" -k-1: "+str(-k-1)
                nierowne = nierowne + 1
        return nierowne


    # print sprawdz(tablicaLiczb[k])

    def dziesiatkowanie(wykladnik):
        liczba = 1
        while (wykladnik):
            liczba = liczba * 10
            wykladnik = wykladnik - 1
        return liczba


    def doLiczby(tablica):
        wartoscPo = 0
        for k in xrange(0, len(tablica)):
            wartoscPo = wartoscPo + int(int(tablica[k]) * dziesiatkowanie((len(tablica) - 1) - k))
        return wartoscPo


    dodawane = 0
    while (sprawdz(tablicaLiczb[k])):

        tablicaRobocza = []
        tablicaLiczb[k] = str(tablicaLiczb[k])
        w = len(tablicaLiczb[k])
        while (w):
            tablicaRobocza.append(tablicaLiczb[k][w - 1])
            w = w - 1

        tablicaLiczb[k] = int(tablicaLiczb[k]) + int(doLiczby(tablicaRobocza))
        dodawane = dodawane + 1
        # print str(tablicaLiczb[k]) +" "+ str(dodawane)
        if (sprawdz(tablicaLiczb[k]) == 0):
            # print str(tablicaLiczb[k])+" "+str(dodawane)
            break

    if (sprawdz(tablicaLiczb[k]) == 0):
        print str(tablicaLiczb[k]) + " " + str(dodawane)
        k = k + 1