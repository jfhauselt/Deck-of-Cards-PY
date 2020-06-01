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

def percentageTest():
    pairs = 0
    twoPair = 0
    three = 0
    four = 0
    straight = 0
    flush = 0
    royalFlush = 0
    trials = 10000
    for i in range(trials):
        mydeck = mainClasses.createDeck()
        mydeck.shuffle()
        myhand = mainClasses.createHand(mydeck)
        if pokerGame.isPair(myhand):
            pairs +=1
        if pokerGame.isTwoPair(myhand):
            twoPair += 1
        if pokerGame.isThreeOfAKind(myhand):
            three +=1
        if pokerGame.isFourOfAKind(myhand):
            four +=1
        if pokerGame.isStraight(myhand):
            straight +=1
        if pokerGame.isFlush(myhand):
            flush +=1
        if pokerGame.isRoyalFlush(myhand):
            pair +=1
    print ("Ran " + str(trials) + " trials")
    print("Results: ")    
    print("Pairs:" + str(pairs) + " " + str((pairs / trials) *100) +"%")
    print("Two Pairs:" + str(twoPair) + " " + str((twoPair / trials)*100) + "%")
    print("Three of a Kind:" + str(three) + " " + str((three / trials) *100 )+ "%")
    print("Four of a Kind:" + str(four) + " " + str((four / trials)*100)+"%")
    print("Straights:" + str(straight) + " " + str((straight / trials)*100)+"%")
    print("Flushes:" + str(flush) + " " + str((flush / trials)*100)+"%")
    print("Royal Flushes:" + str(royalFlush) + " " + str((royalFlush / trials)*100)+"%")

    



