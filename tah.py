class Tah:
#vše co dělá ta pygame + se sem bude passovat informace z enginu pro vykreslení

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