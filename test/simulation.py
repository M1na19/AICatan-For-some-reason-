# import game_state
import sys
sys.path.append('/home/mihai/Github/AICatan-For-some-reason-')
import TradeValue as tv
import CardValue as cv
import random as r
import math
def __randomResourceHand(hand):
    res=r.randint(0,4)
    while(hand[res]==0):
        res=r.randint(0,4)
    hand[res]-=1
    return res
def __inhand(myHand,ports,nrDrum,nrAsezari,nrOrase):
    if(myHand[4]>=3 and myHand[2]>=2 and nrAsezari>nrOrase):
        myHand[4]-=3
        myHand[2]-=2
        nrOrase+=1
        return "oras"
    if(myHand[0]>0 and myHand[1]>0 and myHand[2]>0 and myHand[3]>0 and nrDrum-nrAsezari>=2):
        myHand[0]-=1
        myHand[1]-=1
        myHand[2]-=1
        myHand[3]-=1
        nrAsezari+=1
        return "asezare"
    if(myHand[0]>0 and myHand[1]>0):
        myHand[0]-=1
        myHand[1]-=1
        nrDrum+=1
        return "drum"
    
def __randomize_trades(myHand,urHand):
    cardsOfferMax=min(sum(myHand),sum(urHand))
    if(cardsOfferMax==0):
        return None
    random=r.randint(-2*min(cardsOfferMax,3),2*min(cardsOfferMax,3))
    if(random<=3 and random>=-3):
        prop=1
    elif(random<=5 or random>=-5):
        prop=2*math.copysign(1,random)
    elif(random==6 or random==-6):
        prop=3*math.copysign(1,random)
    if(prop==1):
        return {__randomResourceHand(myHand),__randomResourceHand(urHand)}
    if(prop==2):
        offer=[__randomResourceHand(myHand),__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand)]
    if(prop==2):
        offer=[__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand),__randomResourceHand(urHand)]
    if(prop==3):
        offer=[__randomResourceHand(myHand),__randomResourceHand(myHand),__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand)]
    if(prop==2):
        offer=[__randomResourceHand(myHand)]
        back=[__randomResourceHand(urHand),__randomResourceHand(urHand),__randomResourceHand(urHand)]
    return {offer,back}
def __makeTrade(trade0,trade1,hand0,hand1):
    for res in trade0:
        hand1[res]+=1
    for res in trade1:
        hand0[res]+=1

#have to edit parameters in cardValue
#to do this must separate scores
#and also put tradeValue in a function
asezari=2
nrTurns=10
gamestate=None
#edit as u like
def simulate(prop):
    gamestate.zar()
    drum=[asezari,asezari]
    asezare=[asezari,asezari]
    orase=[0,0]
    while(nrTurns>0):
        __inhand(gamestate.hand[0],gamestate.ports[0],drum[0],asezare[0],orase[0])
        __inhand(gamestate.hand[1],gamestate.ports[1],drum[1],asezare[1],orase[1])
        tradeProposal=__randomize_trades(gamestate.hand[0],gamestate.hand[1])
        if(tv.checkTradeProposal(gamestate,tradeProposal[0],tradeProposal[1],0,1)==True):
            __makeTrade(tradeProposal[0],tradeProposal[1])
        nrTurns-=1
    return orase[0]-orase[1]*2+asezare[0]-asezare[1]+(drum[0]-drum[1])/2