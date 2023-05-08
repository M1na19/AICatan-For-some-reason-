import random
from flask import jsonify
#import gamestate as gs

player_number=0
dezvoltari=[]
def random_config():
    tiles=19
    tileprop=[4,3,4,4,3,1]
    diceprop=[0,0,1,2,2,2,2,0,2,2,2,2,1]
    tileconfig=[]
    while tiles>0:
        r=random.randint(-1,4)
        d=random.randint(2,12)
        while(tileprop[r]<=0):
            r=random.randint(-1,4)
            tileprop[r]-=1
        if(r==-1):
            d=0
        else:
            while(diceprop[d]<=0):
                d=random.randint(2,12)
                diceprop[d]-=1
        tileconfig.append((d,r))
        tiles-=1
    return tileconfig
print(random_config())
def dice():
    return (random.randint(1,6),random.randint(1,6))

def dezvoltare():
    return random.randint(0,4)
#game=None
def resolve_action(action):
    if(action=="start"):
        config=random_config()
        #game=gs.gamestate(config)
        return jsonify(config)
    elif(action=="startPiece"):#pt ai
        pass
    elif(action=="playernumber"):
        dezvoltari=[0,0,0,0,0]*player_number
        pass
    elif(action=="playerData"):
        pass
    elif(action=="getAIaction"):
        #return jsonify(mc.bestmove())
        pass
    elif(action=="getDezvoltare"):
        pass
    elif(action=="joacaDezvoltare"):#split into more
        pass
    elif(action=="tradeProposal"):#pt ai
        pass#add counter proposal
#put actions:add Piece,pas,trade intre playeri
#get actions:zar
