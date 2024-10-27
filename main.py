from abc import ABC, abstractmethod
import random


class petowner:
    __name = "tomt"  # Notera åtkomstdirektivet private för att inte kunna ändra den någonstans
    __djur = []  # Lista för djuren petowner äger.

    def __init__(self, name):  # Constructor
        __name = name
        # Skapar objekt med constructorn och lägger till dessa i listan __djur
        self.__djur.append(dog(3, "Magnus"))
        self.__djur.append(dog(13, "Göran"))
        self.__djur.append(puppy(6, "Milo"))
        self.__djur.append(cat(7, "Tiger"))
        self.__djur.append(bird(10, "Lucas"))
        self.__djur.append(fish(45, "Robert"))

    # Funktion för att skriva ut alla djur i listan __djur
    def print_animals(self):
        print("Eggzons djur")
        for i, djur in enumerate(self.__djur):
            print(f"{i + 1}. {djur}")

    # Funktion för att leka med djuren som kommer att hämta funktionen interact från djur klasserna
    def play(self):

        print("Välj ett djur att leka med")
        self.print_animals()
        while True:
            try:
                val = int(input("Välj ett djur i listan: "))
                if 1 <= val <= len(self.__djur):
                    djur = self.__djur[val - 1]

                    # Removed the hunger check here

                    throw_ball = input("Vill du kasta en boll till djuret? (j/n): ")
                    if throw_ball.lower() == 'j':
                        djur.interact(throw_ball=True)  # Throw ball
                    else:
                        djur.interact()  # Default interaction (wagging tail)
                    djur._hungry = True
                    break
                else:
                    print("Ogiltigt val! ange ett nummer ur listan.")

            except ValueError:
                print("Ogiltigt inmatning Ange ett nummer")

    def feed(self):
        """
        Användare kan använda denna funkktionen för att ge mat åt djuren
        denna hämtar från Animal funktionen eat
        Animal.eat() method.
        """
        print("Djuren väntar otåligt!")
        self.print_animals()

        try:
            val = int(input("Välj ett djur att mata (ange nummer): "))
            if 1 <= val <= len(self.__djur):
                djur = self.__djur[val - 1]  # Access the chosen animal

                food = input(f"Vad vill du mata {djur._name} med? "
                             f" (Favoritmat: {djur._favourite_food}): ")


                if food.lower() == 'q':
                    return  # Exit if the user enters 'q'

                djur.eat(food)  # Hämtar funktionen eat(skickar med food värdet)
            else:
                print("Ogiltigt val.")
        except ValueError:
            print("Ogiltigt val.")

    # Funktion för meny För att integrera med i __djur
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
    #

    _age = 0
    _name = ""
    _hungry = False
    _favourite_food = "Kött"

    @abstractmethod  # För att klassen ska bli abstrakt
    def __init__(self, age, name):

        self._age = age
        self._name = name

    def eat(self, food):
        """
        Handles eating behavior.
        1 feeding of favorite food to get hungry, 2 with other food.
        """
        print("Matdax!")
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
          Handles the eating behavior of the cat, including a chance to
          hunt for a mouse if not given its favorite food.
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
        return super().interact(throw_ball)

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


