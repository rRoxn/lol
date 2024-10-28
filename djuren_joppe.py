from abc import ABC, abstractmethod
import random


class petowner:
    __name = "tomt"  # Notera åtkomstdirektivet private för att inte kunna ändra den någonstans
    __djur = []  # Lista för djuren petowner äger.

    def __init__(self, name):  # Constructor
        __name = name
        # Skapar objekt med constructorn och lägger till dessa i listan __djur
        # Hårdkodar dessa in i listan, för att inte behöva ta emot värdena ifrån användare. Men det ska ju gå att lägga till djur i programmet.
        # Har nog varit för mycket att göra det också.
        self.__djur.append(dog(3, "Magnus"))
        self.__djur.append(dog(13, "Göran"))
        self.__djur.append(puppy(6, "Milo"))
        self.__djur.append(cat(7, "Tiger"))
        self.__djur.append(bird(10, "Lucas"))
        self.__djur.append(fish(45, "Robert"))

    # Metod för att skriva ut alla djur i listan __djur
    def print_animals(self):
        print("Eggzons djur")
        for i, djur in enumerate(self.__djur):
            print(f"{i + 1}. {djur}")

    # Metod för att leka med ett djur i listan
    def play(self):

        print("Välj ett djur att leka med") #Print för fråga användare om Vilket djur
        self.print_animals()                #Skickar efter print_animals metoden för att visa djur.
        while True:                         #En while loop som väntar på input för ett djur.
            try:
                val = int(input("Välj ett djur i listan: "))
                if 1 <= val <= len(self.__djur):
                    djur = self.__djur[val - 1]

                    # throw_ball
                    throw_ball = input("Vill du kasta en boll till djuret? (j/n): ")
                    if throw_ball.lower() == 'j':
                        djur.interact(throw_ball=True)  #Throw ball skickar tillbaka till metoden och ändrar värdet till True
                    else:
                        djur.interact()     #Kallar efter interact metoden i animals utan throw_ball.
                    djur._hungry = True     #Ändrar _hungry värdet till True efter man lekt med djuret.
                    break                   #Breaker loopen för man har lekt
                else:
                    #Skriver man en siffra som inte finns i listan så printas detta ut
                    print("Ogiltigt val! ange ett nummer ur listan.")
            # Tar med en ValueError för att catcha fel om användaren skriver in något annat än int integer.
            except ValueError:
                print("Ogiltigt inmatning Ange ett nummer")

    #Metod för matning(feed) för djuren.
    def feed(self):

        print("Djuren väntar otåligt!") #Print som säger att djuren väntar otåligt innan val av djur.
        self.print_animals()            #Hämtar metoden print_animals för att visa djuren
        #Använder en try-except för att fånga fel skrivningar som användare gör, allt utom int
        try:
            val = int(input("Välj ett djur att mata (ange nummer): "))
            if 1 <= val <= len(self.__djur):             #Går igenom listan.
                djur = self.__djur[val - 1]             #Tar valet minus et då man börjar räkna från 0 i listan så val 0 är = 1 för användaren.
                #Det skickas till metoden feed i klasserna, där de tar emot den som ett arg.
                food = input(f"Vad vill du mata {djur._name} med? "         #Skriver ut och frågar vad man vill mata djuret med
                             f" (Favoritmat: {djur._favourite_food}): ")    #Och skriver ut favorit mat för djuret.

                #Om användaren skriver inget avbryts loopen och man går tillbaka.
                if food.lower() == 'inget':
                    return

                djur.eat(food) #Hämtar metoden eat(skickar med food värdet)
            else:
                print("Ogiltigt val.")
        #Except ValueError för typos
        except ValueError:
            print("Ogiltigt val.")

    #Run metod för programmet, och för en meny För att integrera med objekten i __djur
    def run(self):
        print("Sötnosarna")
        val = ""  # Initiera val till en tom sträng
        while val != "0":  # Kör slingan tills användaren anger 0
            print("\nMeny:")
            print("1. Mata  ett djur")
            print("2. Leka med ett djur")
            print("3. Skriv ut alla djur")
            print("0. Avsluta")
            val = input("Välj ett alternativ: ")

            if val == "1":
                self.feed()
            elif val == "2":
                self.play()
            elif val == "3":
                self.print_animals()
            elif val == "0":
                print("Avslutar programmet...")
            else:
                print("Ogiltigt val. Försök igen.")
