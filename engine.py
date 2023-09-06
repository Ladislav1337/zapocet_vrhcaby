import traceback
from deska import Deska
from pole import Pole
from zeton import Zeton
from hrac import Hrac
from kostky import Kostky
from ui import UI
from tah import Tah
import os

class Engine:
#Zvládání herní logiky, propojování těch tříd aby to dělalo tu hru

    def __init__(self):
        self._deska = Deska(24)
        self._ui = UI()
        self._kostky = Kostky(2)
        self.dohrano = False
        self._hraci = []
        self._bar = []
        self._kostka = [] # hodnoty co se aktivně používají
        self._mozne_tahy = []
        self._aktivni_hrac = None
        self.nova_hra()
         
    def nova_hra(self):
        self.inicializace()
        self.nove_kolo()
    
    def clear_console(self):
        os.system('clear')  # smazani konzole mezi jednotlivym tahem, pro prehlednost, mam pocit, ze to nefunguje pro windows, jen pro linux/mac

        
    #Naplní potřebné proměnné a nachystá vše pro začátek hry
    def inicializace(self):
        self.vytvor_hrace()
        self.napln_desku()
        self.defaultni_zetony()
        self._aktivni_hrac = self._hraci[0]
    
    def vykresleni_stavu(self):
        self._ui.nakresli_desku(self._deska)
        self._ui.nakresli_misc(self._kostka, self._aktivni_hrac)
        self._ui.nakresli_tahy(self._mozne_tahy)
        
    def hod_kostky(self):
        self._kostka = self._kostky.hodKostky()
    
    def vytvor_tahy(self):
        self._mozne_tahy = self.tahy_hrace(self._aktivni_hrac)
        if len(self._mozne_tahy) < 1:
            self.vymen_hrace()
        
    def nove_kolo(self):
        if self.win_check(): 
          return
        self.vytvor_tahy()
        if len(self._kostka) < 1 or len(self._mozne_tahy) < 1:
            self.vymen_hrace()
        self.vykresleni_stavu()

    #Zpracování konzole
    def tah_zadani(self, input):
        try:
            if input == "konec":
                self.ukonci_hru()
            else:
                zadani = int(input)
                if zadani < 0 or zadani >= len(self._mozne_tahy):
                    print("Zadej validní číslo.")
                else:
                    self.tah_provedeni(self._mozne_tahy[zadani])
        except ValueError:
            print("Zadej validní číslo.")
        except Exception as e:
            print(e)
            traceback.print_exc()
    
    #provedení vybraného tahu
    def tah_provedeni(self, tah):
        self.clear_console()  # Vymaže obsah konzole
        if tah.zacatek == "bar":
            self.proved_tah_bar(tah)
            print(f"Player {self._aktivni_hrac.id} hnul z baru na pole {tah.cil}.")
        elif tah.cil == "domek":
            self.proved_tah_domek(tah)
            print(f"Player {self._aktivni_hrac.id} hnul z pole {tah.zacatek} do domku s hodnotou {tah.kostka}.")
        else:
            self.proved_tah_normal(tah)
            print(f"Player {self._aktivni_hrac.id} hnul z pole {tah.zacatek} na pole {tah.cil} s hodnotou {tah.kostka}.")
        self._kostka = self.special_pop(self._kostka, tah.kostka)
        self.nove_kolo()
        
    def ukonci_hru(self):
        print("konec hry")
        self.dohrano = True
    
    def vymen_hrace(self):
        self._aktivni_hrac = self._hraci[(self._hraci.index(self._aktivni_hrac) + 1) % len(self._hraci)] #swapuje [0] a [1]
        self.hod_kostky()
        self.vytvor_tahy()
        
    def win_check(self):
        if len(self.hracovi_figurky(self._aktivni_hrac)) == 0:
            self.ukonci_hru()
            return True
        return False

