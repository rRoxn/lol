class Bankkonto:
    def __init__(self, ett_namn: str, ett_saldo: int):
        self.NAMN = ett_namn
        self.SALDO = ett_saldo
        self.MÅNADSPARANDE = 0
        self.AKTIER = ""

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

# 2. Lägg till en while-loop för att hantera val
while True:
    # 3. Skriv ut menyn
    print("\nVälj ett alternativ:")
    print("1. Sätt in pengar")
    print("2. Ta ut pengar")
    print("3. Sätt månadssparande")
    print("4. Sätt aktie")
    print("5. Visa kontoinformation")
    print("6. Avsluta")

    # 4. Ta emot användarens val
    val = input("Ange ditt val: ")

    # 5. Hantera valen med if, elif och else
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
        aktie = input("Ange aktie (eller tryck Enter för ingen): ")
        if aktie:
            mitt_konto.SÄTT_AKTIE(aktie)
    elif val == "5":
        print(mitt_konto.TOSTRING())
    elif val == "6":
        print("Avslutar programmet...")
        break  # Avsluta loopen
    else:
        print("Ogiltigt val. Försök igen.")