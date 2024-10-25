#Importerar funktion random för att kunna simulera random nummer. 
import random

#Skapa en funktion för att konvertera temperatur från fahrenheit till celcius
def fah_till_celcius(fahrenheit):
    """ Konverterar en temp från fahrenheit till Celcius.
    
    Argument: Temperaturen i Fahrenheit (Heltal)
    Returns: Temperaturen i Celcius (decimaltal)
    """

    celcius = (fahrenheit - 32) * 5/9
    return celcius

#En ny funktion för att slumpa ett tal för fahrenheit till celcius 

def slump_fahr_celcius():
    """
    Genererar en slumpmässig temp, ifrån (import random) och konverterar denna med 
    funktionen fah_till_celcius

    Returns:
        temperaturen i celcius 
    """
    
    slump_fahr = random.randint(-100, 100) #Slumpmässigt värde mellan -100 till 100
    return fah_till_celcius(slump_fahr) 

#Har med __name__ =="__main__" blocket för "syns skulle" där detta egentligen inte behöver vara med när vi endast skall köra detta scriptet ensamt. 
if __name__ == "__main__":
    #Körning av den ordinarie metoden och skapa en variabel för input och printa resultat
    fah_input = int(input("Ange en temperatur i Fahrenheit: "))
    celcius_resultat = fah_till_celcius(fah_input)
    print(f"{fah_input} grader Fahrenheit är lika med: {celcius_resultat:.1f} grader Celcius")

    #Körning av den andra metoden och skapa en variabel för lagra resultat
    slump_celcius = slump_fahr_celcius()
    print(f"Den slumpmässiga temperaturen i Celcius är: {slump_celcius:.1f}")

