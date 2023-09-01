class Zeton:

    def __init__(self, hrac_id):
        self._hrac_id = hrac_id

    def zapamatuj_pole(self, x):
        self._pamet.append(x)

    @property
    def hrac_id(self):
        return self._hrac_id