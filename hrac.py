class Hrac:

    def __init__(self, id, jmeno, strana):
        self._id = id
        self._strana = strana
        self._jmeno = jmeno
        self._domek = 0
        
        
    @property
    def id(self):
        return self._id
    
    @property
    def strana(self):
        return self._strana
    
    @property
    def jmeno(self):
        return self._jmeno
    
    @property
    def domek(self):
        return self._domek
    
    @domek.setter
    def domek(self, value):
        self._domek = value