#john Hauselt
import random
import testCase
import mainClasses
import pokerGame
#main

testCase.testShuffle()
testCase.testDraw()

mydeck = mainClasses.createDeck()
mydeck.shuffle()
myhand = mainClasses.createHand(mydeck)
for item in myhand:
    print(item)
print(pokerGame.isPair(mydeck))

