import numpy as np
number_of_players=1

class tile:
    #because easier
    def __init__(self):
        self.num=0
        self.resource="none"
        self.pieces=np.array(12)
        self.mappoz=(0,0)

class player_structure:
 #e pur si simplu un graf care are doua tipuri de noduri
    class drum:
        def __init__(self):
            self.player=0
            self.poz=(tile(),0)
            self.piece="none"
        def __init__(self,pozition,name,player):
            self.player=player
            self.poz=pozition
            self.isdrum=True
        def get_points(self):
            points=np.array(self.poz[0].pieces[self.poz[1]-1],self.poz[0].pieces[self.poz[1]+1])
        def get_muchi(self):
            muchi=np.array(self.poz[0].pieces[self.poz[1]-2],self.poz[0].pieces[self.poz[1]+2])

    #asta e pt drumuri ca stau pe muchi nu pe colturi

    class oras:
        def __init__(self):
            self.player=0
            self.poz=(tile(),0)
            self.piece="none"
        def __init__(self,pozition,name,player):
            self.poz=pozition
            self.piece=name
            self.player=player
        def get_muchi(self):
            pass
    #asta e pt orase si asezari pe colturi

    def __init__(self):
        self.root=player_structure.point()
        self.kids=np.array()

    def add(self,parent,piece,pozition,player):
        if(parent==None):
            self.root.poz=pozition
            self.root.piece=piece
        elif(piece!='drum'):
            parent.kids.add(player_structure.point(pozition,piece))
        else:
            parent.kids.add(player_structure.muchie(pozition,piece))
    
    def upgrade(loc):
        if(loc.piece=="asezare"):
            loc.piece="oras"


class mapconfig:
    def __init__(self):
        self.map=np.array([tile(),tile(),tile()],
                          [tile(),tile(),tile(),tile()],
                          [tile(),tile(),tile(),tile(),tile()],
                          [tile(),tile(),tile(),tile()],
                          [tile(),tile(),tile()])
        self.infrastructure=np.array(number_of_players)

    def add_piece(self,player,parent,pozition,piece):
        self.infrastructure[player].add(parent,piece,pozition)
        self.map[pozition[0].mappoz[0]][[pozition[0].mappoz[1]]].pieces[pozition[1]].piece=piece

class game_state:
    def __init__(self):
        self.hand=np.zeros(number_of_players,5)
        self.dezvoltari=np.array(5)
        self.other_player_dezvoltari=np.zeros(number_of_players-1)
        config=mapconfig()
    def zar(self,x):
        for i in range(len(self.config.map)):
            for j in range(len(self.config.map[i])):
                if(self.config.map[i][j][0].num==x):
                    for k in range (len(self.config.map[i][j][0].pieces)):
                        if(self.config.map[i][j][0].pieces[k].piece=="asezare"):
                            self.hand[self.config.map[i][j][0].pieces[k].player]+=1
                        if(self.config.map[i][j][0].pieces[k].piece=="oras"):
                            self.hand[self.config.map[i][j][0].pieces[k].player]+=2