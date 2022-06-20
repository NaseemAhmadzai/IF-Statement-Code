from card import Card
import csv
from statistics import mode


########## PROVIDED METHODS  ###########
########## NO NEED TO CHANGE ###########
def writeCSV(filename, data):
    # https://appdividend.com/2020/12/10/how-to-convert-python-list-to-csv-file/
    # https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows
    with open(filename, 'w', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerows(data)


def load_hands(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of poker hands to load
    
    Returns: a list of "poker hand strings".
    
    Depending on the size of the file, this function may
    take a while to finish.
    Taken from the MIT Problem sets
    '''

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    pokerHands = []
    for line in inFile:
        pokerHands.append(line.replace("\"", "").strip())
    print("  ", len(pokerHands), "Poker Hands loaded.")
    return pokerHands


################################################################
################################################################

#### No need to change __init__(), __str__(), isStraight() and isFlush() methods.
class pokerHand(object):

    def __init__(self, handData):
        '''Initializer of the pokerHand instance.
params: handData is a string of five valid Cards, separated by commas.'''
        listHandData = handData.split(",")

        self.hand = []  # will be our list of five cards.

        for rawHandStr in listHandData:
            self.hand.append(Card(rawHandStr))

        self.hand.sort()  # sort in place` to make it easier to identify

    def __str__(self):
        '''Returns a string representation of the cards.'''
        s = ""
        for c in self.hand:
            s = s + str(c) + ", "
        return s[:-2]  # don't include the last comma and space.

    #### Write the following methods which determine the type of poker hand it is.
    #### The first two of "isStraight()" and "isFlush()" is provided for you.
    #### https://www.wsop.com/poker-hands/
    def isStraight(self):
        '''returns True if the hand is a straight'''
        for i in range(4):  # See if the current card and the "next one" is one apart.
            if self.hand[i].get_cardValue() + 1 != self.hand[i + 1].get_cardValue():
                return False  # Gap of more than one - cannot be straight.
        return True  # They are all 1 apart from the neighbouring card. It's a straight..

    def isFlush(self):
        '''returns True if the hand is a flush'''
        ## Make sure they're all the same suit.
        return self.hand[0].get_suitValue() == self.hand[1].get_suitValue() == self.hand[2].get_suitValue() == \
               self.hand[3].get_suitValue() == self.hand[4].get_suitValue()

    #######################
    ####CHANGE BELOW HERE

    def isStraightFlush(self):
        '''returns True if it's a straight flush. False if it isn't, including Royal Flush.'''
        # If is flush and is stright . It can be Royal but we tackled this issue in isWhat by comparing this after
        # isRoyalFlush.
        return self.isFlush() and self.isStraight()

    def isRoyalFlush(self):
        '''returns True if it's a Royal Flush.'''
        # If isFlush and isStraight and all card values are greater than or equals 10
        return self.isFlush() and self.isStraight() and all(i.get_cardValue() >= 10 for i in self.hand)

    def isFourOfAKind(self):
        '''returns True if it's a four-of-a-kind.'''
        cardvalues = [i.get_cardValue() for i in self.hand]  # Get the values of the card
        if cardvalues.count(mode(cardvalues)) >= 4:  # If the most occurred card has occurred 4 times or not
            return True
        return False

    def isFullHouse(self):
        '''returns True if it's a full house'''
        cardvalues = [i.get_cardValue() for i in self.hand]  # Get the values of the card
        unique_card = set(cardvalues)  # Get the unique card which should be only 2
        if len(unique_card) != 2:  # If the number of unique card is not possible it cannot be Full House
            return False
        # Since now at this step there are only 2 unique card so it takes one card and
        # if it has occurred 2 or 3 times the other's occurrence will be 3 or 2 times.
        if cardvalues.count(cardvalues[0]) in (2, 3):
            return True
        return False

    def isThreeOfAKind(self):
        '''returns True if it is a three-of-a-kind.'''
        cardvalues = [i.get_cardValue() for i in self.hand]  # Get the values of the card
        # Checks whether the number of time the card which has occurred the most is 3 times or not
        # And
        # If the most occured card has occured 3 times then checks how many unique card are there if its 3
        # that means the other 2 card are not equal to each other
        if cardvalues.count(mode(cardvalues)) == 3 and len(set(cardvalues)) == 3:
            return True
        return False

    def isTwoPair(self):
        '''returns True if the hand has two pairs.'''
        cardvalues = [i.get_cardValue() for i in self.hand]
        unique_card = list(set(cardvalues))  # All the card without duplication
        occurred_twice = [cardvalues.count(i) == 2 for i in unique_card]  # Whether each card has occured twice or not
        if occurred_twice.count(True) == 2:  # If 2 cards have occurred twice
            return True
        return False

    def isOnePair(self):
        '''returns True if there's only one pair.'''
        cardvalues = [i.get_cardValue() for i in self.hand]
        unique_card = list(set(cardvalues))  # All the card without duplication
        occurred_twice = [cardvalues.count(i) == 2 for i in unique_card]
        # If 1 card has occurred twice . 1 of the other cards may occurr twice making it Two Pair
        # but we have tackled it in isWhat() by comparing this function after Two pair
        if occurred_twice.count(True) == 1:
            return True
        return False

    #######################

    def isWhat(self):
        """
        :return: str -> What type of poker it is
        It checks and returns what type of poker the cards are.
        """
        if self.isRoyalFlush():
            return "Royal Flush"
        elif self.isStraightFlush():
            return "Straight Flush"
        elif self.isFourOfAKind():
            return "4 of a Kind"
        elif self.isFullHouse():
            return "Full House"
        elif self.isFlush():
            return "Flush"
        elif self.isStraight():
            return "Straight"
        elif self.isThreeOfAKind():
            return "3 of a Kind"
        elif self.isTwoPair():
            return "Two Pair"
        elif self.isOnePair():
            return "One Pair"
        else:
            return "High Card"


if __name__ == '__main__':
    # Fill in the program to "do the work"
    pokerHandData = load_hands("pokerdata-16.csv")  # 10,000 poker hands to process
    # remember, pokerHandData is a list of strings. The strings are the "five cards" of a poker hand.

    # Generic algorithm idea. You need to refine it.
    # Iterate over the pokerHandData one at a time.
    # Determine what kind of poker hand it is.
    # Write the __str__ version of the poker hand and its hand type into the CSV output
    data = []
    for i in pokerHandData:
        hand = pokerHand(i)
        data.append([str(hand), hand.isWhat()])
    writeCSV("results.csv", data)
    #### BONUS #####
    #### There's a "Straight Flush" in the provided pokerhand-16.csv file. What are the cards in this hand?
    #### Answer it as a comment in your code.
    # The Straight Flush cards are
    # 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, Jack of Diamonds, Queen of Diamonds
