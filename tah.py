class Tah:
    
    def __init__(self, zacatek, cil, kostka):
        self._zacatek = zacatek
        self._cil = cil
        self._kostka = kostka

    @property
    def zacatek(self):
        return self._zacatek

    @property
    def cil(self):
        return self._cil

    @property
    def kostka(self):
        return self._kostka