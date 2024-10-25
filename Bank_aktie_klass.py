class Aktiepost: 
    """ 
    Representerar en aktiepost med namn, värde vid köp, aktuellt värde, köpdatum
    och antal aktier. 
    Attribut
    * self.NAMN: Aktiens namn (str).
    * self.VÄRDE_VID_KÖP: Värdet vid köpet (int).
    * self.VÄRDE: Aktuellt värde (int).
    * self.DATUM_FÖR_KÖP: Köpdatum (int, t.ex. YYYYMMDD).
    * self.ANTAL_AKTIER: Antal aktier (int).
    """
    def __init__(self, ett_namn: str, ett_varde: int, ett_antalaktier: int):
        self.NAMN = ett_namn
        self.VARDE_VID_KOP = ett_varde
        self.VARDE = ett_varde
        self.DATUM_VID = 20240924 #dagens datum som koden skapades. 
        self.ANTAL_AKTIER = ett_antalaktier

    def toString(self):
        #Retunerar en strängpresentation av aktieposten.
        return f"Aktie: {self.NAMN}, Värde vid köp: {self.VARDE_VID_KOP}kr, Aktuellt värde: {self.VARDE} kr, Köpdatum: {self.DATUM_VID}, Antal aktier: {self.ANTAL_AKTIER}"

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
        self.AKTIER = []
    
    """
    Skapa en funktion för att ta ut pengar från bankkontot. Funktionen skall ta emot ett heltal(INT)
    Gör en if sats för att kontrollera att uttaget är positivt, sedan printar de ut 
    hur mycket man har tagit ut och skriver ut nuvarande saldo på konto.
    Om man inte skriver ett positivt tal så kommer det skrivas ut som ogiltligt.
    """
    def TA_UT(self, sum:int):
        if sum > 0 and sum <= self.SALDO:
            self.SALDO -= sum
            print(f"Uttag på {sum} kr genomfört. Nytt saldo: {self.SALDO} kr")
        else:
            print("Ogiltligt uttag. Kontrollera bellopet och tillgängligt saldo")
    
    #Utför en instättning till konto om bellopet är giltligt. 
    def SATTA_IN(self, sum: int):
        if sum > 0:
            self.SALDO += sum
            print(f"Insättning på {sum} kr genomfört. Nytt saldo: {self.SALDO} kr")
        else:
            print("Ogiltligt insättning. Beloppet måste vara positivt.")

    #Sätt månadssparande om beloppet är giltligt
    def SATT_MANADSSPARANDE(self, spar: int):
        if spar >= 0:
            self.MANADSPARANDE = spar
            print(f"Månadsparande satt till {spar} kr")
        else:
            print("Ogiltligt månadssparande. Beloppet måste vara positivt eller noll.")
    
    #Lägg till akiter i listan och tar emot objekt från klassen aktiepost
    def SATT_AKTIE(self, en_aktie: Aktiepost):
        self.AKTIER.append(en_aktie)
        print(f"Aktie tillagd: {en_aktie.NAMN}")

    #Skriv ut all information om aktierposter
    def VISA_AKTIER(self):
        if self.AKTIER:
            print("\nAktieinnehav:")
            for aktie in self.AKTIER:
                print(aktie.toString())
        else:
            print("Inga aktier registrerade.")

    #Retunera en strängspresentation av bankkonto, exklusive aktieinformation.
    def TOSTRING(self):
        return f"Kontoinnehavare: {self.NAMN}, Saldo: {self.SALDO} kr, Månadssparande: {self.MANADSPARANDE}kr"
    
#Huvudprogram
namn = input("Ange kontoinnehavarens namn: ")
saldo = int(input("Ange initialt saldo: "))
mitt_konto = Bankkonto(namn, saldo)

insattning = int(input("Ange belopp att sätta in: "))
mitt_konto.SATTA_IN(insattning)

uttag = int(input("Ange belopp att ta ut: "))
mitt_konto.TA_UT(uttag)

manadsspar = int(input("Ange månadssparande: "))
mitt_konto.SATT_MANADSSPARANDE(manadsspar)

#Fråga efter tre aktier
for i in range(3):
    namn = input(f"Ange namn på aktie {i+1}: ")
    varde = int(input(f"Ange värde vid köp för aktie {i+1}: "))
    antal = int(input(f"Ange antal aktier för aktie {i+1}: "))
    mitt_konto.SATT_AKTIE(Aktiepost(namn, varde, antal))

#Skriv ut kontoinformation och aktieinnehav
print(mitt_konto.TOSTRING())
mitt_konto.VISA_AKTIER()
    