#ABC är då för att få klassen abstract. (ärver ifrån ABC
class animal(ABC):
    """
    Skapar en abstract klass där denna klass är som en blueprint för animals när man skapar djur.
    Den definiera "vanliga" attributes and behaviors som alla djur har. Subklasserna kommer att ärva ifrån
    denna klassen.
    Denna klass kallas då aldrig utan subklasserna kallar till denna.
    """
    #Variabler för hålla objektens attributes
    _age = 0
    _name = ""
    _hungry = False
    _favourite_food = "Kött"

    @abstractmethod  # För att meotoden ska ses som abstract och göra så att alla subklasser måste ha en __init__
    def __init__(self, age, name):

        self._age = age
        self._name = name
    #Metod för att ta hand om matningen för djuren. feed ifrån petowner kallar denna metod.
    #Den använder food som ett arg
    def eat(self, food):

        print("Matdax!")
        #Lägger till en variabel för mat räknare
        feed_count = 0
        while True:
            #Lägger till en i räknare.
            feed_count += 1
            # konverterar input till lowercase.
            if food.lower() == self._favourite_food.lower():
                #Om food är favourite_food så sätt self_hungry som False och då blir djuret "mätt"
                print(f"{self._name} äter {food} med glädje!")
                self._hungry = False
                print("Djuret är Mätt")
                feed_limit = 1  # Lägger feed limit till 1 för favorit mat.
                #Om man matar med något annat så skriver den ut att djuret ff är hungrig. Man måste mata djuren två gånger med annan mat.
            else:
                print(f"{self._name} äter {food}, men är fortfarande lite hungrig.")

                #Sätter feed limit till 2 då man behöver mata 2 gånger för att få djuret mätt
                feed_limit = 2  # 2 feedings for other food
            #Om räknare når feed limit så skriver den ut att djuret har ätit tillräckligt och vill leka
            if feed_count >= feed_limit:
                self._hungry = False
                print(f"{self._name} har ätit tillräckligt och vill nu leka.")
                break

            #Frågar om man vill mata igen efter man har matat djuret. Om nej så breaker de.
            another = input("Mata mer? (j/n): ")
            if another.lower() != 'j':
                break

            # Få ny mat input för denna gången.
            food = input(f"Vad vill du mata {self._name} med mer? "
                         f"(Favoritmat: {self._favourite_food}): ")

    #Metod för att integrera med djuren.
    def interact(self, throw_ball=False):  # Default parameter, for throw ball.
        if throw_ball:
            if self._hungry:
                print(f"{self._name} är för hungrig för att jaga bollen.")
            else:
                # Ålders koll för djuren som använder denna.
                if self._age < 2:
                    print(f"{self._name} springer klumpigt efter bollen.")
                elif self._age < 7:
                    print(f"{self._name} jagar entusiastiskt efter bollen!")
                else:
                    print(f"{self._name} orkar inte springa efter bollen, men viftar glatt på svansen.")
        #Denna får man om man leker med djuren utan att kasta bollen till de.
        else:
            print(f"{self._name} blir glad.")

     #Metod för att skriva ut objekten i listan. Sätter olika för hunger värdet.
    def __str__(self):
        hungry_status = "är mätt" if not self._hungry else "är hungrig"
        return f"{self._name} ({type(self).__name__}), {self._age} år, {hungry_status}"
#Klass för hundar som ärver ifrån animal.
class dog(animal):
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En hund har skapats")


#klass för valpar som ärver i från dog.
class puppy(dog):
    def __init__(self, months, name):  # Constructor med månader och namn istället

        super().__init__(0, name)  # Kallar efter baseclass och ger värdet 0 as age.
        self._months = months  # Ger klassen months som ett värde.
#Klass för katter som ärver i från animal men har egna attributes och metoder.
class cat(animal):
    #Klass variabel för favorit mat för katt
    _favourite_food = "Fisk"

    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En katt har skapats")

    def interact(self, throw_ball=False):
        if throw_ball:
            if self._hungry:
                print(f"{self._name} är för hungrig för att bry sig om bollen.")
            else:
                print(f"{self._name} tittar på bollen med ointresse.")
        else:
            super().interact()
    def eat(self, food):


         # Hanterar eating för katten om maa inte ger katten favorit maten så har katten 50% chans att jaga en mus

        if food != self._favourite_food and random.random() < 0.5:
            print("Katten ger sig ut på jakt efter en mus!")
            #Simulerar att katten jagar en mus och blir mätt av att äta den.
            print("Katten fångade en mus och är mätt!")
            self._hungry = False  # Katten är mätt efter ätit sin mus.
        else:
            # Om katten får sin favoritmat så jagar inte han och man kallar efter metoden i animals

            super().eat(food)


#Klass för fiskar har också egna attributes och metoder. då jag ändrar metoden för interact så man inte kan leka med detta djur
class fish(animal):

    _favourite_food = "fiskmat"

    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En fisk har skapas")

    def interact(self, throw_ball=False):
        if throw_ball:
            print(f"{self._name} är en fisk och kan inte leka med en boll!")  # Fish-specific message
        else:
            #Skriver ut detta om man inte kastar bollen till fisken som då inte går. Går ej att leka med en fisk.
            print(f"{self._name} är en fisk och kan inte leka!")


    def eat(self, food):
        print("Matdax")
        if food.lower() != self._favourite_food.lower():
            print("Fisken är mätt och simmar runt.")
            self._hungry = False

#Klass för fågeln
class bird(animal):
    #klassvariabl.
    _favourite_food = "solrosfrön"
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En fågel har skapats")
    #metod för interact
    def interact(self, throw_ball=False):
        if throw_ball:
            if self._hungry:
                print(f"{self._name} är för hungrig för att bry sig om bollen.")
            else:
                print(f"{self._name} flyger efter bollen men får inte tag på den.")

        else: super().interact()

    def eat(self, food):
        if food != self._favourite_food:
            print("Fågeln är mätt och kvittrar gott")
            self._hungry = False

        else:
            super().eat(food)


#Skapar en variabel för Egzon som kommer vara petowner. Sen kör man denna.
Egzon = petowner("Egzon")
Egzon.run()

'''Via metoden Run som tillhör objektet Jocke så styrs hela programmet
Objektet Jocke skapas av klassen petowner.
Från detta nya objekt körs metoden Run() som hela programmet utgår ifrån.
I denna metod ska en meny visas där man kan genomföra olika aktiviteter
När metoden Run är klar (om man väljer att avsluta menyn) så kommer inget mer att hända'''


