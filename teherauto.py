# teherauto.py
from auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras  # tonnában

    def info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras} t, Bérleti díj: {self.berleti_dij} Ft/nap"