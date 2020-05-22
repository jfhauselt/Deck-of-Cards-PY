import mainClasses
import pokerGame

def testShuffle():
    for i in range(1000):
        mydeck = mainClasses.createDeck()
        mydeck.shuffle()
    print("created 1000 decks")

def testDraw():
    mydeck = mainClasses.createDeck()
    myHand = mainClasses.createHand(mydeck)
    for i in myHand:
        print(i)


    



