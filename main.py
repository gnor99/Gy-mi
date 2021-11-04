#!/usr/bin/env python3
import random
     
def deckgenerator():

    fruits = ['apple','grapes', 'strawberry', 'peach', 'plum', 'pear'] #ennyi gyümölcs van

    deck = []

    for i in range(6): #Ennyi gyümölcs van
        for j in range(5): #Számozás
            for k in range(4): # Mindegyik kártyából ennyi van
                deck.append(fruits[i] + ' ' + str(j+1)) #létrehoz egy kátyát úgy hogy elöször szerepel a gyümölcs és utána hogy hányas számú a kártya

    random.shuffle(deck) #megkeveri a kártyákat

    return deck


def draw(deck):

    a = deck.pop(0) #kiveszi az elso kartyát a paklibol aka huz egy lapot

    return a


def main():
    deck = deckgenerator()
    print(draw(deck)) 


if __name__ == "__main__":
    main()