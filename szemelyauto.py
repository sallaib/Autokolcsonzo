# szemelyauto.py
from auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ferohely):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ferohely = ferohely

    def info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Férőhely: {self.ferohely}, Bérleti díj: {self.berleti_dij} Ft/nap"