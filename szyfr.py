def szyfr_V(text, klucz, tryb=True):
    dlugosc_klucza = len(klucz)
    klucz_ASCII = [ord(i) for i in klucz]
    text_ASCII = [ord(i) for i in text]
    wynik = []
    j = 0
    for i in range(len(text_ASCII)):
        if 65 <= text_ASCII[i] <= 90:
            if tryb:
              wynik.append(chr((text_ASCII[i] + klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")))
            else:
              wynik.append(chr((text_ASCII[i] + 26 - klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")))
            j += 1
        elif 97 <= text_ASCII[i] <= 122: 
            if tryb:
              wynik.append(chr(((text_ASCII[i] - 32) + klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")).lower())
            else:
              wynik.append(chr(((text_ASCII[i] - 32) + 26 - klucz_ASCII[j % dlugosc_klucza]) % 26 + ord("A")).lower())
            j += 1
        else:
            wynik.append(chr(text_ASCII[i]))
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
