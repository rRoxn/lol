class Bankkonto:
    def __init__(self, ett_namn: str, ett_saldo: int):
        self.NAMN = ett_namn
        self.SALDO = ett_saldo
        self.MÅNADSPARANDE = 0  # Initialt inget månadssparande
        self.AKTIER = ""  # Initialt inga aktier

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

    def TOSTRING(self):
        return f"Kontoinnehavare: {self.NAMN}, Saldo: {self.SALDO} kr, Månadssparande: {self.MÅNADSPARANDE} kr, Aktier: {self.AKTIER}"
    


# 1. Skapa ett nytt bankkonto
namn = input("Ange kontoinnehavarens namn: ")
saldo = int(input("Ange initialt saldo: "))
mitt_konto = Bankkonto(namn, saldo)

# 2. Sätt in pengar
insättning = int(input("Ange belopp att sätta in: "))
mitt_konto.SÄTTA_IN(insättning)

# 3. Ta ut pengar
uttag = int(input("Ange belopp att ta ut: "))
mitt_konto.TA_UT(uttag)

# 4. Sätt månadssparande och aktie
månadsspar = int(input("Ange månadssparande: "))
aktie = input("Ange aktie (eller tryck Enter för ingen): ")
mitt_konto.SÄTT_MÅNADSPAR(månadsspar)
if aktie:  # Kontrollera om användaren angav en aktie
    mitt_konto.SÄTT_AKTIE(aktie)

# 5. Skriv ut kontoinformationen
print(mitt_konto.TOSTRING())