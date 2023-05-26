import evaluatoare.CardValue as cval
import copy
def gainOfCards(gamestate,newcards,player):
    totalvalue=0
    for i in range(len(newcards)):
        totalvalue+=cval.cardEvaluator(gamestate,player)[newcards[i]]
        gamestate.hand[player][newcards[i]]+=1
    for i in range(len(newcards)):
        gamestate.hand[player][newcards[i]]-=1
    return totalvalue
def tradeBank(gamestate,Trade,resource,player):
    simulatedGameState=copy.deepcopy(gamestate)
    for i in range(len(Trade)):
        simulatedGameState.hand[player][Trade[i]]-=1
        totalvalue0=gainOfCards(simulatedGameState,[resource],player)-gainOfCards(simulatedGameState,Trade,player)
        if(totalvalue0>0):
            return True
        else:
            return False
def checkTradeProposal(gamestate,Trade0,Trade1,player0,player1):
#town city road card
# 0 1 2 3
# lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
# tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule
# This is where the code begins
    simulatedGameState=copy.deepcopy(gamestate)
    for i in range(len(Trade0)):
        simulatedGameState.hand[player0][Trade0[i]]-=1
    for i in range(len(Trade1)):
        simulatedGameState.hand[player1][Trade1[i]]-=1

    totalvalue0=gainOfCards(simulatedGameState,Trade1,player0)-gainOfCards(simulatedGameState,Trade0,player0)
    totalvalue1=gainOfCards(simulatedGameState,Trade0,player1)-gainOfCards(simulatedGameState,Trade1,player1)

    if totalvalue0>0 and totalvalue0-totalvalue1>-0.1:
        return True
    else:
        return False
