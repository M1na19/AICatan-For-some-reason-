import CardValue as cval
import copy
def checkTradeProposal(gamestate,Trade0,Trade1,player0,player1):
#town city road card
# 0 1 2 3
# lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
# tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule
# This is where the code begins
    totalvalue0=0
    totalvalue1=0
    simulatedGameState=copy.deepcopy(gamestate)
    for i in range(len(Trade1)):
        while(Trade1[i]>0):
            totalvalue0+=cval.cardEvaluator(simulatedGameState,player0)[Trade1[i]]
            Trade1[i]-=1
    for i in range(len(Trade0)):
        while(Trade0[i]>0):
            totalvalue1+=cval.cardEvaluator(simulatedGameState,player0)[Trade0[i]]
            Trade0[i]-=1

    if totalvalue0>totalvalue1:
        return True
    else:
        return False
