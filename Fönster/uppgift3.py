import tkinter as tk
from tkinter import messagebox
import os
import requests

class FileEditorApp:
    def __init__(self, root):
        # Huvudfönster
        self.root = root
        self.root.title("File Editor")  # Fönstrets titel
        self.root.geometry("1250x600")  # Fönstrets storlek

        # Huvudfönster
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Textfält för att skriva eller visa text
        self.text_field = tk.Text(self.main_frame, height=20, width=100)
        self.text_field.pack(pady=10, padx=10)

        # Textfält för att skriva egen text för att spara i fil
        self.input_field = tk.Text(self.main_frame, height=5, width=100)
        self.input_field.pack(pady=10, padx=10)

                
        # Inmatningsfält för API-sökvillkor
        self.search_field = tk.Entry(self.main_frame, width=30)
        self.search_field.pack(pady=5)

        # Rekommendationer för sökord
        self.recommendations_label = tk.Label(self.main_frame, text="Rekommenderade sökord: Pris, Produkter")
        self.recommendations_label.pack(pady=5)

        # Filnamn för att läsa och skriva till
        self.filename = "data.txt"

        # Knapp för att skriva text till fil
        self.save_button = tk.Button(self.main_frame, text="Skriv till fil", command=self.write_to_file)
        self.save_button.pack(pady=5)

        # Knapp för att läsa från fil
        self.load_button = tk.Button(self.main_frame, text="Läs från fil", command=self.read_from_file)
        self.load_button.pack(pady=5)

        # Knapp för att rensa textfältet
        self.clear_button = tk.Button(self.main_frame, text="Rensa", command=self.clear_text_field)
        self.clear_button.pack(pady=5)

        # Knapp för att hämta data från API
        self.fetch_button = tk.Button(self.main_frame, text="Hämta data från API", command=self.fetch_data_from_api)
        self.fetch_button.pack(pady=5)

        # Knapp för att avsluta programmet
        self.quit_button = tk.Button(self.main_frame, text="Avsluta", command=self.root.quit)
        self.quit_button.pack(pady=5)

        
    def write_to_file(self):
        """Skriver innehållet från textfältet och inputfältet till en fil."""
        text_from_output = self.text_field.get("1.0", tk.END).strip()
        text_from_input = self.input_field.get("1.0", tk.END).strip()
        text = text_from_output + '
' + text_from_input if text_from_output and text_from_input else text_from_output or text_from_input  # Hämtar text från textfältet
        if text:
            with open(self.filename, 'a') as file:  # Öppnar filen i append-läge
                file.write(text + "\n")
            messagebox.showinfo("Info", "Texten har sparats till fil.")
        else:
            messagebox.showwarning("Varning", "Textfältet är tomt.")

    def read_from_file(self):
        """Läser från filen och visar innehållet i textfältet."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                file_content = file.read()
                self.text_field.delete("1.0", tk.END)  # Rensar textfältet innan vi skriver ny text
                self.text_field.insert(tk.END, file_content)  # Infogar innehållet från filen
        else:
            messagebox.showwarning("Varning", "Filen finns inte.")

    def clear_text_field(self):
        """Rensar textfältet."""
        self.text_field.delete("1.0", tk.END)

    def fetch_data_from_api(self):
        """Hämtar data från Fake Store API baserat på användarens inmatade villkor och sparar det i filen."""
        condition = self.search_field.get().strip().lower()  # Hämtar användarens sökvillkor
        if not condition:
            messagebox.showwarning("Varning", "Ange ett giltigt villkor för att hämta data.")
            return

        try:
            # API-anrop till Fake Store API
            response = requests.get("https://fakestoreapi.com/products", timeout=10)

            if response.status_code == 200:
                data = response.json()
                # Debug: skriver ut hela API-responsen för att se vad som hämtas
                print("Hämtad data från API:", data)

                filtered_data = []

                if condition == "pris":
                    # Sortera efter pris i fallande ordning
                    filtered_data = sorted(data, key=lambda x: x['price'], reverse=True)
                    formatted_data = "\n".join([f"Pris: ${item['price']}" for item in filtered_data])
                elif condition == "produkter":
                    # Sortera efter kategori och sedan alfabetiskt efter titel
                    filtered_data = sorted(data, key=lambda x: (x['category'].lower(), x['title'].lower()))
                    formatted_data = "\n".join([f"Produkt: {item['title']}, Kategori: {item['category']}, Pris: ${item['price']}" for item in filtered_data])
                else:
                    # Filtrera produkter som matchar användarens villkor
                    filtered_data = [
                        item for item in data if condition in item['title'].lower() or condition in item['category'].lower()
                    ]
                    formatted_data = "\n".join([f"Pris: ${item['price']}, Produkt: {item['title']}, Kategori: {item['category']}" for item in filtered_data])

                if filtered_data:
                    # Visar data i textfältet och sparar till fil
                    self.text_field.delete("1.0", tk.END)
                    self.text_field.insert(tk.END, formatted_data)
                    with open(self.filename, 'a') as file:
                        file.write(formatted_data + "\n")
                    messagebox.showinfo("Info", "Data har hämtats och sparats.")
                else:
                    messagebox.showinfo("Info", f"Ingen data hittades för villkoret: {condition}.")
            else:
                messagebox.showerror("Fel", f"API-anrop misslyckades med statuskod {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Fel", f"Ett fel inträffade vid API-anrop: {str(e)}")
        except Exception as e:
            messagebox.showerror("Fel", f"Ett oväntat fel inträffade: {str(e)}")

    

# Skapar huvudfönstret för Tkinter
root = tk.Tk()

# Skapar och startar applikationen
app = FileEditorApp(root)

# Startar huvudloopen för Tkinter GUI
root.mainloop()
