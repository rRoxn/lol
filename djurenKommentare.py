from abc import ABC, abstractmethod
import random


class petowner:
    __name = "tomt"  # Notera åtkomstdirektivet private för att inte kunna ändra den någonstans
    __djur = []  # Lista för djuren petowner äger.

    def __init__(self, name):  # Constructor
        __name = name
        # Skapar objekt med constructorn och lägger till dessa i listan __djur
        #Hårdkodar dessa in i listan, för att inte beghöva ta emot vördena ifrån användare. Men det ska ju gå att lägga till djur i programmet. 
        #Har nog varit för mycket att göra det också. 
        self.__djur.append(dog(3, "Magnus"))
        self.__djur.append(dog(6, "Göran"))
        self.__djur.append(puppy(6, "Milo"))
        self.__djur.append(cat(7, "Tiger"))
        self.__djur.append(bird(10, "Lucas"))
        self.__djur.append(fish(45, "Robert"))

    # Metod för att skriva ut alla djur i listan __djur
    def print_animals(self):
        print("Egzons djur")
        for i, djur in enumerate(self.__djur):
            print(f"{i + 1}. {djur}")

    # Metod för att leka med ett djur i listan
    def play(self):

        print("Välj ett djur att leka med") #Print för fråga användare om Vilket djur 
        self.print_animals() #Skickar efter print_animals metoden för att visa djur.
        while True: #En while loop som väntar på input för ett djur. 
            try:
                val = int(input("Välj ett djur i listan: "))
                if 1 <= val <= len(self.__djur):
                    djur = self.__djur[val - 1]

                    
                    #throw_ball
                    throw_ball = input("Vill du kasta en boll till djuret? (j/n): ")
                    if throw_ball.lower() == 'j':
                        djur.interact(throw_ball=True)  # Throw ball
                    else:
                        djur.interact()  # Kallar efter interact funktionen i animals. 
                    djur._hungry = True #Ändrar _hungry värdet till True efter man lekt med djuret. 
                    break #Breaker loopen för man har lekt 
                else:
                    print("Ogiltigt val! ange ett nummer ur listan.")#Skriver man en siffra som inte finns i listan så printas detta ut
            #Tar med en ValueError för att catcha fel om användaren skriver in någpot annat än int integer. 
            except ValueError:
                print("Ogiltigt inmatning Ange ett nummer") 
    #Metod för matning(feed) för djuren. 
    def feed(self):
        #Print som säger att djuren vätar otåligt
        print("Djuren väntar otåligt!")
        self.print_animals() #Hämtar metoden print_animals för att visa djuren

        try:#Använder en try-except för att fånga fel skrivningar som användare gör, allt utom int
            val = int(input("Välj ett djur att mata (ange nummer): "))
            if 1 <= val <= len(self.__djur):#Går igenom listan. 
                djur = self.__djur[val - 1]  #Tar valet minus et då man börjar räkna från 0 i listan så val 0 är = 1 för användaren.

                food = input(f"Vad vill du mata {djur._name} med? " #Skriver ut och frågar vad man vill mata djuret med
                             f" (Favoritmat: {djur._favourite_food}): ") #Och skriver ut favorit mat för djuret. 


                if food.lower() == 'inget':
                    return  # Om användaren skriver inget avbryts loopen och man går tillbaka.

                djur.eat(food)  # Hämtar metoden eat(skickar med food värdet)
            else:
                print("Ogiltigt val.")
        #Except ValueError för typos        
        except ValueError:
            print("Ogiltigt val.")

    # Run metod för programmet, och för en meny För att integrera med i __djur
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

