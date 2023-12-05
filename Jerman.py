import tkinter as tk
import googletrans

class Translate(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.label_teks_indonesia = tk.Label(self, text="Teks Indonesia")
        self.label_teks_indonesia.grid(row=0, column=0, sticky=tk.W)

        self.entry_teks_indonesia = tk.Entry(self)
        self.entry_teks_indonesia.grid(row=0, column=1, sticky=tk.W)

        self.button_terjemahkan = tk.Button(self, text="Terjemahkan", command=self.terjemahkan)
        self.button_terjemahkan.grid(row=1, column=0, sticky=tk.W)

        self.label_teks_jerman = tk.Label(self, text="Teks Jerman")
        self.label_teks_jerman.grid(row=2, column=0, sticky=tk.W)

        self.label_teks_jerman_hasil = tk.Label(self)
        self.label_teks_jerman_hasil.grid(row=2, column=1, sticky=tk.W)

    def terjemahkan(self):
        teks_indonesia = self.entry_teks_indonesia.get()
        penerjemah = googletrans.Translator()
        hasil_terjemahan = penerjemah.translate(teks_indonesia, dest="de")
        self.label_teks_jerman_hasil.config(text=hasil_terjemahan.text)


root = tk.Tk()
app = Translate(root)
app.pack()
root.mainloop()
