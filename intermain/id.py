import time
import json
import random
import os

filedir = os.path.dirname(os.path.abspath(__file__))
ok = time.localtime()
year_ = ok.tm_year
miesiac_ = ok.tm_mon
dzien_ = ok.tm_mday
del ok

def wagi(pesel):
    """Oblicz cyfrę kontrolną PESEL na podstawie pierwszych 10 cyfr."""
    tablica_wag = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    for i in range(10):
        suma += int(pesel[i]) * tablica_wag[i]
    ostatnia_cyfra = suma % 10
    cyfra_kontrolna = (10 - ostatnia_cyfra) % 10
    pesel += str(cyfra_kontrolna)
    return pesel

def liczpesel(datadzien, datamiesiac, datarok, plec):
    """Zbuduj poprawny numer PESEL na podstawie daty i płci."""
    pesel = ""
    pesel += str(datarok)[-2:]
    m_offset = datamiesiac + (20 if datarok >= 2000 else 0)
    pesel += f"{m_offset:02d}"
    pesel += f"{datadzien:02d}"

    # trzy losowe cyfry
    for _ in range(3):
        pesel += str(random.randint(0, 9))

    # cyfra oznaczająca płeć (nieparzysta=mężczyzna, parzysta=kobieta)
    if plec == "m":
        pesel += str(random.randint(1, 5) * 2 - 1)
    elif plec == "k":
        pesel += str(random.randint(0, 4) * 2)
    else:
        pesel += str(random.randint(0, 9))

    pesel = wagi(pesel)
    return pesel

