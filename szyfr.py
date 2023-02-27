def szyfr_V(text, klucz, tryb=True):
    dlugosc_klucza = len(klucz)
    klucz_ASCII = [ord(i) for i in klucz] #zamiana każdego znaku w kluczu na numer w ASCII - komenda ord()
    text_ASCII = [ord(i) for i in text] #zamiana każdego znaku w tekście na numer w ASCII - komenda ord()
    wynik = []
    j = 0 #j zostało stworzone, żeby znaki specjalne nie zmieniały kolejności w kluczu. Na przykład spacja przestawiała kolejność 
    for i in range(len(text_ASCII)):
        if 65 <= text_ASCII[i] <= 90: #sprawdzam czy znak w tekście zawiera się między 65 i 90 (w tym przedziale znajdują się duże litery w ASCII)
            if tryb:
              wynik.append(chr((text_ASCII[i] + klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A"))) #do numeru ASCII tekstu dodajemy numer ASCII klucza i zamieniamy na znak komendą chr() - szyfrujemy tekst
            else:
              wynik.append(chr((text_ASCII[i] + 26 - klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")))#do numeru ASCII tekstu odejmujemy numer ASCII klucza. Potem modulo 26 daje reszte z dzielenia przez liczbe znakow alfabecie()26 co daje ilosc przesuniecia w znakach ASCII i zamieniamy na znak komendą chr() - odszyfrowujemy tekst
            j += 1
        elif 97 <= text_ASCII[i] <= 122: #sprawdzam czy znak w tekście zawiera się między 97 i 122 (w tym przedziale znajdują się małe litery w ASCII)
            if tryb:
              wynik.append(chr(((text_ASCII[i] - 32) + klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")).lower()) #do numeru ASCII tekstu dodajemy numer ASCII klucza i zamieniamy na znak komendą chr(). Dodatkowo zmieniam litere na małą - szyfrujemy tekst
            else:
              wynik.append(chr(((text_ASCII[i] - 32) + 26 - klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")).lower()) #do numeru ASCII tekstu odejmujemy numer ASCII klucza i zamieniamy na znak komendą chr(). Dodatkowo zmieniam litere na małą - odszyfrowujemy tekst
            j += 1
        else:
            wynik.append(chr(text_ASCII[i])) #Jeżeli znak nie znajduje się w przedziale dużych liczb ASCII (od 65 do 90) lub małych liczb(od 97 do 122) jest dodawany do wyniku bez szyfrowania
    return "".join(wynik)

text = input("Wprowadź zdanie: ")
klucz = input("Wprowadź klucz: ").upper()
tryb = input("Chcesz szyfrować czy deszyfrować zdanie? (sz/de): ").upper()

if tryb == "SZ":
    zaszyfr = szyfr_V(text, klucz)
    print("Zaszyfrowany tekst: ", zaszyfr)
elif tryb == "DE":
    deszyfr = szyfr_V(text, klucz, False)
    print("Zdeszyfrowany tekst: ", deszyfr)
else:
    print("Nieprawidłowy wybór.")
