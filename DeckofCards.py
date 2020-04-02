import os
import random
import re
import sys

IN_DECK = 1
DEALT = 1

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.suit = suit
        self.value = value
        def __hash__(self):
            return hash((self.name,self.suit,self.value))
        def __eq__(self, other):
            return (self.__class__ == other.__class__ and 
            self.name == other.suit and self.name == other.name and
            self.value == other.value)



class Deck:
    def __init__(self, suits, names, values):
        self.size = len(suits)*len(names)
        self.in_deck = []
        self.dealt = set()
        for i in range(len(names)):
            for s in suits:
                self.in_deck.append(Card(names[i],values[i],s))
        self.__shuffle()

    def __shuffle(self):
        random.shuffle(self.in_deck)
    
    def return_and_shuffle(self):
        for c in self.dealt:
            self.dealt.remove(c)
            self.in_deck.append(c)
        self.__shuffle()

    def deal_cards(self, cards_to_players, one_at_a_time=True):
        if sum(cards_to_players) > self.in_deck:
            return None
        hands = [[] for _ in range(len(cards_to_players))]
        if not one_at_a_time:
            for i, cards in enumerate(cards_to_players):
                for j in range(cards):
                    c = self.in_deck.pop()
                    self.dealt.add(c)
                    hands[i].append(c)
            return hands
        cards_left = True
        while cards_left:
            dealt = False
            for i, cards in enumerate(cards_to_players):
                if cards == 0:
                    continue
                c = self.in_deck.pop()
                self.dealt.add(c)
                hands[i].append(c)
                cards_to_players[i] -= 1
                dealt = True
            if not dealt:
                cards_left = False
        
        return hands
        
