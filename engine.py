from deska import Deska
from pole import Pole
from zeton import Zeton
from hrac import Hrac
from kostky import Kostky
from ui import UI

class Engine:
#Zvládání herní logiky, víceméně propojování těch tříd aby to dělalo tu hru

    def init(self):
        self._deska = Deska(24)
        self._ui = UI()
        self._hraci = []
        self._bar = []
        self._kostka = [] # hodnoty co se aktivně používají
        self.nova_hra()

    def nova_hra(self):
        self.inicializace()
        #self.vykreslenistavu()
        for  in range(20):
            self.hod_kostky()
            print(self._kostka)

    #vyrobí potřebné instance tříd
    def inicializace(self):
        self.vytvor_hrace()
        self.napln_desku()
        self.defaultni_zetony()

    def vykresleni_stavu(self):
        self._ui.nakresli_desku(self._deska)



##########  inicializace ###############
    def napln_desku(self):
        for i in range(self._deska.delka):
            self._deska.pridej_pole(Pole(i))

    def defaultni_zetony(self):
        ids = [] # budou vždycky dvě, z poolu těch hráčů
        for hrac in self._hraci:
            ids.append(hrac.id)
        self.napln_pole(0, 2, ids[0])
        self.napln_pole(11, 5, ids[0])
        self.napln_pole(16, 3, ids[0])
        self.napln_pole(18, 5, ids[0])
        self.napln_pole(5, 5, ids[1])
        self.napln_pole(12, 5, ids[1])
        self.napln_pole(7, 3, ids[1])
        self.napln_pole(23, 2, ids[1])

    def napln_pole(self, x, pocet, id_hrac):
        for pole in self.deska.obsah:
            if pole.x == x:
                for  in range(pocet):
                    pole.obsah.append(Zeton(id_hrac))

    def vytvor_hrace(self):
        self._hraci.append(Hrac(7, "Player 1"))
        self._hraci.append(Hrac(2, "Player 2"))