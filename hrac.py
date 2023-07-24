class Hrac:

    def __init__(self, jmeno, id):
        self._jmeno = jmeno
        self._id = id
        self._domek = 0

    @property
    def id(self):
        return self._id

    @property
    def jmeno(self):
        return self._jmeno

    @property
    def domek(self):
        return self._domek



