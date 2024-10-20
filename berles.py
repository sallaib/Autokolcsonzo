# berles.py
class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum  # 'YYYY-MM-DD' formátumban

    def info(self):
        return f"Bérlés - Autó: {self.auto.rendszam}, Dátum: {self.datum}"