def BlackjackHighest(strArr):
  arrOfScores = list(map(getScoreOfCard, strArr))
  score = calculateScore(arrOfScores)
  maxValue = max(arrOfScores)
  maxIndex = arrOfScores.index(maxValue)
  if(score <= 11 and checkIfHandHasAce(strArr) > 0):
    return aboveOrBelowOrBlackJack(score + 10) + " " + "ace"
  return aboveOrBelowOrBlackJack(score) + " " + strArr[maxIndex]  

def calculateScore(arrOfValues):
  currentScore = sum(arrOfValues)
  #adjust scores to reflect real values
  for val in arrOfValues:
    if val == "king":
      currentScore -= 3
    elif val == "queen":
      currentScore -= 2
    elif val == "jack":
      currentScore -= 1
  return currentScore 

def checkIfHandHasAce(cards):
  return len([card for card in cards if card == "ace"])

def getScoreOfCard(card):
  dictOfCards = {
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
    "jack" : 11, #jack-king artifically higher to preserve ordering
    "queen" : 12,
    "king" : 13,
    "ace" : 1
  }
  return dictOfCards[card]

def aboveOrBelowOrBlackJack(score):
  if score == 21:
    return "blackjack"
  if score < 21:
    return "below"
  if score > 21:
    return "above"
  
# arr = ["four","ace","ten"]
arr = ["jack","king"]
# arr = ["four","ace","ten"]
print(BlackjackHighest(arr))