#!/usr/bin/env python3
 
     
def deckgenerator():
    fruits = ['apple','grapes', 'strawberry', 'peach', 'plum', 'pear']
    deck = []
    for i in range(6): #Ennyi gyümölcs van
        for j in range(5): #Számozás
            for k in range(4): # Mindegyik kártyából ennyi van
                actual = fruits[i] + ' ' + str(j)
                deck.append(actual)
    return deck


def main():
    deck = deckgenerator()
    print(deck) 


if __name__ == "__main__":
    main()