import pickle
import backend.game_state as gs
import backend.montecarlo as mc
import backend.features as f
import os
import asyncio
import random
import evaluatoare.TradeValue as tv
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
        game.zar(sum(answear))
    elif(rq=='playerData'):
        answear=(game.hand[player],dezvoltari[player])
    elif(rq=='getDezv'):
        if(f.can_buy(game,player,[0,0,1,1,1])):
            f.cost(game,[0,0,1,1,1],player)
        else:
            return []
        answear=f.dezvoltare()
        game.add_dezv(answear,player)
        dezvoltari[player][answear]+=1
    elif(rq=="AIaction"):
        loop=asyncio.get_event_loop()
        answear=loop.run_until_complete(mc.best_move(game).name)
    elif(rq=="AIstart"):
        pass
    elif(rq=='possibleDrumuri'):
        if(f.can_buy(game,player,[1,1,0,0,0])):
            f.cost(game,[1,1,0,0,0],player)
        else:
            return []
        answear=[]
        pieces=f.place_piece(game,player)
        for piece in pieces:
            if(piece.tileinfo[1]%2==1):
                answear.append(piece.tileinfo)
    elif(rq=='possibleAsezari'):
        if(f.can_buy(game,player,[1,1,1,1,0])):
            f.cost(game,[1,1,1,1,0],player)
        else:
            return []
        answear=[]
        pieces=f.place_piece(game,player)
        for piece in pieces:
            if(piece.tileinfo[1]%2==0):
                answear.append(piece.tileinfo)
    elif(rq=='possibleOrase'):
        if(f.can_buy(game,player,[0,0,2,0,3])):
            f.cost(game,[0,0,2,0,3],player)
        else:
            return []
        answear=f.upgradeable(game,player)
        for i in range(len(answear)):
            answear[i]=answear[i].tileinfo
    elif(rq=='longestRoad'):
        answear=game.biggestRoad
    elif(rq=='longestArmy'):
        f.celMaiMareDrum(game,player)
        answear=game.biggestArmy
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
    elif(rq=='discard'):
        answear=round(sum(game.hand[player])/2)
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
    elif(rq=="putData"):
        carti=info[0]
        dezv=info[1]
        game.hand[player]=carti
        dezvoltari[player]=dezv
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
        dezvoltari[player][2]-=1
        resources=info[0]
        for i in range(5):
            game.hand[player][i]+=resources[i]
    elif(rq=="monopol"):
        dezvoltari[player][4]-=1
        res=info[0]
        for i in range(game.number_of_players):
            if(i!=player):
                game.hand[player][res]+=game.hand[i][res]
                game.hand[i][res]=0
    elif(rq=="2drumuri"):
        dezvoltari[player][3]-=1
    elif(rq=="soldat"):
        dezvoltari[player][1]-=1
    elif(rq=='steal'):
        player2=info[0]
        if(sum(game.hand[player2])>0):
            card=random.randint(0,4)
            while(game.hand[player2][card]==0):
                card=random.randint(0,4)
            game.hand[player2][card]-=1
            game.hand[player][card]+=1
    elif(rq=="discard"):
        resources=info[0]
        for i in range(len(resources)):
            game.hand[player][i]-=resources[i]

    endState(game,dezvoltari)
def resolve_getInfo(rq,player,info):
    state=getState()
    game=state[0]
    dezvoltari=state[1]
    answear=[]
    if(rq=='playerInTile'):
        tile=int(info[0])
        answear=[0 for i in range(game.number_of_players)]
        for piece in game.tiles[tile].pieces:
            if(piece.name in ('asezare','oras') and player!=piece.player):
                answear[piece.player]=1
    
    elif(rq=="tradeProposal"):
        playerProposing=info[0]
        trade0=info[1]
        trade1=info[2]
        answear=False
        if(tv.checkTradeProposal(game,trade0,trade1,player,playerProposing)):
            answear=True
            for res in range(len(trade0)):
                game.hand[player][res]-=trade0[res]
                game.hand[playerProposing][res]+=trade0[res]
            for res in range(len(trade1)):
                game.hand[player][res]+=trade1[res]
                game.hand[playerProposing][res]-=trade1[res]
        


    endState(game,dezvoltari)
    return answear
#discard cards on 7 and steal a card(practic trade dar cu 0 resurse de o parte)