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



def main():
    deck = deckgenerator()
    random.shuffle(deck) #megkeveri a kártyákat
    print(deck) 


if __name__ == "__main__":
    main()