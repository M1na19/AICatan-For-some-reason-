import pickle
import backend.game_state as gs
import backend.montecarlo as mc
import backend.features as f
import os

game=None
dezvoltari=[]
    


def start(sp,nr_p):
    config=f.random_config()
    game=gs.game_state(config,sp)
    dezvoltari=nr_p*[0,0,0,0,0]
    print(os.path.abspath('./storage'))
    with open("./storage/state.pickle","wb") as state:
            pickle.dump(game,state)
            pickle.dump(dezvoltari,state)
            state.close()
    return config
def resolve_get(rq):
    with open("./storage/state.pickle","rb") as read_state:
        game=pickle.load(read_state)
        dezvoltari=pickle.load(read_state)
        read_state.close()
    if(rq=='zar'):
          return f.dice();
        
    with open("./storage/state.pickle","wb") as state:
            pickle.dump(game,state)
            pickle.dump(dezvoltari,state)
            state.close()

def resolve_put(rq):
    with open("./storage/state.pickle","rb") as read_state:
        game=pickle.load(read_state)
        dezvoltari=pickle.load(read_state)
        read_state.close()
    with open("./storage/state.pickle","wb") as state:
            pickle.dump(game,state)
            pickle.dump(dezvoltari,state)
            state.close()
#put actions:joacadezvoltare,add Piece,pas,trade intre playeri,playernumber
#get actions:getdezvoltare,get ai action,startpiece,playerdata,start,zar,tradeproposal
