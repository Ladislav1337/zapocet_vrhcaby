class UI:

    def __init__(self):
        pass
    
    def nakresli_desku(self, deska):
        for policko in deska.obsah:
            rr = f"[{policko.x}]: {policko.ascii_obsahu()}"
            print(rr)
    
    def nakresli_tahy(self, tahy):
        i = 0
        for tah in tahy:
            rr = f"[{i}]: kostka({tah.kostka}) | {tah.zacatek} -> {tah.cil}"
            print(rr)
            i+=1
            
    def nakresli_misc(self, kostka, hrac):
        print(f"Hraje: {hrac.jmeno}({hrac.id})")
        a = []
        for cislo in kostka:
            a.append(cislo)
        print(f"Kostka: {a}")