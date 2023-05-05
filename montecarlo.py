import queue
import time
import heapq
import numpy as np
import game_state as gs
player_me=int()
decision=2
class node:
    def __init__(self,name,state,parent):
        self.action=name
        self.value=0
        self.depth=0
        self.state=state
        self.parent=parent
        self.kids=list()
    def __lt__(self,other):
        return self.depth<other.depth
    def make_kids(self):
        if(self.action!=None):
            node.do_action(self)
        moves=find_moves(self.state,self.state.player_turn)
        for i in range(len(moves)):
            if(type(moves[i])==gs.game_state):
                self.kids.append(node(None,moves[i],self))
                self.kids[-1].depth=self.depth+1
            elif(type(moves[i])==str):
                self.kids.append(node(moves[i],None,self))
                self.kids[-1].depth=self.depth
                
    
    #aici daca am spre ex oponentul joaca o dezvoltare nu pot sa stiu ce dezvoltare va juca
    #de acea voi ramifica in toate dezvoltarile si valoare nodului finala va fi media posibilitatilor
    def do_action(X):
        pass
            

class MonteCarlo_tree:
    def __init__(self,startstate):
        self.start=node("start",startstate,None)

#ma uit unde pot sa pun drum sau asezare
#am verificat,pare ca functioneaza
def place_piece(state:gs.game_state,player:int):
    to_visit=list()
    visited=dict()
    q=queue.Queue()
    q.put(state.players[player][0])
    q.put(state.players[player][1])
    while not q.empty():
        now=q.get()
        visited[now]=True
        for ngh in now.neigh:
            if(ngh.player==-1):
                to_visit.append(ngh)
            if (not ngh in visited or visited[ngh]==False) and (ngh.player==player or ngh.tileinfo[1]%2==0):
                q.put(ngh)
                visited[ngh]=True
    return to_visit

#vad daca pot sa pun asezare
def check_avail(piece,depth):
    condition=True
    if(depth>0):
        for i in range(len(piece.neigh)):
            if(piece.neigh[i].name=="asezare"):
                condition=False
            condition=condition and check_avail(piece.neigh[i],depth-1)
    return condition

        

        

#ma uit unde pot sa pun oras
#am verificat,pare ca functioneaza
def upgradeable(state:gs.game_state,player:int):
    to_upgrade=list()
    visited=dict()
    q=queue.Queue()
    q.put(state.players[player][0])
    q.put(state.players[player][1])
    while not q.empty():
        now=q.get()
        visited[now]=True
        if now.name=="asezare":
            to_upgrade.append(now)
        for nod in now.neigh:
            if (not nod in visited or visited[nod]==False) and (nod.player==player or nod.tileinfo[1]%2==0):
                q.put(nod)
                visited[nod]=True
    return to_upgrade

#toate mutarile posibile, btw fuck u mache trb efectiv sa facem sah

def find_moves(state:gs.game_state,player:int):
    moves=list()
    piece_options=place_piece(state,player)

    #cumpar drum
    if(state.hand[player][0]>0 and state.hand[player][1]>0):
        new_state=state.copy()
        new_state.hand[player][0]-=1
        new_state.hand[player][1]-=1
        for i in range(len(piece_options)):
            if piece_options[i].tileinfo[1]%2==0:
                moves.append(new_state.copy().add_piece("drum",player,piece_options[i].tileinfo))
    
    #cumpar asezare
    if(state.hand[player][0]>0 and state.hand[player][1]>0 and state.hand[player][2]>0 and state.hand[player][3]>0):
        new_state=state.copy()
        new_state.hand[player][0]-=1
        new_state.hand[player][1]-=1
        new_state.hand[player][2]-=1
        new_state.hand[player][3]-=1
        for i in range(len(piece_options)):
            if(piece_options[i].tileinfo[1]%2==1 and check_avail(piece_options[i])):
                moves.append(new_state.copy().add_piece("asezare",player,piece_options[i].tileinfo))
    
    #cumpar oras
    upgrade_options=upgradeable(state,player)
    if state.hand[player][2]>=2 and state.hand[player][4]>=3:
        new_state=state.copy()
        new_state.hand[player][2]-=2
        new_state.hand[player][4]-=3
        for i in range(len(upgrade_options)):
            moves.append(new_state.copy().add_piece("oras",player,piece_options[i].tileinfo))
    
    #cumpar dezvoltare
    if state.hand[player][2]>=1 and state.hand[player][3]>=1 and state.hand[player][4]>=1:
        new_state=state.copy()
        new_state.hand[player][2]-=1
        new_state.hand[player][3]-=1
        new_state.hand[player][4]-=1
        moves.append("dezvoltare")
    
    #daca sunt eu folosesc hot 
    if(player==player_me and state.dezvoltari[1]>0):
        new_state=state.copy()
        new_state.dezvoltari[1]-=1
        moves.append("hot")

    #daca sunt eu folosesc 2 resurse
    if(player==player_me and state.dezvoltari[2]>0):
        new_state=state.copy()
        new_state.dezvoltari[2]-=1
        moves.append("2 resurse")
    
    #daca sunt eu folosesc 2 drumuri
    if(player==player_me and state.dezvoltari[3]>0):
        new_state=state.copy()
        new_state.dezvoltari[3]-=1
        moves.append("2 drumuri")

    #daca sunt eu folosesc monopol
    if(player==player_me and state.dezvoltari[4]>0):
        new_state=state.copy()
        new_state.dezvoltari[4]-=1
        moves.append("monopol")
    
    #ceilalti playeri dezvoltari
    if(player!=player_me):
        moves.append("oponent_dezvoltare")

    #go nuts
    moves.append("trading")
    return moves
        
def best_move(gamestate):
    starttime=time.time()
    mc=MonteCarlo_tree(gamestate)
    leafs=[mc.start]
    while(time.time()-starttime<decision):
        pass






            


            



    

