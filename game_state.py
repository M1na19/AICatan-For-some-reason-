import numpy as np
import queue
number_of_players=1
config= [[1,2,(3,4,5),(11,10,9)],
        [1,5,(5,6,7),(1,12,11)],
        [1,4,(9,8,7),(1,2,3)],
        [2,3,(3,4,5),(11,10,9)],
        [2,5,(9,8,7),(1,2,3)],
        [2,6,(7,6,5),(1,12,11)],
        [3,7,(5,6,7),(1,12,11)],
        [3,6,(9,8,7),(1,2,3)],
        [4,5,(3,4,5),(11,10,9)],
        [4,9,(5,6,7),(1,12,11)],
        [4,8,(9,8,7),(1,2,3)],
        [5,6,(3,4,5),(11,10,9)],
        [5,10,(5,6,7),(1,12,11)],
        [5,9,(9,8,7),(1,2,3)],
        [6,7,(3,4,5),(11,10,9)],
        [6,11,(5,6,7),(1,12,11)],
        [6,10,(9,8,7),(1,2,3)],
        [7,12,(5,6,7),(1,12,11)],
        [7,11,(9,8,7),(1,2,3)],
        [8,9,(3,4,5),(11,10,9)],
        [8,13,(5,6,7),(1,12,11)],
        [9,10,(3,4,5),(11,10,9)],
        [9,14,(5,6,7),(1,12,11)],
        [9,13,(9,8,7),(1,2,3)],
        [10,11,(3,4,5),(11,10,9)],
        [10,15,(5,6,7),(1,12,11)],
        [10,14,(9,8,7),(1,2,3)],
        [11,12,(3,4,5),(11,10,9)],
        [11,16,(5,6,7),(1,12,11)],
        [11,15,(9,8,7),(1,2,3)],
        [12,16,(9,8,7),(1,2,3)],
        [13,14,(3,4,5),(11,10,9)],
        [13,17,(5,6,7),(1,12,11)],
        [14,15,(3,4,5),(11,10,9)],
        [14,18,(5,6,7),(1,12,11)],
        [14,17,(9,8,7),(1,2,3)],
        [15,16,(3,4,5),(11,10,9)],
        [15,19,(5,6,7),(1,12,11)],
        [15,18,(9,8,7),(1,2,3)],
        [16,19,(9,8,7),(1,2,3)]]
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
        for i in range(len(config)):
            tile.merge(self.tiles[config[i][0]],self.tiles[config[i][1]],config[i][2],config[i][3])
    def __init__(self):
        self.hand=np.zeros((number_of_players,5),dtype=int)
        self.dezvoltari=np.array(5,dtype=int)
        self.other_player_dezvoltari=np.zeros(number_of_players-1,dtype=int)
        self.tiles=np.array(19,dtype=tile)
        self.players=np.array(number_of_players,dtype=(piece,piece))
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

        