class animal(ABC):

    # Skapar en abstract klass där subklasserna ska ärva funktioner/värde. Som en blueprint för djur.
    # Där jag skapar dessa funktioner för "dog" som en blueprint.
    #Varför göra klassen abstract är för att man ska kunna se att det är "blueprint" klassen som man ärver ifrån eller kör metoder. 
    #Variabler för klasserna. Som alla ska ha. 
    _age = 0
    _name = ""
    _hungry = False
    _favourite_food = "Kött"

    @abstractmethod  # För att metoden ska klassas som abstract. 
    def __init__(self, age, name):

        self._age = age
        self._name = name

    def eat(self, food):
        """
       Tar hand om antalet gånger eller om det är favoritmaten till djuret. 
       Blir hungrig efter 2 av valfri mat som är vilket input som helst. du kan skriva banan som godis. 
        """
        print("Matdax!")
        #Variabel för räknare för matning
        feed_count = 0
        while True:
            feed_count += 1
            # Convert both food and _favourite_food to lowercase for comparison
            if food.lower() == self._favourite_food.lower():
                print(f"{self._name} äter {food} med glädje!")
                self._hungry = False
                print("Djuret är Mätt")
                feed_limit = 1  # 1 feeding for favorite food
            else:
                print(f"{self._name} äter {food}, men är fortfarande lite hungrig.")
                feed_limit = 2  # 2 feedings for other food

                feed_limit = 2  # 2 feedings for other food

            if feed_count >= feed_limit:
                self._hungry = False
                print(f"{self._name} har ätit tillräckligt och vill nu leka.")
                break

            # Ask if the user wants to feed the animal again
            another = input("Mata mer? (j/n): ")
            if another.lower() != 'j':
                break

            # Get new food input for the next iteration
            food = input(f"Vad vill du mata {self._name} med mer? "
                         f"(Favoritmat: {self._favourite_food}): ")


    def interact(self, throw_ball=False):  # Default parameter for overloading
        if throw_ball:
            if self._hungry:
                print(f"{self._name} är för hungrig för att jaga bollen.")
            else:
                # Age-specific behavior (example for dogs)
                if self._age < 2:
                    print(f"{self._name} springer klumpigt efter bollen.")
                elif self._age < 7:
                    print(f"{self._name} jagar entusiastiskt efter bollen!")
                else:
                    print(f"{self._name} orkar inte springa efter bollen, men viftar glatt på svansen.")
        else:  # Original behavior when throw_ball is False
            print(f"{self._name} viftar glatt på svansen.")

     # Funktion för att skriva ut objekten.
    def __str__(self):
        hungry_status = "är mätt" if not self._hungry else "är hungrig"
        return f"{self._name} ({type(self).__name__}), {self._age} år, {hungry_status}"
#Dog klassen kommer ärva det mesta ifrån Animal rakt av. 
class dog(animal):
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En hund har skapats")



class puppy(dog):
    def __init__(self, months, name):  # Constructor with name and months as arguments

        super().__init__(0, name)  # Call the base class constructor with age 0 and the given name
        self._months = months  # Assign the months value to the puppy's attribute

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
            super().interact()  # Call the base class interact()

    def eat(self, food):

        """
          Tar hand om mata funktionen för katt, (override) eat i animals för subklass
          """
        if food != self._favourite_food and random.random() < 0.5:
            print("Katten ger sig ut på jakt efter en mus!")
            # Simulate hunting - you can add more elaborate logic here if needed
            print("Katten fångade en mus och är mätt!")
            self._hungry = False  # Katten är mätt efter ätit sin mus.
        else:
            # If the cat gets its favorite food or doesn't hunt,
            # call the original eat() method from the Animal class
            super().eat(food)


        # class fish(animal):
class fish(animal):
    _favourite_food = "fiskmat"
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En fisk har skapas")

    def interact(self, throw_ball=False):
        return super().interact(throw_ball)

    def eat(self, food):
        print("Matdax")
        if food != self._favourite_food:
            print("Fågeln är mätt och kvittar gott")
            self._hungry = False

        else:
            super().eat(food)

class bird(animal):
    #klassvariabl.
    _favourite_food = "solrosfrön"
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En fågel har skapats")

    def interact(self, throw_ball=False):
        if throw_ball:
            print(f"{self._name} flyger iväg!")  # Bird always flies away when ball is thrown
        else:
            if self._hungry:
                print(f"{self._name} är för hungrig för att flyga runt.")
            else:
                print(f"{self._name} flyger runt glatt!")  # Bird flies around happily

    def eat(self, food):
        if food != self._favourite_food:
            print("Fågeln är mätt och kvittrar gott")
            self._hungry = False

        else:
            super().eat(food)



Egzon = petowner("Egzon")
Egzon.run()

'''Via metoden Run som tillhör objektet Jocke så styrs hela programmet
Objektet Jocke skapas av klassen petowner.
Från detta nya objekt körs metoden Run() som hela programmet utgår ifrån.
I denna metod ska en meny visas där man kan genomföra olika aktiviteter
När metoden Run är klar (om man väljer att avsluta menyn) så kommer inget mer att hända'''


