# autokolcsonzo.py
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadasa(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        return [auto.info() for auto in self.autok]

    def berles(self, rendszam, datum):
        # ellenőrizzük, hogy az autó létezik-e és nem foglalt-e az adott dátumra
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if auto:
            if any(b for b in self.berlesek if b.auto.rendszam == rendszam and b.datum == datum):
                return "Az autó már foglalt az adott napra."
            else:
                uj_berles = Berles(auto, datum)
                self.berlesek.append(uj_berles)
                return f"Sikeres bérlés: {auto.rendszam} - {datum}"
        else:
            return "Nincs ilyen autó a rendszerben"

    def berles_lemondasa(self, rendszam, datum):
        berles = next((b for b in self.berlesek if b.auto.rendszam == rendszam and b.datum == datum), None)
        if berles:
            self.berlesek.remove(berles)
            return f"Sikeresen lemondta a bérlést: {rendszam} - {datum}"
        else:
            return "Nincs ilyen bérlés."

    def berlesek_listazasa(self):
        if not self.berlesek:
            return ["Nincsenek aktív bérlések."]
        else:
            return [berles.info() for berles in self.berlesek]