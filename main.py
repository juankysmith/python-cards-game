from elements.cards import DeckOfCards
from time import sleep

if __name__ == "__main__":
    deck = DeckOfCards()
    num_cards = input('¿How many cards do you want?  ')
    while not num_cards.isnumeric() or (num_cards.isnumeric() and int(num_cards) <= 0):
        num_cards = input('Please, introduce a number > 0 ¿How many cards do you want?  ')
    num_cards = int(num_cards)
    for card in deck.next():
        print('Your card: {}'.format(card))
        print('{} cards left'.format(len(deck)))
        sleep(2)
        num_cards -= 1
        if not num_cards:
            break
