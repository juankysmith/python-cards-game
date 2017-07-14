

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return self.name

    def take_card(self, card):
        self.cards.append(card)
