import pickle
import backend.game_state as gs
import backend.montecarlo as mc
import backend.features as f
game=None
dezvoltari=[]
def getState():
    with open("./storage/state.pickle","rb") as read_state:
        game=pickle.load(read_state)
        dezvoltari=pickle.load(read_state)
        read_state.close()
def endState():
     with open("./storage/state.pickle","wb") as state:
            pickle.dump(game,state)
            pickle.dump(dezvoltari,state)
            state.close()


def start(sp,nr_p):
    getState()
    config=f.random_config()
    game=gs.game_state(config,sp,nr_p)
    dezvoltari=nr_p*[0,0,0,0,0]
    endState()
    return config
def resolve_get(rq,player,info):
    getState()
    answear=''
    if(rq=='zarResurse'):
        answear=f.dice()
        game.zar(answear)
    elif(rq=='zar'):
        answear=f.dice()
    elif(rq=='playerData'):
        answear=(game.hand[player],dezvoltari[player])
    elif(rq=='getDevCard'):
        answear=f.dezvoltare()
        game.add_dezv(answear,player)
    elif(rq=="AIaction"):
        answear=mc.best_move(game)
    elif(rq=="AIstart"):
        pass
    elif(rq=="tradeProposal"):
        pass
    elif(rq=='possiblePiecePlace'):
        answear=mc.place_piece(game,player)
        name=info.get("name")
        for piece in answear:
            if(piece.name!=name):
                answear.remove(piece)
        for i in range(len(answear)):
            answear[i]=answear[i].tileinfo
    endState()
    return answear

def resolve_put(rq,player,info):
    getState()
    if(rq=="placePiece"):
        name=info.get('name')
        tile=info.get('tile')
        poz=info.get('poz')
        game.add_piece(name,player,(tile,poz))
    elif(rq=="pas"):
          game.playerturn+=1
          game.playerturn%=(dezvoltari.count()+1)
    elif(rq=="playersTrade"):
          player2=info.get('otherPlayer')
          resources1=info.get(resources1)# info as 0,0,0,0,1 with 1,0,0,0,0 asta inseamna un lemn pe o piatra
          resources2=info.get(resources2)
          for i in range(5):
            game.hand[player][i]-=resources1[i]
            game.hand[player][i]+=resources2[i]
            game.hand[player2][i]-=resources2[i]
            game.hand[player2][i]+=resources1[i]
    elif(rq=="moveThief"):
        newtile=info.get('hottile')
        game.hotile=newtile
    elif(rq=="gain2Resources"):
        resources=info.get('resources')
        for i in range(5):
            game.hand[player][i]+=resources[i]
    elif(rq=="place2Drum"):
        tile1=info.get('tile1')
        poz1=info.get('poz1')
        tile2=info.get('tile2')
        poz2=info.get('poz2')
        game.add_piece("drum",player,(tile1,poz1))
        game.add_piece("drum",player,(tile2,poz2))
    elif(rq=="monopol"):
        res=info.get('resource')
        for i in range(game.number_of_players):
            if(i!=player):
                game.hand[player][res]+=game.hand[i][res]
                game.hand[i][res]=0
    endState()
    return

#discard cards on 7 and steal a card(practic trade dar cu 0 resurse de o parte)