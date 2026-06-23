from threading import Thread,Event
from time import sleep
from sys import stdout
try:
    from intermain.id import auto
    from intermain.ai import run
    from intermain.api import pogoda
except:
    from typing import Any

    def auto(wzraca: bool = False) -> Any:
        # fallback when intermain.id is not available
        return None

    def run(liczba1: int, tekst: str, liczba2=1) -> str:
        # fallback when intermain.ai is not available
        return "nie zaladowano importu"

    def pogoda(*args, **kwargs):
        return None
"""
# spinner podczas długiej operacji
inter.printb("Ładowanie modelu...")
result = inter.spinner("sleep(3)", exec_or_eval="exec")
inter.printb(f"Zakończono: {result}", kolor="green")
choice = inter.inputs(
    "ok> ",
    ["1", "2", "3"],
    "Zły wybór, spróbuj jeszcze raz",
    True
)

inter.printb(f"Wybrałeś: {choice}", kolor="blue")

# końcowy komunikat
inter.printb(last=True, kolor="red")"""

class inter:
    _ostatnia_wiadomosc = ""
    def clear(self):
        import os
        os.system("cls")

    def printb(self, *args, sep=" ", end="\n", last=False, kolor=None):
        if kolor:
            BLACK   = "\033[30m"
            RED     = "\033[31m"
            GREEN   = "\033[32m"
            YELLOW  = "\033[33m"
            BLUE    = "\033[34m"
            MAGENTA = "\033[35m"
            CYAN    = "\033[36m"
            WHITE   = "\033[37m"
            RESET   = "\033[0m"
            BOLD    = "\033[1m"

            if kolor == "red":      kolor = RED
            elif kolor == "green":  kolor = GREEN
            elif kolor == "yellow": kolor = YELLOW
            elif kolor == "blue":   kolor = BLUE
            elif kolor == "magenta":kolor = MAGENTA
            elif kolor == "cyan":   kolor = CYAN
            elif kolor == "white":  kolor = WHITE
            elif kolor == "black":  kolor = BLACK
            elif kolor == "bold":   kolor = BOLD
            else:                   print("error");return
        else:
            kolor = ""
            RESET = ""

        if last:
            try:
                print(kolor + self._ostatnia_wiadomosc + RESET, end=end, sep=sep)
            except Exception:
                print("nie ma starej wiadomosci", end=end, sep=sep)
        else:
            wiadomosc = sep.join(str(a) for a in args)
            self._ostatnia_wiadomosc = wiadomosc
            print(kolor + wiadomosc + RESET, end=end, sep=sep)
    def inputs(self,wiad = "", wybory = [], error = "", as_int = False):
        while True:
            pick = input(wiad)
            if pick in wybory:
                if as_int == True:
                    pick = int(pick)
                    return pick
                else: return pick
            if error:
                print(wybory)
                print(error)

    def TrueorFalse(self,tekst=""):
        while True:
            pick = input(tekst)
            if pick == "y":
                return True
            elif pick == "n":
                return False
            else:
                print("wpisz y/n")

    def liczby(self,wybory:int, tekst:str):
        wybory = int(wybory)
        while True:
            try:
                pick = int(input(tekst))
                for i in range(1,wybory+1):
                    if pick == i:
                        pick = int(pick)
                        return pick
                print("nie ma takiego wyboru")
            except ValueError:
                print("nie ma takiego wyboru")

_inter = inter()

def ai(liczba1:int, tekst:str, liczba2=1):
    #liczba1:int jezeli 1 to local ai jezeli 2 to gemini
    #tekst to promt do ai
    #liczba2=1 jezeli wybrales local ai(1) to liczba2 to wybranie ai 1=gorsze ai 2=lepsze ai (jezeli uzywasz gemini zignoruj)
    odpowiedz = str(run(liczba1, tekst, liczba2))
    return odpowiedz

def generete_id():
    result = auto()
    if result is None:
        raise RuntimeError("auto() zwróciło None — brak załadowanego modułu intermain.id")
    pesel, datarok, datamiesiac, datadzien, plec, imie, nazwisko, emeryt, wiekdane, miesiacdane, dziendane, year_, miesiac_, dzien_ = result
    return pesel, datarok, datamiesiac, datadzien, plec, imie, nazwisko, emeryt, wiekdane, miesiacdane, dziendane, year_, miesiac_, dzien_




clear = _inter.clear
printb = _inter.printb
inputs = _inter.inputs
liczby = _inter.liczby
TrueorFalse = _inter.TrueorFalse