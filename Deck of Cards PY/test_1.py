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
        mydeck.add(mainClasses.Card("clubs","K"))
        self.assertFalse(pokerGame.isThreeOfAKind(mydeck))

    def fourOfAKindTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertFalse(pokerGame.isFourOfAKind(mydeck))
        mydeck.add( mainClasses.Card("hearts",10))
        self.assertTrue(pokerGame.isFourOfAKind(mydeck))

    def flushTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts",10))
        mydeck.add( mainClasses.Card("hearts","J"))
        mydeck.add( mainClasses.Card("hearts","K"))
        mydeck.add( mainClasses.Card("hearts","Q"))
        self.assertTrue(pokerGame.isFlush(mydeck))
        mydeck.add( mainClasses.Card("clubs","Q"))
        self.assertFalse(pokerGame.isFlush(mydeck))

    def straightTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","2"))
        mydeck.add( mainClasses.Card("hearts",3))
        mydeck.add( mainClasses.Card("hearts",4))
        mydeck.add( mainClasses.Card("hearts",5))
        self.assertTrue(pokerGame.isStraight(mydeck))
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","Q"))
        mydeck.add( mainClasses.Card("hearts","j"))
        mydeck.add( mainClasses.Card("hearts","10"))
        mydeck.add( mainClasses.Card("hearts","K"))
        self.assertFalse(pokerGame.isStraight(mydeck))
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","Q"))
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","4"))
        mydeck.add( mainClasses.Card("hearts","2"))
        self.assertFalse(pokerGame.isStraight(mydeck))

    def royalFlushTest(self):
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","10"))
        mydeck.add( mainClasses.Card("hearts","J"))
        mydeck.add( mainClasses.Card("hearts","Q"))
        mydeck.add( mainClasses.Card("hearts","K"))
        self.assertTrue(pokerGame.isFlush(mydeck))
        self.assertTrue(pokerGame.isRoyalFlush(mydeck))
        mydeck = mainClasses.Deck()
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","A"))
        mydeck.add( mainClasses.Card("hearts","Q"))
        mydeck.add( mainClasses.Card("hearts","K"))
        mydeck.add( mainClasses.Card("hearts","J"))
        mydeck.add( mainClasses.Card("hearts","10"))
        self.assertFalse(pokerGame.isRoyalFlush(mydeck))



        

if __name__ == '__main__':
    unittest.main()
