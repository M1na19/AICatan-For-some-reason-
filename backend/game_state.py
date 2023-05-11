import numpy as np
import queue

#doar eu si miezeu stiam ce inseamna codul asta cand l am scris, acum doar miezeu stie

config= [[(0,0)],
        [(0,1)],
        [(0,2),(1,10)],
        [(0,3),(1,9)],
        [(0,4),(1,8),(4,0)],
        [(0,5),(4,11)],
        [(0,6),(3,2),(4,10)],
        [(0,7),(3,1)],
        [(0,8),(3,0)],
        [(0,9)],
        [(0,10)],
        [(0,11)],
        
        [(1,0)],
        [(1,1)],
        [(1,2),(2,10)],
        [(1,3),(2,9)],
        [(1,4),(2,8),(5,0)],
        [(1,5),(5,11)],
        [(1,6),(4,2),(5,10)],
        [(1,7),(4,1)],
        [(1,11)],

        [(2,0)],
        [(2,1)],
        [(2,2)],
        [(2,3)],
        [(2,4),(6,0)],
        [(2,5),(6,11)],
        [(2,6),(5,2),(6,10)],
        [(2,7),(5,1)],
        [(2,11)],

        [(3,3),(4,9)],
        [(3,4),(4,8),(8,0)],
        [(3,5),(8,11)],
        [(3,6),(7,2),(8,10)],
        [(3,7),(7,1)],
        [(3,8),(7,0)],
        [(3,9)],
        [(3,10)],
        [(3,11)],

        [(4,3),(5,9)],
        [(4,4),(5,8),(9,0)],
        [(4,5),(9,11)],
        [(4,6),(8,2),(9,10)],
        [(4,7),(8,1)],

        [(5,3),(6,9)],
        [(5,4),(6,8),(10,0)],
        [(5,5),(10,11)],
        [(5,6),(9,2),(10,10)],
        [(5,7),(9,1)],

        [(6,1)],
        [(6,2)],
        [(6,3)],
        [(6,4),(11,0)],
        [(6,5),(11,11)],
        [(6,6),(10,2),(11,10)],
        [(6,7),(10,1)],

        [(7,3),(8,9)],
        [(7,4),(12,0),(8,8)],
        [(7,5),(12,11)],
        [(7,6),(12,10)],
        [(7,7)],
        [(7,8)],
        [(7,9)],
        [(7,10)],
        [(7,11)],

        [(8,3),(9,9)],
        [(8,4),(9,8),(13,0)],
        [(8,5),(13,11)],
        [(8,6),(13,10),(12,2)],
        [(8,7),(12,1)],

        [(9,3),(10,9)],
        [(9,4),(10,8),(14,0)],
        [(9,5),(14,11)],
        [(9,6),(14,10),(13,2)],
        [(9,7),(13,1)],

        [(10,3),(11,9)],
        [(10,4),(11,8),(15,0)],
        [(10,5),(15,11)],
        [(10,6),(15,10),(14,2)],
        [(10,7),(14,1)],

        [(11,1)],
        [(11,2)],
        [(11,3)],
        [(11,4)],
        [(11,5)],
        [(11,6),(15,2)],
        [(11,7),(15,1)],

        [(12,3),(13,9)],
        [(12,4),(13,8),(16,0)],
        [(12,5),(16,11)],
        [(12,6),(16,10)],
        [(12,7)],
        [(12,8)],
        [(12,9)],

        [(13,3),(14,9)],
        [(13,4),(14,8),(17,0)],
        [(13,5),(17,11)],
        [(13,6),(17,10),(16,2)],
        [(13,7),(16,1)],

        [(14,3),(15,9)],
        [(14,4),(15,8),(18,0)],
        [(14,5),(18,11)],
        [(14,6),(18,10),(17,2)],
        [(14,7),(17,1)],

        [(15,3)],
        [(15,4)],
        [(15,5)],
        [(15,6),(18,2)],
        [(15,7),(18,1)],

        [(16,3),(17,9)],
        [(16,4),(17,8)],
        [(16,5)],
        [(16,6)],
        [(16,7)],
        [(16,8)],
        [(16,9)],

        [(17,3),(18,9)],
        [(17,4),(18,8)],
        [(17,5)],
        [(17,6)],
        [(17,7)],

        [(18,3)],
        [(18,4)],
        [(18,5)],
        [(18,6)],
        [(18,7)]]
