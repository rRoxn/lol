class AKTIEPOST:
    def __init__(self, ett_namn: str, ett_värde: int, ett_antalaktier: int):
        self.NAMN = ett_namn
        self.VÄRDE_VID_KÖP = ett_värde
        self.VÄRDE = ett_värde
        self.DATUM_FÖR_KÖP = 20230926
        self.ANTAL_AKTIER = ett_antalaktier

    def to_string(self):
        return f"Aktie: {self.NAMN}, Värde vid köp: {self.VÄRDE_VID_KÖP} kr, Nuvarande värde: {self.VÄRDE} kr, Köpt: {self.DATUM_FÖR_KÖP}, Antal aktier: {self.ANTAL_AKTIER}"

class Bankkonto:
    def __init__(self, ett_namn: str, ett_saldo: int):
        self.NAMN = ett_namn
        self.SALDO = ett_saldo
        self.MÅNADSPARANDE = 0
        self.AKTIER = []

    def TA_UT(self, sum: int):
        if sum > 0 and sum <= self.SALDO:
            self.SALDO -= sum
            print(f"Uttag på {sum} kr genomfört. Nytt saldo: {self.SALDO} kr")
        else:
            print("Ogiltigt uttag. Kontrollera beloppet och tillgängligt saldo.")

    def SÄTTA_IN(self, sum: int):
        if sum > 0:
            self.SALDO += sum
            print(f"Insättning på {sum} kr genomfört. Nytt saldo: {self.SALDO} kr")
        else:
            print("Ogiltig insättning. Beloppet måste vara positivt.")

    def SÄTT_MÅNADSPAR(self, spar: int):
        if spar >= 0:
            self.MÅNADSPARANDE = spar
            print(f"Månadssparande satt till {spar} kr")
        else:
            print("Ogiltigt månadssparande. Beloppet måste vara positivt eller noll.")

    def SÄTT_AKTIE(self, en_aktie: str):
        self.AKTIER = en_aktie
        print(f"Aktieinnehav satt till: {en_aktie}")

    def VISA_AKTIER(self):
        if not self.AKTIER:
            print("Inga aktier registrerade.")
        else:
            print("\nAktieinnehav:")
            for aktie in self.AKTIER:
                print(aktie.to_string()) 

    def VISA_KONTOINFO(self):
        return f"Kontoinnehavare: {self.NAMN}, Saldo: {self.SALDO} kr, Månadssparande: {self.MÅNADSPARANDE} kr"

# Skapa ett nytt bankkonto
try:
    namn = input("Ange kontoinnehavarens namn: ")
    saldo = int(input("Ange initialt saldo: "))
    mitt_konto = Bankkonto(namn, saldo)

    # Fråga efter tre aktier
    for i in range(3):
        namn = input(f"Ange namn på aktie {i+1}: ")
        värde = int(input(f"Ange värde vid köp för aktie {i+1}: "))
        antal = int(input(f"Ange antal aktier för aktie {i+1}: "))
        aktiepost = AKTIEPOST(namn, värde, antal)
        mitt_konto.AKTIER.append(aktiepost) 

    while True:
        print("\nVälj ett alternativ:")
        print("1. Sätt in pengar")
        print("2. Ta ut pengar")
        print("3. Sätt månadssparande")
        print("4. Sätt aktie")
        print("5. Visa kontoinformation")
        print("6. Visa aktier") 
        print("7. Avsluta")

        val = input("Ange ditt val: ")

        if val == "1":
            insättning = int(input("Ange belopp att sätta in: "))
            mitt_konto.SÄTTA_IN(insättning)
        elif val == "2":
            uttag = int(input("Ange belopp att ta ut: "))
            mitt_konto.TA_UT(uttag)
        elif val == "3":
            månadsspar = int(input("Ange månadssparande: "))
            mitt_konto.SÄTT_MÅNADSPAR(månadsspar)
        elif val == "4":
            print("Du har redan registrerat tre aktier.") 
        elif val == "5":
            print(mitt_konto.VISA_KONTOINFO()) 
        elif val == "6":
            mitt_konto.VISA_AKTIER()
        elif val == "7":
            print("Avslutar programmet...")
            break 
        else:
            print("Ogiltigt val. Försök igen.")

except EOFError:
    print("Error: No input provided. Please make sure you are running the code in an interactive environment.")