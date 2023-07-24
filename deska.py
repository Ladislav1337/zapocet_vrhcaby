class Deska:
#obsah obsahuje políčka

    def __init__(self, delka):
        self._obsah = []
        self._delka = delka

    def pridej_pole(self, pole):
        self._obsah.append(pole)

    @property
    def obsah(self):
        return self._obsah

    @property
    def delka(self):
        return self._delka


    