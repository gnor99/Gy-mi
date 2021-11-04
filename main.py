#!/usr/bin/env python3
import random
     
def deckgenerator():

    fruits = ['apple','grapes', 'strawberry', 'peach', 'plum', 'pear'] #ennyi gyümölcs van

    deck1 = []
    deck2 = []

    for i in range(6): #Ennyi gyümölcs van
        for j in range(5): #Számozás
            for k in range(4): # Mindegyik kártyából ennyi van
                deck1.append(fruits[i] + ' ' + str(j+1)) #létrehoz egy kátyát úgy hogy elöször szerepel a gyümölcs és utána hogy hányas számú a kártya

    random.shuffle(deck1) #megkeveri a kártyákat

    for i in range(40): #az egyszemélyes játéknál 40 lapot vissza kell tenni a dobozba
        deck1.pop(0)

    for i in range(40): #ketté szedjük a paklit
        deck2.append(deck1.pop(0)) 

    return deck1, deck2

def choose(left, right):
    #a két felhuzzpt lapból választani kell egyet amit megtarunk, a másikat eldobjuk
    print("type left if you want this card: " + left + '\n' + "type right if you want this card: " +  right)
    

    while input() != "left" or input() !="right":
        inp = input()

        if inp == "left":
            return left

        elif inp == "right":
            return right
    


def draw(deck1, deck2):
    first = deck1.pop(0) #kiveszi az elso kartyát az elsö paklibol aka huz egy lapot
    sec = deck2.pop(0) #kiveszi az elso kartyát a masodik paklibol aka huz egy lapot
    print("first: " + first + " sec: " + sec)
    choosen = choose(first, sec) 

    return choosen

def stackgenerator(): #létrehozza a különböző tárolokat 
    #ezek a gyümölcs paklik
    
    appledeck = [] 
    grapesdeck = []
    strawberrydeck = []
    peachdeck = []
    plumdeck = []
    peardeck = []


def main():
    deck1,deck2 = deckgenerator()
    stackgenerator()
    print(draw(deck1,deck2)) 



if __name__ == "__main__":
    main()