from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return self.deck

    def shuffle(self):
        return shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


class Player:
    def __init__(self):
        self.hand = []
        self.chip = 1000
        self.hand_total = 0
        self.ace = 0

    def receive_card(self, card):
        self.hand.append(card)

    def count_point(self):
        global round_on
        self.ace = 0
        self.hand_total = 0
        for n in self.hand:
            if n.rank == 'Ace':
                self.ace += 1
            self.hand_total += values[n.rank]

    def hand_status(self):
        print("You have in your hand: ")
        for n in self.hand:
            print(n)
        print(f"You have {self.hand_total} points")

    def check_busted(self):
        global round_on
        self.count_point()
        if self.hand_total == 21 and len(self.hand) == 2:
            self.hand_status()
            print("BLACKJACK!!")
            round_on = False
        elif self.hand_total > 21 and self.ace >= 1:
            while self.hand_total > 21 and self.ace >= 1:
                self.hand_total -= 10
                self.ace -= 1
            if self.hand_total > 21:
                self.hand_status()
                print("Busted")
                round_on = False
            else:
                self.hand_status()
        elif self.hand_total <= 21:
            self.hand_status()
        elif self.hand_total > 21:
            self.hand_status()
            print("Busted")
            round_on = False

    def hit_or_stand(self):
        global round_on
        while round_on:
            self.check_busted()
            if round_on:
                try:
                    a = input("Hit or stand: ").capitalize()
                    if a == "Hit":
                        self.receive_card(deck.deal_card())
                    elif a == "Stand":
                        round_on = False
                    else:
                        print("You can only type 'Hit' or 'Stand'")
                except:
                    print("Error. Try again.")


class House:
    def __init__(self):
        self.hand = []
        self.chip = 1000
        self.hand_total = 0
        self.ace = 0

    def receive_card(self, card):
        self.hand.append(card)
        self.hand_total += values[card.rank]

    def count_point(self):
        global round_on
        self.ace = 0
        self.hand_total = 0
        for n in self.hand:
            if n.rank == 'Ace':
                self.ace += 1
            self.hand_total += values[n.rank]

    def hand_status(self):
        print("The house has: ")
        for n in self.hand:
            print(n)
        print(f"House has {self.hand_total} points")

    def check_busted(self):
        global round_on
        self.count_point()
        if not round_on:
            if self.hand_total == 21 and len(self.hand) == 2:
                self.hand_status()
                print("BLACKJACK!!")
            elif self.hand_total > 21 and self.ace >= 1:
                while self.hand_total > 21 and self.ace >= 1:
                    self.hand_total -= 10
                    self.ace -= 1
                if self.hand_total > 21:
                    self.hand_status()
                    print("Busted")
                else:
                    self.hand_status()
            elif 17 < self.hand_total <= 21:
                self.hand_status()
            elif self.hand_total > 21:
                self.hand_status()
                print("Busted")
            else:
                house.receive_card(deck.deal_card())
                house.hand_status()
        else:
            print("The house has: ")
            print("Hidden card")
            for n in self.hand[1:]:
                print(n)

    def hit_or_stand(self):
        pass


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    game_on = True
    round_on = True
    player1 = Player()
    house = House()
    while game_on:
        while round_on:
            for _ in range(2):
                player1.receive_card(deck.deal_card())
                house.receive_card(deck.deal_card())
            house.check_busted()
            player1.hit_or_stand()
        house.check_busted()
        break