port_poz=[{3,8},{3,10},{12,8},{12,10},{1,0},{1,2},{6,0},{6,2},{15,4},{15,6}]
port_3_1poz=[{0,0},{0,10},{11,2},{11,4},{16,6},{16,8},{17,4},{17,6}]
echiv=dict()
for echi in config:
    for i in range(len(echi)):
        echiv[echi[i]]=[]
        for j in range(len(echi)):
            if i!=j:
                echiv[echi[i]].append(echi[j])
class piece:
    
    def __init__(self) -> None:
        self.name="none"
        self.player=-1
        self.tileinfo=(0,0)
        self.neigh=list()
    def __hash__(self) -> int:
        return hash(self.tileinfo)
    def __eq__(self, other):
        if isinstance(other, piece):
            return other.tileinfo==self.tileinfo or other.tileinfo in echiv[self.tileinfo]
    def tie(self,nod):
        self.neigh.append(nod)
        nod.neigh.append(self)
   
    def merge(list):
        z=piece()
        z.name="inlocuire"
        z.tileinfo=list[0].tileinfo
        for x in list:
            for n1 in range(len(x.neigh)):
                for n2 in range(len(x.neigh[n1].neigh)):
                    if(x.neigh[n1].neigh[n2]==x):
                        x.neigh[n1].neigh[n2]=z
        for x in list:
            z.neigh+=x.neigh
        z.neigh=unique_list(z.neigh)
        return z
    
class tile:
    def __init__(self,indx) -> None:
        self.index=indx
        self.value=0
        self.resource=0
        self.pieces=[piece() for i in range(12)]
        for i in range(len(self.pieces)):
            self.pieces[i].tie(self.pieces[i-1])
            self.pieces[i].tileinfo=(self.index,i)
            

class game_state:
    def __get_piece(self,tileinfo):
        return self.tiles[tileinfo[0]].pieces[tileinfo[1]]
    def __setup(self,tileconfig):
        for echi in config:
            plist=[]
            for element in echi:
                plist.append(self.__get_piece(element))
            result=piece.merge(plist)
            for element in echi:
                self.tiles[element[0]].pieces[element[1]]=result

        for i in range(len(tileconfig)):
            self.tiles[i].value=tileconfig[i][0]
            self.tiles[i].resource=tileconfig[i][1]
            if(tileconfig[i][1]==-1):
                self.hottile=i

    def __init__(self,tileconfig,playerturn,nrplayers):
        self.player_turn=playerturn
        self.number_of_players=nrplayers;
        self.hand=[[0 for j in range(5)] for i in range(nrplayers)]
        self.dezvoltari=[0]*5
        self.other_player_dezvoltari=[0]*(nrplayers-1)
        self.tiles=[tile(i) for i in range(19)]
        self.hottile=0
        self.players = [[None, None] for _ in range(nrplayers)]
        self.ports=[[0 for j in range(6)] for i in range(nrplayers)]
        self.__setup(tileconfig)
    def zar(self,zar):
        for i in range(len(self.tiles)):
            if self.tiles[i].value==zar and self.hottile!=i:
                for j in range(len(self.tiles[i].pieces)):
                    if self.tiles[i].pieces[j].name=="asezare":
                        self.hand[self.tiles[i].pieces[j].player][self.tiles[i].resource]+=1
                    elif self.tiles[i].pieces[j].name=="oras":
                        self.hand[self.tiles[i].pieces[j].player][self.tiles[i].resource]+=2
    def add_piece(self,name,player,tileinfo):

        self.tiles[tileinfo[0]].pieces[tileinfo[1]].name=name
        self.tiles[tileinfo[0]].pieces[tileinfo[1]].player=player

        if name=="asezare" or name=="oras": #daca e intr-o pozitie de port il aduag
            while(i<len(port_poz)):
                if(tileinfo==port_poz[i] or tileinfo in echiv[port_poz[i]] or tileinfo==port_poz[i+1] or tileinfo in echiv[port_poz[i+1]]):
                    self.ports[player][i]=1
                i+=2
            for port in port_3_1poz:
                if(port==tileinfo or tileinfo in echiv[port]):
                    self.ports[5]=1

        if name=="asezare":# la inceput il adaug in player ce tine grafu constructiilor
            if self.players[player][0]==None :
                self.players[player][0]=self.tiles[tileinfo[0]].pieces[tileinfo[1]]
            elif self.players[player][1]==None:
                self.players[player][1]=self.tiles[tileinfo[0]].pieces[tileinfo[1]] 

    def add_dezv(self,dezv,player):
        self.dezvoltari[dezv]+=1


def unique_list(fullist):
    result = []
    for element in fullist:
        if element not in result:
            result.append(element)
    return result
    
        