def auto(wzraca=False):
    # =========================================================================
        # SEKCJA 1: PODSTAWOWE DANE IDENTYFIKACYJNE I DATA URODZENIA
        # =========================================================================
        # {pesel}       -> Zwraca: 11-cyfrowy tekst (string) będący wygenerowanym numerem PESEL.
        #                  Zawiera zakodowaną datę urodzenia, serię losową, cyfrę płci oraz cyfrę kontrolną.
        # {datarok}     -> Zwraca: Liczbę całkowitą (int), np. 1995. Rok, w którym ta osoba się urodziła.
        # {datamiesiac} -> Zwraca: Liczbę całkowitą (int) z zakresu 1-12. Miesiąc urodzenia tej osoby.
        # {datadzien}   -> Zwraca: Liczbę całkowitą (int) z zakresu 1-31. Dzień miesiąca, w którym osoba się urodziła.
        #print(f"dane osobowe:\npesel: {pesel}\nrok urodzenia: {datarok}\nmiesiac urodzenia: {datamiesiac}\ndzien urodzenia: {datadzien}")

        # =========================================================================
        # SEKCJA 2: TOŻSAMOŚĆ, STATUS I WYLOSOWANE PARAMETRY WEJŚCIOWE (WIEK OSOBY)
        # =========================================================================
        # {plec}        -> Zwraca: Tekst (string) "kobieta" lub "meszczyzna". Określa płeć biologiczna osoby.
        # {imie}        -> Zwraca: Tekst (string) zawierający wylosowane z bazy JSON imię pasujące do płci.
        # {nazwisko}    -> Zwraca: Tekst (string) zawierający wylosowane z bazy JSON nazwisko.
        # {emeryt}      -> Zwraca: Wartość logiczną (bool) True lub False. Wynik warunku, czy wiek przekracza próg emerytalny.
        # {wiekdane}    -> Zwraca: Liczbę całkowitą (int). Wylosowany na samym początku, wyjściowy wiek (np. od 18 do 70).
        # {miesiacdane} -> Zwraca: Liczbę całkowitą (int). Wylosowany na samym początku, wyjściowy miesiąc (od 1 do 12).
        # {dziendane}   -> Zwraca: Liczbę całkowitą (int). Wylosowany na samym początku, wyjściowy dzień (od 1 do 28/31).
        #
        # UWAGA LOGICZNA: {wiekdane}, {miesiacdane} i {dziendane} to były parametry "startowe" do obliczeń.
        # Natomiast faktyczna data urodzenia ({datadzien}.{datamiesiac}.{datarok}) powstała dopiero PO przesunięciach kalendarzowych.
        #print(f"plec: {plec}\nimie: {imie}\nnazwisko: {nazwisko}\nczy emeryt: {emeryt}\ndane o dzisiejszym wieku osoby:\nwiek: {wiekdane}\nmiesiac: {miesiacdane}\ndzien: {dziendane}")

        # =========================================================================
        # SEKCJA 3: ZEGAR SYSTEMOWY (STAN CALENDARZA W MOMENCIE URUCHOMIENIA)
        # =========================================================================
        # {year_}       -> Zwraca: Liczbę całkowitą (int). Obecny rok pobrany z systemu operacyjnego (np. 2026).
        # {miesiac_}    -> Zwraca: Liczbę całkowitą (int). Obecny miesiąc pobrany z systemu operacyjnego (np. 5).
        # {dzien_}      -> Zwraca: Liczbę całkowitą (int). Obecny dzień miesiąca pobrany z systemu operacyjnego (np. 30).
        #print(f"dzisiejsza data:\nrok: {year_}\nmiesiac: {miesiac_}\ndzien: {dzien_}")
    sciezka = os.path.join(filedir,"imiona.json")
    """Wygeneruj losowe dane osobowe. Zwraca tuple gdy wzraca=True."""
    sciezka = os.path.join(filedir, "imiona.json")
    with open(sciezka, encoding="UTF-8") as r:
        dane = json.load(r)

    plec = random.choice(["k", "m"])
    if plec == "m":
        imie = random.choice(dane["imiona"]["meskie"])
    else:
        imie = random.choice(dane["imiona"]["zenskie"])

    nazwisko = random.choice(dane["nazwiska"])

    wiek = random.randint(18, 70)
    wiekdane = wiek
    miesiac = random.randint(1, 12)
    miesiacdane = miesiac
    dzien = random.randint(1, 28)
    dziendane = dzien
    emeryt = True if wiek > 60 else False

    datadzien = dzien
    datamiesiac = miesiac
    if (miesiac_ < miesiac) or (miesiac_ == miesiac and dzien_ < dzien):
        datarok = year_ - wiek - 1
    else:
        datarok = year_ - wiek

    pesel = liczpesel(datadzien, datamiesiac, datarok, plec)
    plec_str = "meszczyzna" if plec == "m" else "kobieta"

    if not wzraca:
        print(f"dane osobowe:\npesel: {pesel}\nrok urodzenia: {datarok}\nmiesiac urodzenia: {datamiesiac}\ndzien urodzenia: {datadzien}")
        print(f"plec: {plec_str}\nimie: {imie}\nnazwisko: {nazwisko}\nczy emeryt: {emeryt}\ndane o dzisiejszym wieku osoby:\nwiek: {wiekdane}\nmiesiac: {miesiacdane}\ndzien: {dziendane}")
        print(f"dzisiejsza data:\nrok: {year_}\nmiesiac: {miesiac_}\ndzien: {dzien_}")
    else:
        return (
            pesel,           # 1. string: 11-cyfrowy numer PESEL
            datarok,         # 2. int: Faktyczny rok urodzenia (np. 1995)
            datamiesiac,     # 3. int: Faktyczny miesiąc urodzenia (1-12)
            datadzien,       # 4. int: Faktyczny dzień urodzenia (1-31)
            plec,            # 5. string: "kobieta" lub "meszczyzna"
            imie,            # 6. string: Wylosowane/wpisane imię
            nazwisko,        # 7. string: Wylosowane/wpisane nazwisko
            emeryt,          # 8. bool: Status emerytalny (True/False)
            wiekdane,        # 9. int: Wylosowany/wpisany startowy wiek osoby
            miesiacdane,     # 10. int: Wylosowany/wpisany startowy miesiąc
            dziendane,       # 11. int: Wylosowany/wpisany startowy dzień
            year_,           # 12. int: Dzisiejszy rok pobrany z systemu
            miesiac_,        # 13. int: Dzisiejszy miesiąc pobrany z systemu
            dzien_           # 14. int: Dzisiejszy dzień pobrany z systemu
        )
#print(f"dane osobowe:\npesel: {pesel}\nrok urodzenia: {datarok}\nmiesiac urodzenia: {datamiesiac}\ndzien urodzenia: {datadzien}")
#print(f"plec: {plec}\nimie: {imie}\nnazwisko: {nazwisko}\nczy emeryt: {emeryt}\ndane o dzisiejszym wieku osoby:\nwiek: {wiekdane}\nmiesiac: {miesiacdane}\ndzien: {dziendane}")
#print(f"dzisiejsza data:\nrok: {year_}\nmiesiac: {miesiac_}\ndzien: {dzien_}")
