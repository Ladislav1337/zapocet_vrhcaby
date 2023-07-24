class Pole:

    def __init__(self, x):
        self._x = x
        self._obsah = [] #obsahuje žetony

    def je_volno(self, hrac_id) -> bool:
        return not((len(self._obsah)>1 and self._obsah[-1].hrac_id != hrac_id))

    def vrat_horni_zeton(self):
        pass
    
    def pridat_zeton(self, zeton):
        zeton.zapamatuj_pole(self.x)
        self._obsah.append(zeton)

    def odeber_zeton(self):
        self._obsah.pop(len(self._obsah)-1)

    def aktivni_zeton(self):
        return None if len(self._obsah) == 0 else self._obsah[-1]

    def ascii_obsahu(self):
        output = ""
        for zeton in self._obsah:
            output += f"{zeton.hrac_id} "
        for _ in range(6-len(self._obsah)):
            output += "  "
        return output

    @property
    def x(self):
        return self._x

    @property
    def obsah(self):
        return self._obsah