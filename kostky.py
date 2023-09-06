import random

class Kostky:
#má jen jednu public funkci na vrácení arraye těch kostek

    def __init__(self, pocet_kostek):
        self._pocet = pocet_kostek
        
    def hodKostky(self):
        kostky = []
        for _ in range(self._pocet):
            kostky.append(random.randint(1,6))
        #když jsou stejný zdvojnásob
        double = True
        for num in kostky:
            if num != kostky[0]:
                double = False
        if double:
            for _ in range(self._pocet):
                kostky.append(kostky[0])
        return kostky
    