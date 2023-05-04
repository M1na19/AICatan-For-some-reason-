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
    def make_kids(nod):
        if(nod.action!=None):
            node.do_action(nod)
        moves=find_moves(nod)
        for i in range(len(moves)):
            if(type(moves[i])==gs.game_state):
                nod.kids.append(None,moves[i],nod)
                nod.kids[-1].depth=nod.depth+1
            elif(type(moves[i])==str):
                nod.kids.append(moves[i],None,nod)
                nod.kids[-1].depth=nod.depth
                
    
    #aici daca am spre ex oponentul joaca o dezvoltare nu pot sa stiu ce dezvoltare va juca
    #de acea voi ramifica in toate dezvoltarile si valoare nodului finala va fi media posibilitatilor
    def do_action():
        pass
            

class MonteCarlo_tree:
    def __init__(self,startstate):
        self.start=node("start",startstate,None)

#ma uit unde pot sa pun drum sau asezare

def place_piece(state:gs.game_state,player:int):
    to_visit=list()
    visited=dict()
    q=queue.Queue()
    q.put(state.players[player])
    while not q.empty():
        now=q.get()
        for i in range(len(now.neigh)):
            if(now.neigh[i].player==0):
                to_visit.append(now.neigh[i])
            if (not now.neigh[i] in visited or visited[now.neigh[i]]==False) and (now.neigh[i].player==player or now.neigh[i].tileinfo[1]%2==0):
                q.push(now.neigh[i])
                visited[now.neigh[i]]=True
    return to_visit

#vad daca pot sa pun asezare

def check_avail(piece,depth):
    condition=True
    if(depth>0):
        for i in range(piece.neigh):
            if(piece.neigh[i].name=="asezare"):
                condition=False
            condition=condition and check_avail(piece.neigh[i],depth-1)
    return condition

        

        

#ma uit unde pot sa pun oras

def upgradeable(state:gs.game_state,player:int):
    to_upgrade=list()
    visited=dict()
    q=queue.Queue()
    q.put(state.players[player])
    while not q.empty():
        now=q.get()
        if now.name=="asezare":
            upgradeable.append(now)
        else:
            for i in range(len(now.neigh)):
                if (not now.neigh[i] in visited or visited[now.neigh[i]]==False) and (now.neigh[i].player==player or now.neigh[i].tileinfo[1]%2==0):
                    q.push(now.neigh[i])
                    visited[now.neigh[i]]=True
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
    
    #cumpar drum
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
        
def best_move(gamestate):
    starttime=time.time
    mc=MonteCarlo_tree(gamestate)
    leafs=[mc.start]
    while(time.time-starttime<decision):
        now=heapq.heappop(leafs)
        node.make_kids(now)






            


            



    

