#skapa en klass för bankkonto
class Bankkonto:
    """
    __init__-metoden: "Konstruktor" för att skapa ett nytt objekt.

    Denna metod initierar ett nytt objekt av klassen och tilldelar värden till dess attribut baserat på de angivna parametrarna.

    Parametrar:
    * ett_namn (str): Namnet på kontoinnehavaren.
    * ett_saldo (int): Kontots initiala saldo.

    Attribut:
    * self.NAMN: Kontoinnehavarens namn (hämtas från parametern `ett_namn`).
    * self.SALDO: Kontots aktuella saldo (hämtas från parametern `ett_saldo`).
    * self.MÅNADSPARANDE: Månatligt sparande, initialt satt till 0.
    * self.AKTIER: Lista för att lagra aktieposter, initialt tom.
    """
    def __init__(self, ett_namn: str, ett_saldo: int):
        self.NAMN = ett_namn
        self.SALDO = ett_saldo
        self.MANADSPARANDE = 0 
        self.AKTIER = ""
    """
    Skapa en funktion för att ta ut pengar från bankkontot. Funktionen skall ta emot ett heltal(INT)
    Gör en if sats för att kontrollera att uttaget är positivt, sedan printar de ut 
    hur mycket man har tagit ut och skriver ut nuvarande saldo på konto.
    Om man inte skriver ett positivt tal så kommer det skrivas ut som ogiltligt.
    """
    def TA_UT(self, sum: int):
        if sum > 0 and sum <= self.SALDO:
            self.SALDO -= sum
            print(f"Uttag på {sum} kr genomfört. Nytt saldo: {self.SALDO} kr")
        else:
            print("Ogiltigt uttag. Kontrollera beloppet och tillgängligt saldo.")

    #Funktion för att sätta in pengar, liknande funktionen TA_UT
    def SATTA_IN(self, sum: int):
        if sum > 0:
            self.SALDO += sum
            print(f"Insättning på {sum} kr genomfört. Nytt saldo: {self.SALDO} kr")
        else:
            print("Ogiltligt insättning. Beloppet måste vara positivt.")
    
    #Funktion för att sätta månadsparande, liknande de andra funktionerna
    def SATT_MANADSPARANDE(self, spar: int):
        if spar >= 0:
            self.MANADSPARANDE = spar
            print(f"Månadsparande satt till {spar} kr")
        else:
            print("Ogiltligt månadssparande. Beloppet måste vara positivt eller noll.")
   
    """
     En funktion för att skriva in en aktie.
     Denna funktion tar emot en string och printar sedan ut vad för aktie man 
     har "tagit".
    """
    def SATT_AKTIE(self, en_aktie: str):
        self.AKTIER = en_aktie
        print(f"Aktieinnehav satt till: {en_aktie}")
    #Skapar en TOSTRING för att skriva ut bankkontots "innehåll" 
    def TOSTRING(self):
        return f"Kontoinnehavare: {self.NAMN}, Saldo: {self.SALDO} kr, Månadsparande: {self.MANADSPARANDE} kr, Aktier: {self.AKTIER}"
    
#Skapar ett bankkonto med namn och saldo
namn = input("Ange kontoinnehavarens namn: ")
saldo = int(input("Ange initialt saldo: "))
mitt_konto = Bankkonto(namn, saldo)

# 2. Sätt in pengar
insattning = int(input("Ange belopp att sätta in: "))
mitt_konto.SATTA_IN(insattning)

# 3. Ta ut pengar
uttag = int(input("Ange belopp att ta ut: "))
mitt_konto.TA_UT(uttag)

# 4. Sätt månadssparande och aktie
manadsspar = int(input("Ange månadssparande: "))
aktie = input("Ange aktie (eller tryck Enter för ingen): ")
mitt_konto.SATT_MANADSPARANDE(manadsspar)
if aktie:  # Kontrollera om användaren angav en aktie
    mitt_konto.SATT_AKTIE(aktie)

# 5. Skriv ut kontoinformationen
print(mitt_konto.TOSTRING())  


