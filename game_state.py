import numpy as np
import queue
number_of_players=1
config= [[0,1,(2,3,4),(10,9,8)],
        [0,4,(4,5,6),(0,11,10)],
        [0,3,(8,7,6),(0,1,2)],
        [1,2,(2,3,4),(10,9,8)],
        [1,4,(8,7,6),(0,1,2)],
        [1,5,(7,6,5),(0,11,10)],
        [2,6,(4,5,6),(0,11,10)],
        [2,5,(8,7,6),(0,1,2)],
        [3,4,(2,3,4),(10,9,8)],
        [3,8,(4,5,6),(0,11,10)],
        [3,7,(8,7,6),(0,1,2)],
        [4,5,(2,3,4),(10,9,8)],
        [4,9,(4,5,6),(0,11,10)],
        [4,8,(8,7,6),(0,1,2)],
        [5,6,(2,3,4),(10,9,8)],
        [5,10,(4,5,6),(0,11,10)],
        [5,9,(8,7,6),(0,1,2)],
        [6,11,(4,5,6),(0,11,10)],
        [6,10,(8,7,6),(0,1,2)],
        [7,8,(2,3,4),(10,9,8)],
        [7,12,(4,5,6),(0,11,10)],
        [8,9,(2,3,4),(10,9,8)],
        [8,13,(4,5,6),(0,11,10)],
        [8,12,(8,7,6),(0,1,2)],
        [9,10,(2,3,4),(10,9,8)],
        [9,14,(4,5,6),(0,11,10)],
        [9,13,(8,7,6),(0,1,2)],
        [10,11,(2,3,4),(10,9,8)],
        [10,15,(4,5,6),(0,11,10)],
        [10,14,(8,7,6),(0,1,2)],
        [11,15,(8,7,6),(0,1,2)],
        [12,13,(2,3,4),(10,9,8)],
        [12,16,(4,5,6),(0,11,10)],
        [13,14,(2,3,4),(10,9,8)],
        [13,17,(4,5,6),(0,11,10)],
        [13,16,(8,7,6),(0,1,2)],
        [14,15,(2,3,4),(10,9,8)],
        [14,18,(4,5,6),(0,11,10)],
        [14,17,(8,7,6),(0,1,2)],
        [15,18,(8,7,6),(0,1,2)]]
class piece:
    def __init__(self) -> None:
        self.name="none"
        self.player=0
        self.tileinfo=(0,0)
        self.neigh=[]
    def tie(self,nod):
        self.neigh.append(nod)
        nod.neigh.append(self)
    def merge(x,y):
        for i in range(len(y.neigh)):
            for j in range(len(y.neigh[i].neigh)):
                if y.neigh[i].neigh[j]==y:
                    y.neigh[i].neigh[j]=x
        x.neigh+=y.neigh
        y=x
class tile:
    def __init__(self) -> None:
        self.index=0
        self.value=0
        self.resource=0
        self.pieces=[piece() for i in range(12)]
        for i in range(len(self.pieces)):
            self.pieces[i].tie(self.pieces[i-1])
            self.pieces[i].tileinfo=(self.index,i)

    def merge(x,y,pozx,pozy):
        for i in range(len(pozx)):
            piece.merge(x.pieces[pozx[i]],y.pieces[pozy[i]])
            

class game_state:
    def __setup(self,tileconfig):
        for i in range(len(self.tiles)):
            self.tiles[i].index=i
        for i in range(len(config)):
            tile.merge(self.tiles[config[i][0]],self.tiles[config[i][1]],config[i][2],config[i][3])
        for i in range(len(tileconfig)):
            self.tiles[i].value=tileconfig[i][0]
            self.tiles[i].resource=tileconfig[i][1]
    def __init__(self,tileconfig,playerturn):
        self.player_turn=playerturn
        self.hand=[[0 for j in range(5)] for i in range(number_of_players)]
        self.dezvoltari=[0]*(number_of_players)
        self.other_player_dezvoltari=[0]*(number_of_players-1)
        self.tiles=[tile() for i in range(19)]
        self.players=number_of_players*[(None,None)]
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



        