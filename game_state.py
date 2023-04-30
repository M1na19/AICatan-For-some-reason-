import numpy as np
import queue
number_of_players=1
config=[[1,2,(3,4,5),(11,10,9)],
        [1,3,(5,6,7),(1,12,11)],
        [],
        [],
        [],
        []]
class piece:
    def __init__(self) -> None:
        self.name="none"
        self.player=0
        self.echiv=np.array(dtype=piece)
        self.neigh=np.array(dtype=piece)
    def tie(self,nod):
        self.neigh.append(nod)
        nod.neigh.append(self)
    def merge(x,y):
        x.echiv=y
        y.echiv=x
class tile:
    def __init__(self) -> None:
        self.value=0
        self.pieces=np.array(12,dtype=piece)
        for i in range(len(self.pieces)):
            self.pieces[i].tie(self.pieces[i-1])

    def merge(x,y,pozx,pozy):
        for i in range(len(pozx)):
            piece.merge(x.pieces[pozx],y.pieces[pozy])
            

class game_state:
    def __setup(self):
        tile.merge(self.tiles[1],self.tiles[2],(),())
    def __init__(self):
        self.hand=np.zeros(number_of_players,5,dtype=int)
        self.dezvoltari=np.array(5,dtype=int)
        self.other_player_dezvoltari=np.zeros(number_of_players-1,dtype=int)
        self.tiles=np.array(19,dtype=tile)
        self.__setup()
    def zar(self,zar):
        for i in range(len(self.tiles)):
            if self.tiles[i].value==zar:
                for j in range(len(self.tiles[i].pieces)):
                    if self.tiles[i].pieces[j].name=="sat":
                        self.hand[self.tiles[i].pieces[j].player]+=1
                    elif self.tiles[i].pieces[j].name=="oras":
                        self.hand[self.tiles[i].pieces[j].player]+=2
    def add_piece(self,name,player,tilenr,tileindx):
        self.tiles[tilenr].pieces[tileindx].name=name
        self.tiles[tilenr].pieces[tileindx].player=player
        for i in range(len(self.tiles[tilenr].pieces[tileindx].echiv)):
            self.tiles[tilenr].pieces[tileindx].echiv[i].name=name
            self.tiles[tilenr].pieces[tileindx].echiv[i].player=player

        