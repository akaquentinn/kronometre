# -*- coding: utf-8 -*-
import tkinter as tk
import time

font = "Saira"


class Kronometre:
    def __init__(self, master):
        self.master = master
        self.master.title("Kronometre")

        self.gecen_sure = 0
        self.running = False

        # ARAYÜZ ELEMENTLERİ
        self.sure_gostergesi = tk.Label(master, text="00:00:00", font=(font, 48))
        self.sure_gostergesi.pack()

        alt_cerceve = tk.Frame(master)
        alt_cerceve.pack(side=tk.BOTTOM, fill=tk.X)

        self.baslangic_butonu = tk.Button(
            alt_cerceve, text="Say", font=font, command=self.say
        )
        self.baslangic_butonu.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.durdur_butonu = tk.Button(
            alt_cerceve, text="Dur", font=font, command=self.dur
        )
        self.durdur_butonu.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.sifirla_butonu = tk.Button(
            alt_cerceve, text="Sıfırla", font=font, command=self.sifirla
        )
        self.sifirla_butonu.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.sureyi_guncelle()

        self.master.update()
        self.master.minsize(
            self.sure_gostergesi.winfo_width(),
            self.sure_gostergesi.winfo_height() + self.baslangic_butonu.winfo_height(),
        )

    def say(self):
        if not self.running:
            self.running = True
            self.sureyi_guncelle()

    def dur(self):
        self.running = False

    def sifirla(self):
        self.gecen_sure = 0
        self.sure_gostergesi.config(text="00:00:00")
        self.dur()

    def sureyi_guncelle(self):
        if self.running:
            self.gecen_sure += 1
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(self.gecen_sure))
            self.sure_gostergesi.config(text=formatted_time)
            self.master.after(1000, self.sureyi_guncelle)


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("C:/kronometre/icon/kronometre.ico")
    chronometer = Kronometre(root)
    root.mainloop()
