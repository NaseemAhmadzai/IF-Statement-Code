class Card(object):
    # Static variables:
    cardName = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "T": "10", "J": "Jack",
                "Q": "Queen", "K": "King", "A": "Ace"}
    suitName = {"D": "Diamonds", "C": "Clubs", "H": "Hearts", "S": "Spades"}
    cardValue = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                 "A": 14}
    suitValue = {"D": 0.1, "C": 0.2, "H": 0.3, "S": 0.4}

    def __init__(self, value: str):
        value = value.upper()  # Capitalizes the values
        self.name = value[0]
        self.suit = value[1]

    def __str__(self):
        """

        :return:str-> The name of the card.
        """
        return Card.cardName[self.name] + " of " + Card.suitName[self.suit]

    def get_cardName(self):
        """
        Returns the card name
        """
        return Card.cardName[self.name]

    def get_suitName(self):
        """
        Returns the suit name
        """
        return Card.suitName[self.suit]

    def get_cardValue(self):
        """
        Returns the card value
        """
        return Card.cardValue[self.name]

    def get_suitValue(self):
        """
        Returns the suit name
        """
        return Card.suitValue[self.suit]

    def __eq__(self, other):
        """
        :param other: Other Card.
        Returns True if both card are equal else returns False
        """
        return other.get_suitValue() == self.get_suitValue() and other.get_cardValue() == self.get_cardValue()

    def __lt__(self, other):
        """
         :param other: Other Card.
         Returns True if self is less than other else returns False
         """
        if self.get_suitValue() == other.get_suitValue():  # If the suitvalue is same.
            return self.get_cardValue() < other.get_cardValue() # Compares the card Value
        return self.get_suitValue() < other.get_suitValue()

    def __gt__(self, other):
        """
         :param other: Other Card.
         Returns True if self is greater than or other else returns False
         """
        if self.get_suitValue() == other.get_suitValue():# If the suitvalue is same.
            return self.get_cardValue() > other.get_cardValue()# Compares the card Value
        return self.get_suitValue() > other.get_suitValue()

    def __le__(self, other):
        """
         :param other: Other Card.
         Returns True if self is less than or equals to other else returns False
         """
        return self.__lt__(other) and self.__eq__(other)

    def __ge__(self, other):
        """
         :param other: Other Card.
         Returns True if self is greater than or equals to other else returns False
         """
        return self.__gt__(other) and self.__ge__(other)
