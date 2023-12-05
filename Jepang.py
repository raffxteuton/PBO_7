import tkinter as tk
import requests

# Definisikan fungsi untuk menerjemahkan teks
def translate(text):
    url = "https://translate.googleapis.com/translate"
    params = {
        "q": text,
        "source": "id",
        "target": "ja",
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return data["translated_text"][0]


# Definisikan kelas utama aplikasi
class TranslateApp(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.init_ui()

    def init_ui(self):
        # Buat label untuk teks asli
        self.label_teks_asli = tk.Label(self, text="Teks Asli")
        self.label_teks_asli.grid(row=0, column=0)

        # Buat kotak input untuk teks asli
        self.entry_teks_asli = tk.Entry(self)
        self.entry_teks_asli.grid(row=0, column=1)

        # Buat label untuk teks terjemahan
        self.label_teks_terjemahan = tk.Label(self, text="Teks Terjemahan")
        self.label_teks_terjemahan.grid(row=1, column=0)

        # Buat label untuk hasil terjemahan
        self.label_teks_terjemahan_hasil = tk.Label(self)
        self.label_teks_terjemahan_hasil.grid(row=1, column=1)

        # Buat tombol untuk menerjemahkan teks
        self.button_terjemahkan = tk.Button(self, text="Terjemahkan", command=self.translate_text)
        self.button_terjemahkan.grid(row=2, column=0)

    def translate_text(self):
        # Dapatkan teks asli dari kotak input
        teks_asli = self.entry_teks_asli.get()

        # Terjemahkan teks asli
        teks_terjemahan = translate(teks_asli)

        # Tampilkan teks terjemahan pada label
        self.label_teks_terjemahan_hasil.config(text=teks_terjemahan)


# Buat aplikasi
root = tk.Tk()
app = TranslateApp(root)
app.pack()
root.mainloop()
