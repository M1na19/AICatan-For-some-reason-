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
        self.tileinfo=(0,0)
        self.neigh=list()
    def tie(self,nod):
        self.neigh.append(nod)
        nod.neigh.append(self)
    def merge(x,y):
        for i in range(len(y.neigh)):
            for j in range(y.neigh[i].neigh):
                if y.neigh[i].neigh[j]==y:
                    y.neigh[i].neigh[j]=x
        x.neigh+=y.neigh
        y=x
class tile:
    def __init__(self) -> None:
        self.index=0
        self.value=0
        self.resource=0
        self.pieces=np.array(12,dtype=piece)
        for i in range(len(self.pieces)):
            self.pieces[i].tie(self.pieces[i-1])
            self.pieces[i].tileinfo=(self.index,i)

    def merge(x,y,pozx,pozy):
        for i in range(len(pozx)):
            piece.merge(x.pieces[pozx],y.pieces[pozy])
            

class game_state:
    def __setup(self,tileconfig):
        for i in range(self.tiles):
            self.tiles[i].index=i
        for i in range(len(config)):
            tile.merge(self.tiles[config[i][0]],self.tiles[config[i][1]],config[i][2],config[i][3])
        for i in range(len(tileconfig)):
            self.tiles[i].value=tileconfig[0]
            self.tiles[i].resource=tileconfig[1]
    def __init__(self,tileconfig,playerturn):
        self.player_turn=playerturn
        self.hand=np.zeros((number_of_players,5),dtype=int)
        self.dezvoltari=np.array(5,dtype=int)
        self.other_player_dezvoltari=np.zeros(number_of_players-1,dtype=int)
        self.tiles=np.array(19,dtype=tile)
        self.players=np.array(number_of_players,dtype=(piece,piece))
        self.__setup(tileconfig)
    def zar(self,zar):
        for i in range(len(self.tiles)):
            if self.tiles[i].value==zar:
                for j in range(len(self.tiles[i].pieces)):
                    if self.tiles[i].pieces[j].name=="sat":
                        self.hand[self.tiles[i].pieces[j].player][self.tiles[i].resource]+=1
                    elif self.tiles[i].pieces[j].name=="oras":
                        self.hand[self.tiles[i].pieces[j].player][self.tiles[i].resource]+=2
    def add_piece(self,name,player,tileinfo):
        self.tiles[tileinfo[0]].pieces[tileinfo[1]].name=name
        self.tiles[tileinfo[0]].pieces[tileinfo[1]].player=player
    def add_dezv(self,dezv,player):
        self.dezvoltari[dezv]+=1



        