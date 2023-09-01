class Hrac:

    def __init__(self, jmeno, id, strana):
        self._jmeno = jmeno
        self._id = id
        self._domek = 0
        self._strana=strana

    @property
    def id(self):
        return self._id

    @property
    def jmeno(self):
        return self._jmeno

    @property
    def domek(self):
        return self._domek

    @domek.setter
    def domek(self, value):
        self._domek = value