#provedení tahů

    def proved_tah_bar(self, tah):
        zeton = None
        for zet in self._bar:
            if zet.hrac_id == self._aktivni_hrac.id:
                zeton = zet
        pole_nove =  self.najdi_pole(tah.cil)
        #kontrola na sebrání 
        if len(pole_nove.obsah) > 0 and pole_nove.aktivni_zeton().hrac_id !=  self._aktivni_hrac.id:
            #Nejdřív ji ulož do toho místa odkud ji pak zase vracíš do hry
            self._bar.append(pole_nove.aktivni_zeton())
            pole_nove.odeber_zeton()
        self._bar.remove(zeton)
        pole_nove.pridat_zeton(zeton)
    
    def proved_tah_domek(self, tah):
        zet = self.najdi_zeton(tah.zacatek)
        self.najdi_hrace(zet.hrac_id).domek += 1
        print(f"Player {zet.hrac_id} má v domku {self.najdi_hrace(zet.hrac_id).domek}.")
        self.najdi_pole(tah.zacatek).odeber_zeton()
        

    def proved_tah_normal(self, tah):
        zeton = self.najdi_zeton(tah.zacatek)
        pole_puvodni = self.najdi_pole(tah.zacatek)
        pole_nove = self.najdi_pole(tah.cil)
        #kontrola jestli to jde
        if pole_nove.je_volno(self.najdi_hrace(zeton.hrac_id)):
            pole_puvodni.odeber_zeton()
            #kontrola na sebrání 
            if len(pole_nove.obsah) > 0 and pole_nove.aktivni_zeton().hrac_id !=  zeton.hrac_id:
                #Nejdřív ji ulož do toho místa odkud ji pak zase vracíš do hry
                self._bar.append(pole_nove.aktivni_zeton())
                #ulož do paměti
                pole_nove.aktivni_zeton().zapamatuj_pole("bar")
                pole_nove.odeber_zeton()
            pole_nove.pridat_zeton(zeton)

#nabídka tahů

    def tahy_hrace(self, hrac):
        #musíš táhnout z baru?
        for zeton in self._bar:
            if zeton.hrac_id == hrac.id:
                #musíš udělat tahy z baru
                return self.bar_tahy(hrac)
        vse = []
        #můžeš táhnout do domku?
        if self.kontrola_domku(hrac):
            vse += self.domek_tahy(hrac)
        #normální tahy
        vse += self.overall_tahy(hrac)
        return vse

    def bar_tahy(self, hrac):
        vysledek = []
        for cislo in self._kostka:
            if(hrac.strana == "nahoru"):
                pol = self.najdi_pole(24-cislo)
            else:
                pol = self.najdi_pole(-1+cislo)
            if pol.je_volno(hrac):
                vysledek.append(Tah("bar",pol.x, cislo))
        return vysledek
    
    def domek_tahy(self, hrac):
        vysledek = []
        for cislo in self._kostka:
            for pole in self._deska.obsah:
                if pole.aktivni_zeton() != None and pole.aktivni_zeton().hrac_id == hrac.id:
                    if(hrac.strana == "nahoru"):
                        if pole.x - cislo < 0:
                            vysledek.append(Tah(pole.x, "domek", cislo))
                    else:
                        if pole.x + cislo > 23:
                            vysledek.append(Tah(pole.x, "domek", cislo))
        return vysledek
    
    def overall_tahy(self, hrac):
        vysledek = []
        for cislo in self._kostka:
            for pole in self._deska.obsah:
                if pole.aktivni_zeton() != None and pole.aktivni_zeton().hrac_id == hrac.id:
                    if ((pole.x - cislo > -1) and hrac.strana == "nahoru") or ((pole.x + cislo < 24) and hrac.strana == "dolu"):#pokud to je na desce
                        if(hrac.strana == "nahoru"):
                            pol = self.najdi_pole(pole.x - cislo)
                        else:
                            pol = self.najdi_pole(pole.x + cislo)
                        if pol.je_volno(hrac):
                            vysledek.append(Tah(pole.x, pol.x, cislo))
        return vysledek
    
    def kontrola_domku(self, hrac):
        for pole in self._deska.obsah:
            if hrac.strana == "nahoru":
                if pole.x > 5 and pole.aktivni_zeton() != None and pole.aktivni_zeton().hrac_id == hrac.id:
                    return False
            else:
                if pole.x < 18 and pole.aktivni_zeton() != None and pole.aktivni_zeton().hrac_id == hrac.id:
                    return False
        return True
    
    def hracovi_figurky(self, hrac):
        zetony = []
        for pole in self._deska.obsah:
            for zeton in pole.obsah:
                if zeton.hrac_id == hrac.id:
                    zetony.append(zeton)
        return zetony
    
    def najdi_pole(self, x):
        for pole in self._deska.obsah:
            if pole.x == x:
                return pole
    
    def najdi_zeton(self, x):
        return self.najdi_pole(x).aktivni_zeton()
    
    #popne z číselného arraye(kostky) jedno zadané číslo
    def special_pop(self, arr, item):
        vys = arr
        index_to_remove = arr.index(item)
        vys.pop(index_to_remove)
        print (f"Special pop: {vys}")
        return vys
    
    def najdi_hrace(self, id):
        for hrac in self._hraci:
            if hrac.id == id:
                return hrac
        return None
     
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
        for pole in self._deska.obsah:
            if pole.x == x:
                for _ in range(pocet):
                    pole.obsah.append(Zeton(id_hrac))
    
    def vytvor_hrace(self):
        self._hraci.append(Hrac(7, "Hráč 1", "dolu"))
        self._hraci.append(Hrac(2, "Hráč 2", "nahoru"))
            
    