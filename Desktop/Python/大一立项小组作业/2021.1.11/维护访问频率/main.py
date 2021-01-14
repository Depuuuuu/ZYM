if __name__ == '__main__':

    from CardHandClasss import *

    a = CardHand()
    heart = a.heart()
    clubs = a.clubs()
    spades = a.spades()
    diamonds = a.diamonds()
    for i in range(1,5):
        a.add_card(i, heart)
        a.add_card(i, clubs)
        a.add_card(i, spades)
        a.add_card(i, diamonds)
    for i in a:
        print(i)
    print(a.all_of_suit(heart))