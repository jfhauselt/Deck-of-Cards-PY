import unittest
import pokerGame
import mainClasses

class Tests1(unittest.TestCase):
    def pairTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertTrue(pokerGame.isPair(mydeck))
        mydeck=mainClasses.Deck()
        mydeck.add(mainClasses.Card("clubs",10))
        mydeck.add( mainClasses.Card("hearts",9))
        self.assertFalse(pokerGame.isPair(mydeck))
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",9))
        mydeck.add(mainClasses.Card("clubs",10))
        mydeck.add(mainClasses.Card("clubs",9))
        pokerGame.isTwoPair(mydeck)
        self.assertTrue(pokerGame.isTwoPair(mydeck))
        self.assertFalse(pokerGame.isPair(mydeck))
    
    def threeOfAKindTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertTrue(pokerGame.isThreeOfAKind(mydeck))
        mydeck=mainClasses.Deck()
        mydeck.add(mainClasses.Card("clubs",10))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertFalse(pokerGame.isThreeOfAKind(mydeck))
        mydeck.add(mainClasses.Card("clubs","k"))
        self.assertFalse(pokerGame.isThreeOfAKind(mydeck))

    def fourOfAKindTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertFalse(pokerGame.isFourOfAKind(mydeck))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertTrue(pokerGame.isFourOfAKind(mydeck))


        

if __name__ == '__main__':
    unittest.main()
