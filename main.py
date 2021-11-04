#!/usr/bin/env python3
import random
     
def deckgenerator():
    fruits = ['apple','grapes', 'strawberry', 'peach', 'plum', 'pear']
    deck = []
    for i in range(6): #Ennyi gyümölcs van
        for j in range(5): #Számozás
            for k in range(4): # Mindegyik kártyából ennyi van
                deck.append(fruits[i] + ' ' + str(j+1))
    return deck


def draw(deck):
    a = deck.pop(0) #kiveszi az elso kartyát a paklibol aka huz egy lapot
    return a


def main():
    deck = deckgenerator()
    random.shuffle(deck) #megkeveri a kártyákat
    print(draw(deck)) 


if __name__ == "__main__":
    main()