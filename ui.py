class UI:
#Cokoliv co dělá to gay ass pygame + se sem budou passovat informace z enginu pro vykreslení

    def __init__(self):
        pass

    def nakresli_desku(self, deska):
        #horni tabulka
        for policko in deska.obsah:
            rr = f"[{policko.x}]: {policko.ascii_obsahu()}"
            print(rr)
