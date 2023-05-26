import pickle
import backend.game_state as gs
import backend.montecarlo as mc
import backend.features as f
import os
import asyncio
import random
pickleLocation=os.path.abspath(".")+"/fullBackend/storage/state.pickle"

def getState():
    with open(pickleLocation,"rb") as read_state:
        game=pickle.load(read_state)
        dezvoltari=pickle.load(read_state)
        f.dezvoltari=dezvoltari
        read_state.close()
    f.dezvoltari=dezvoltari
    return (game,dezvoltari)
def endState(game,dezvoltari):
     
     with open(pickleLocation,"wb") as state:
            pickle.dump(game,state)
            pickle.dump(dezvoltari,state)
            state.close()


def start(sp,nr_p):
    config=f.random_config()
    game=gs.game_state(config,sp,nr_p)
    dezvoltari=[[0,0,0,0,0] for i in range(nr_p)]
    endState(game,dezvoltari)
    return config
def resolve_get(rq,player):
    state=getState()
    game=state[0]
    dezvoltari=state[1]
    answear=''
    if(rq=='zar'):
        answear=f.dice()
    elif(rq=='playerData'):
        answear=(game.hand[player],dezvoltari[player])
    elif(rq=='getDevCard'):
        answear=f.dezvoltare()
        game.add_dezv(answear,player)
    elif(rq=="AIaction"):
        loop=asyncio.get_event_loop()
        answear=loop.run_until_complete(mc.best_move(game).name)
    elif(rq=="AIstart"):
        pass
    elif(rq=="tradeProposal"):
        pass
    elif(rq=='possibleDrumuri'):
        answear=mc.place_piece(game,player)
        for piece in answear:
            if(piece.name!='drum'):
                answear.remove(piece)
        for i in range(len(answear)):
            answear[i]=answear[i].tileinfo
    elif(rq=='possibleAsezari'):
        answear=mc.place_piece(game,player)
        for piece in answear:
            if(piece.name!='asezare'):
                answear.remove(piece)
        for i in range(len(answear)):
            answear[i]=answear[i].tileinfo
    elif(rq=='possibleOras'):
        answear=mc.upgradeable(game,player)
        for i in range(len(answear)):
            answear[i]=answear[i].tileinfo
    elif(rq=='longestRoad'):
        answear=game.biggestRoad
    elif(rq=='longestArmy'):
        f.celMaiMareDrum(game,player)
        answear=game.biggestArmy
    elif(rq=='playerInTile'):
        pass
    elif(rq=='visiblePoints'):
        answear=game.constructi[0]*2+game.constructi[1]
        if(f.ceaMaiMareArmata(game,player)):
            answear+=2
        if(f.celMaiMareDrum(game,player)):
            answear+=2
    elif(rq=='pozThief'):
        answear=game.hottile
    elif(rq=='gameWon'):
        answear=False
        for i in range(game.number_of_players):
            if(f.winned(game,player)):
                answear=True
    endState(game,dezvoltari)
    return answear

def resolve_put(rq,player,info):
    state=getState()
    game=state[0]
    dezvoltari=state[1]
    if(rq=="placePiece"):
        name=info[0]
        tile=info[1]
        poz=info[2]
        game.add_piece(name,player,(tile,poz))
    elif(rq=="pas"):
          game.playerturn+=1
          game.playerturn%=(game.number_of_players)
    elif(rq=="playersTrade"):
          player2=info[0]
          resources1=info[1]# info as 0,0,0,0,1 with 1,0,0,0,0 asta inseamna un lemn pe o piatra
          resources2=info[2]
          for i in range(5):
            game.hand[player][i]-=resources1[i]
            game.hand[player][i]+=resources2[i]
            game.hand[player2][i]-=resources2[i]
            game.hand[player2][i]+=resources1[i]
    elif(rq=="moveThief"):
        newtile=info[0]
        game.hotile=newtile
    elif(rq=="gain2Resources"):
        resources=info[0]
        for i in range(5):
            game.hand[player][i]+=resources[i]
    elif(rq=="monopol"):
        res=info[0]
        for i in range(game.number_of_players):
            if(i!=player):
                game.hand[player][res]+=game.hand[i][res]
                game.hand[i][res]=0
    elif(rq=='steal'):
        player2=info[0]
        if(sum(game.hand[player2])>0):
            card=random.randint(0,4)
            while(game.hand[player2][card]==0):
                card=random.randint(0,4)
            game.hand[player2][card]-=1
    elif(rq=="discard"):
        resources=info[0]
        for i in range(len(resources)):
            game.hand[player][i]-=resources[i]

    endState(game,dezvoltari)

#discard cards on 7 and steal a card(practic trade dar cu 0 resurse de o parte)