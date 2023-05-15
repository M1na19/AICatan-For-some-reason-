import sys
sys.path.append('/home/mihai/Github/AICatan-For-some-reason-')
import evaluatoare.TradeValue as tv
import evaluatoare.CardValue as cv
import backend.game_state as gs
import backend.features as ft
import random as r
import math

def __randomResourceHand(hand):
    res=r.randint(0,4)
    while(hand[res]==0):
        res=r.randint(0,4)
    return res
def __inhand(myHand,nrDrum,nrAsezari,nrOrase,player):
    if(myHand[4]>=3 and myHand[2]>=2 and nrAsezari[player]>nrOrase[player]):
        myHand[4]-=3
        myHand[2]-=2
        nrOrase[player]+=1
        return "oras"
    if(myHand[0]>0 and myHand[1]>0 and myHand[2]>0 and myHand[3]>0 and nrDrum[player]-nrAsezari[player]>=2):
        myHand[0]-=1
        myHand[1]-=1
        myHand[2]-=1
        myHand[3]-=1
        nrAsezari[player]+=1
        return "asezare"
    if(myHand[0]>0 and myHand[1]>0):
        myHand[0]-=1
        myHand[1]-=1
        nrDrum[player]+=1
        return "drum"
    
def __randomize_trades(myHand,urHand):
    cardsOfferMax=min(sum(myHand),sum(urHand))
    if(cardsOfferMax==0):
        return None
    random=r.randint(-2*min(cardsOfferMax,3),2*min(cardsOfferMax,3))
    if(random<=3 and random>=-3):
        prop=1
    elif(random<=5 and random>=-5):
        prop=2*math.copysign(1,random)
    elif(random==6 or random==-6):
        prop=3*math.copysign(1,random)
    if(prop==1):
        return ([__randomResourceHand(myHand)],[__randomResourceHand(urHand)])
    if(prop==2):
        offer=[__randomResourceHand(myHand),__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand)]
    if(prop==-2):
        offer=[__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand),__randomResourceHand(urHand)]
    if(prop==3):
        offer=[__randomResourceHand(myHand),__randomResourceHand(myHand),__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand)]
    if(prop==-3):
        offer=[__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand),__randomResourceHand(urHand),__randomResourceHand(urHand)]
    return (offer,back)
def __makeTrade(trade0,trade1,hand0,hand1):
    for res in trade0:
        hand1[res]+=1
    for res in trade1:
        hand0[res]+=1
def __checkPortsTrade(gamestate,ports,player):
    for i in range(len(ports)-1):
        if(ports[i]==1):
            for j in range(5):
                if(gamestate.hand[player][i]>=2 and tv.tradeBank(gamestate,[i,i],j,player) ):
                    gamestate.hand[player][i]-=2
                    gamestate.hand[player][j]+=1
    if(ports[5]==1):
        for i in range(5):
            for j in range(5):
                if(gamestate.hand[player][i]>=3 and tv.tradeBank(gamestate,[i,i,i],j,player)):
                    gamestate.hand[player][i]-=3
                    gamestate.hand[player][j]+=1
    for i in range(5):
        for j in range(5):
            if(gamestate.hand[player][i]>=4 and tv.tradeBank(gamestate,[i,i,i,i],j,player)):
                gamestate.hand[player][i]-=4
                gamestate.hand[player][j]+=1

#have to edit parameters in cardValue
#to do this must separate scores
#and also put tradeValue in a function
asezari=2

def makeGame(gamestate):
    #random bulshit go
    gamestate.add_piece('asezare',0,(r.randint(0,18),r.randint(0,5)*2))
    gamestate.add_piece('asezare',0,(r.randint(0,18),r.randint(0,5)*2))
    gamestate.add_piece('asezare',1,(r.randint(0,18),r.randint(0,5)*2))
    gamestate.add_piece('asezare',1,(r.randint(0,18),r.randint(0,5)*2))
#edit as u like
def simulate(prop,nrTurns):
    gamestate=gs.game_state(ft.random_config(),0,2)
    makeGame(gamestate)
    cv.weightPort=prop[0]
    cv.weightRareness=prop[1]
    cv.weightUsefull=prop[2]
    drum=[0,0]
    asezare=[asezari,asezari]
    orase=[0,0]
    while(nrTurns>0):
        gamestate.zar(sum(ft.dice()))
        __inhand(gamestate.hand[0],drum,asezare,orase,0)
        __inhand(gamestate.hand[1],drum,asezare,orase,1)
        tradeProposal=__randomize_trades(gamestate.hand[0],gamestate.hand[1])
        __checkPortsTrade(gamestate,gamestate.ports[0],0)
        __checkPortsTrade(gamestate,gamestate.ports[1],1)
        if(tradeProposal!=None and tv.checkTradeProposal(gamestate,tradeProposal[0],tradeProposal[1],0,1)==True):
            __makeTrade(tradeProposal[0],tradeProposal[1],gamestate.hand[0],gamestate.hand[1])
        nrTurns-=1
    return (orase[0]-orase[1])*2+asezare[0]-asezare[1]+(drum[0]-drum[1])/2