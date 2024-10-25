from abc import ABC, abstractmethod
from array import array
import random
#Det är många kommentarer att hålla reda på.
#Ett tips är att om ni siktar mot betyget A att ni tar bort de kommentarerna.
#som inte är relevanta för er. Exempelvis om man siktar mot betyget E
#kan man ta bort alla kommentarer som inleds med att de riktar sig mot elever
#som siktar mot C eller A

'''Petowner är den klass som "äger" djuren och att dessa lagras i en vektor.
Petowner kan exempelvis mata djuren genom att anropa metoden eat() i djurets objekt
från metoden feed()'''

class petowner:
    __name = "tomt" #Notera åtkomstdirektivet private för att inte kunna komma åt denna någon annanstans i koden.
    __djur = []  #Lista för djuren petowner äger. 

    def __init__(self, name): #Konstruktor 
        __name = name
        #skapar objekt med konstruktorn och lägger till dessa i listan __djur
        self.__djur.append(dog(3, "Magnus"))
        self.__djur.append(puppy(0, "Milo"))
        self.__djur.append(cat(7, "Tiger"))
        self.__djur.append(bird(10, "Lucas"))
        self.__djur.append(fish(45, "Rubert"))

    #Skriver ut alla djur i listan
    def print_animals(self):
        print("Skriver ut alla djur")
        #Denna metod kan användas för att skriva ut alla djur
        for i, djur in enumerate(self.__djur):
            print(f"{i+1}. {djur}")
    #Metod för att leka med djuren som kommer att hämta funktionen interact från djur klasserna
    def play(self):
        print("Välj ett djur att leka med")
        self.print_animals() #Hämtar funktionen print_animal för att visa djuren
        while True:
            try:
                val = int(input("Välj ett djur i listan: "))
                if 1 <= val <= len(self.__djur):
                    djur = self.__djur[val - 1]
                    djur.interact()
                    djur._hungry = True
                    break
                else:
                 print("Ogiltligt val! Ange ett nummer ur listan.")

            except ValueError:
                 print("Ogitligt inmatning Ange ett nummer")
    
                
  
    def feed(self):
        print("Djuret äter")


    def Run(self):
        print("Här kommer menyn")
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
        
        # I denna metod styrs programmet.
        # Skapa en loop som körs så länge användaren inte skriver in noll(0) som kan innebära att programmet avslutas
        # I menyn kan användaren välja att exempelvis leka med eller mata ett djur.
        #Medan du utvecklar koden så rekommenderas att man anropar olika
        #metoder för djuret genom att koda detta direkt i koden i denna metod.
        #så slipper man använda menyn under utvecklingsarbetet.
        #Exempelvis
        # self.play()
        #self.print_animals()


class animal(ABC):
     #Var noggranna med att läsa in er på vad det innebär att klassen är abstrakt
    #Läs studieguiden och titta på filmerna. Åtkomstdirektivet protected används. Varför?
    _age = 0
    _name = "tomt"
    _hungry = False
    _favourite_food = "Kött"
   
    @abstractmethod #För att klassen ska bli abstrakt
    
    def __init__(self, age, name):
        
        self._age = age
        self._name = name
        self._hungry = False
        self._favourite_food = "Kött"

    def eat(self, food):
        if (food == self._favourite_food):
            print("Djuret är mätt")
            self._hungry = False
            #Lämplig kod för att djuret ska bli mätt
        else:
            print("Djuret är hungrigt")
            self._hungry = True
            # Lämplig kod för att djuret fortsatt ska vara hungrigt

    def  getname(self):
        print("returnera namn")
        #Kod för att returnera namn

    
    def interact(self, throw_ball = False):  # Lägg till parameter throw_ball
        if throw_ball:
            if self._hungry:
                print("Djuret är för hungrigt för att jaga bollen.")
            else:
                if self.__age < 2:
                    print("Djuret springer klumpigt efter bollen.")
                elif self.__age < 7:
                    print("Djuret jagar entusiastiskt efter bollen!")
                else: #Om åldern är över 7år
                    print("Djuret orkar inte jaga bollen, men viftar glatt på svansen.")
        else:
            print("Djuret viftar glatt på svansen")
                


    #Funktion för att skriva ut obejekten. 
    def __str__(self):
        return (f"Namn: {type(self)._name}, Ålder: {self._age} Hungrig: {self._hungry}, Favorit mat: {self._favourite_food}")
       

class dog(animal):
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En hund har skapats")
    #Denna metod ärver från Animal och kommer att anropa metoden i klassen Animal
    def interact(self):
        return super().interact()
      
      
    def eat(self):  # Implementation of eat for the dog class
        print(f"{self._Name} äter hundmat.")

class puppy(dog):
    _months=0
    '''Skapa en konstruktorn som har värden Age och String om argument och dessa värden
    skickas till basklassen.
    Dessutom ska ytterligare ett värde läggas till och skickas med när objektet skapas
    Det är värdet månader. Och det ska inte skickas till base eftersom det värdet inte finns
    i basklassen. Värdet för age (i år) sätts till 0 (noll)'''

class cat(animal):
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En katt har skapats")

    def interact(self):
        print("katten spinner")

    def eat(self, food):
        print("Matdax")
        if food != self._favourite_food and random.random() < 0.5:
            print("Katten ger sig ut på jakt efter en mus!")
            print("Katten fångade en mus och är mätt!")
            self._hungry = False #Katten är mätt efter ätit sin mus.
        
        else:
            super().eat(food) #Anropar den usprunliga metoden eat från animal
        

#class fish(animal):
class fish(animal):
    _favourite_food = "Solrosfrön"
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
        


#class bird(animal):
class bird(animal):
    def __init__(self, _age, _name):
        super().__init__(_age, _name)
        print("En fågel har skapats")
    
    def interact(self, throw_ball=False):
        return super().interact(throw_ball)
    
    def eat(self, food):
        print("Matdax")
        if food != self._favourite_food:
            print("Fågeln är mätt och kvittar gott")
            self._hungry = False

        else:
            super().eat(food)


Jocke = petowner("Jocke")
Jocke.Run()

'''Via metoden Run som tillhör objektet Jocke så styrs hela programmet
Objektet Jocke skapas av klassen petowner.
Från detta nya objekt körs metoden Run() som hela programmet utgår ifrån.
I denna metod ska en meny visas där man kan genomföra olika aktiviteter
När metoden Run är klar (om man väljer att avsluta menyn) så kommer inget mer att hända'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
