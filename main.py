# main.py
import tkinter as tk
from tkinter import messagebox
from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto

def inicializalas():
    kolcsonzo = Autokolcsonzo("G1JLOK Kft.")

    # 3 autó hozzáadása
    auto1 = Szemelyauto("ABC-123", "Toyota Yaris", 5000, 5)
    auto2 = Szemelyauto("DEF-456", "Mercedes CLA", 9000, 5)
    auto3 = Teherauto("GHI-789", "Mercedes Sprinter ", 10000, 2)

    kolcsonzo.auto_hozzaadasa(auto1)
    kolcsonzo.auto_hozzaadasa(auto2)
    kolcsonzo.auto_hozzaadasa(auto3)

    # 4 bérlés hozzáadása
    kolcsonzo.berles("ABC-123", "2023-10-01")
    kolcsonzo.berles("DEF-456", "2023-10-02")
    kolcsonzo.berles("GHI-789", "2023-10-03")
    kolcsonzo.berles("ABC-123", "2023-10-04")  # ugyanaz az autó másik napra

    return kolcsonzo

def main():
    kolcsonzo = inicializalas()

    # Fő ablak létrehozása
    root = tk.Tk()
    root.title("Autókölcsönző Rendszer")

    # Funkciók a gombokhoz
    def autok_listazasa():
        autok = kolcsonzo.autok_listazasa()
        messagebox.showinfo("Elérhető autók", "\n".join(autok))

    def berlesek_listazasa():
        berlesek = kolcsonzo.berlesek_listazasa()
        messagebox.showinfo("Aktív bérlések", "\n".join(berlesek))

    def auto_berlese():
        berles_ablak = tk.Toplevel(root)
        berles_ablak.title("Autó bérlése")

        tk.Label(berles_ablak, text="Rendszám:").pack()
        rendszam_entry = tk.Entry(berles_ablak)
        rendszam_entry.pack()

        tk.Label(berles_ablak, text="Dátum (YYYY-MM-DD):").pack()
        datum_entry = tk.Entry(berles_ablak)
        datum_entry.pack()

        def berles_submit():
            rendszam = rendszam_entry.get()
            datum = datum_entry.get()
            eredmeny = kolcsonzo.berles(rendszam, datum)
            messagebox.showinfo("Bérlés eredménye", eredmeny)
            berles_ablak.destroy()

        tk.Button(berles_ablak, text="Bérel", command=berles_submit).pack()

    def berles_lemondasa():
        lemondas_ablak = tk.Toplevel(root)
        lemondas_ablak.title("Bérlés lemondása")

        tk.Label(lemondas_ablak, text="Rendszám:").pack()
        rendszam_entry = tk.Entry(lemondas_ablak)
        rendszam_entry.pack()

        tk.Label(lemondas_ablak, text="Dátum (YYYY-MM-DD):").pack()
        datum_entry = tk.Entry(lemondas_ablak)
        datum_entry.pack()

        def lemondas_submit():
            rendszam = rendszam_entry.get()
            datum = datum_entry.get()
            eredmeny = kolcsonzo.berles_lemondasa(rendszam, datum)
            messagebox.showinfo("Lemondás eredménye", eredmeny)
            lemondas_ablak.destroy()

        tk.Button(lemondas_ablak, text="Lemond", command=lemondas_submit).pack()

    # Gombok a fő ablakban
    tk.Button(root, text="Autók listázása", command=autok_listazasa).pack(pady=5)
    tk.Button(root, text="Autó bérlése", command=auto_berlese).pack(pady=5)
    tk.Button(root, text="Bérlés lemondása", command=berles_lemondasa).pack(pady=5)
    tk.Button(root, text="Bérlések listázása", command=berlesek_listazasa).pack(pady=5)
    tk.Button(root, text="Kilépés", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
