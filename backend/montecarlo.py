from copy import deepcopy
import random
import asyncio
from features import cost,check_avail,place_piece,upgradeable
import numpy as np
import backend.game_state as gs
threadNr=1000
discountFactor=0.95

def manageNonAction(name):
    pass

class node:
    def __init__(self,name,state,parent,action:bool):
        self.action=name
        self.value=0
        if(action==True):
            self.depth=parent.depth+1
        else:
            self.depth=parent.depth
        self.state=state
        self.parent=parent
    async def branch(self,AIplayer,threads):
        if(self.state!=None):
            moves=find_moves(self.state,self.state.player_turn,AIplayer)
        tasks=[]
        for i in threads:
            randAction=random.randint(0,moves.count)
            moves[randAction]=node(moves[randAction][0],moves[randAction][0],self,True)
            task=asyncio.create_task(moves[randAction].branch(AIplayer,max(1,threads-moves.count)))
            tasks.append(task)
        results=await asyncio.gather(*tasks)
        self.value=(sum(results)/results.count)*discountFactor
        return self.value                
    
    #aici daca am spre ex oponentul joaca o dezvoltare nu pot sa stiu ce dezvoltare va juca
   
            

class MonteCarlo_tree:
    def __init__(self,startstate,AIplayer):
        self.start=node("start",startstate,None)
        self.nextMoves=find_moves(self.start.state,self.start.state.player_turn,AIplayer)
    async def findBranch(self,threads):
        self.nextMoves=[node(move[0],move[1],self.start,True) for move in self.nextMoves]
        tasks=[]
        for possibility in self.nextMoves:
            task=asyncio.create_task(possibility.branch(self.AIplayer,threads-self.nextMoves.count))
            tasks.append(task)
        results=await asyncio.gather(*tasks)
        maxPoz=0
        for i in range(len(results)):
            if(results[maxPoz]<results[i]):
                maxPoz=i
        return self.nextMoves[maxPoz]

            


        

        


#toate mutarile posibile, btw fuck u mache trb efectiv sa facem sah

def find_moves(state:gs.game_state,AIplayer,player:int)->list(tuple):
    moves=list()
    piece_options=place_piece(state,player)
    #cumpar drum
    if(state.hand[player][0]>0 and state.hand[player][1]>0):
        new_state=state.copy()
        cost(new_state,[1,1,0,0,0],player)
        for i in range(len(piece_options)):
            if piece_options[i].tileinfo[1]%2==0:
                moves.append(new_state.copy().add_piece("drum",player,piece_options[i].tileinfo))
    
    #cumpar asezare
    if(state.hand[player][0]>0 and state.hand[player][1]>0 and state.hand[player][2]>0 and state.hand[player][3]>0):
        new_state=state.copy()
        cost(new_state,[1,1,1,1,0])
        for i in range(len(piece_options)):
            if(piece_options[i].tileinfo[1]%2==1 and check_avail(piece_options[i])):
                moves.append(new_state.copy().add_piece("asezare",player,piece_options[i].tileinfo))
    
    #cumpar oras
    upgrade_options=upgradeable(state,player)
    if state.hand[player][2]>=2 and state.hand[player][4]>=3:
        new_state=state.copy()
        cost(new_state,[0,0,2,0,3])
        for i in range(len(upgrade_options)):
            moves.append(new_state.copy().add_piece("oras",player,piece_options[i].tileinfo))
    
    #cumpar dezvoltare
    if state.hand[player][2]>=1 and state.hand[player][3]>=1 and state.hand[player][4]>=1:
        new_state=state.copy()
        cost(new_state,[0,0,1,1,1],player)
        moves.append("dezvoltare")
    
    #daca sunt eu folosesc hot 
    if(player==AIplayer and state.dezvoltari[1]>0):
        new_state=state.copy()
        new_state.dezvoltari[1]-=1
        moves.append("hot")

    #daca sunt eu folosesc 2 resurse
    if(player==AIplayer and state.dezvoltari[2]>0):
        new_state=state.copy()
        new_state.dezvoltari[2]-=1
        moves.append("2 resurse")
    
    #daca sunt eu folosesc 2 drumuri
    if(player==AIplayer and state.dezvoltari[3]>0):
        new_state=state.copy()
        new_state.dezvoltari[3]-=1
        moves.append("2 drumuri")

    #daca sunt eu folosesc monopol
    if(player==AIplayer and state.dezvoltari[4]>0):
        new_state=state.copy()
        new_state.dezvoltari[4]-=1
        moves.append("monopol")
    
    #ceilalti playeri dezvoltari
    if(player!=AIplayer):
        moves.append("oponent_dezvoltare")

    #go nuts
    moves.append("trading")
    return moves
def best_move(gamestate,AIplayer):
    mc=MonteCarlo_tree(gamestate,AIplayer)
    best=mc.findBranch(threadNr)
    gamestate=best.state
    return best.name

class treeFunctions:
    def default(nod):
        moves=list()
        state=deepcopy(nod.state)
        moves.append(node("Build",state,nod,False))
        moves.append(node("Dezvoltare",state,nod,False))
        moves.append(node("pass",state,nod,True))
        return moves
    

    def zar(nod):
        moves:list[node]=list()
        for i in range(2,13):
            state:gs.game_state=deepcopy(nod.state)
            if i!=7:
                moves.append(node("default",state.zar(i),nod,False))
            else:
                moves.append(node("moveThief",state,nod,False))
        return moves
    
    def pas(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        state.player_turn=(state.player_turn+1)%state.number_of_players
        moves.append(node('zar',state,nod,True))
        return moves
    
    def moveThief(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        for i in range(19):
            if(i!=state.hottile):
                state:gs.game_state=deepcopy(nod.state)
                state.hottile=i
                moves.append(node('steal',state,nod,True))
        return moves
    
    def steal(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        for pieces in state.tiles[state.hottile].pieces:
            if pieces.player==state.player_turn:
                for res in range(5):
                    if(state.hand[pieces.player][res]>0):
                        state:gs.game_state=deepcopy(nod.state)
                        state.hand[pieces.player][res]-=1
                        state.hand[state.player_turn][res]+=1
                        moves.append(node("default",state,nod,True))
        return moves

    def discard(node):
        pass


    def playDezvoltare(nod):
        moves=list()
        state=deepcopy(nod.state)
        moves.append(node("monopol",state,nod,False))
        moves.append(node("2resurse",state,nod,False))
        moves.append(node("2drumuri",state,nod,False))
        moves.append(node("soldat",state,nod,False))
        return moves


    def monopol(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        for i in range(5):
            state:gs.game_state=deepcopy(nod.state)
            for player in range(state.number_of_players):
                if player!=state.player_turn:
                    state.hand[state.player_turn][i]+=state.hand[player][i]
                    state.hand[player][i]=0
            moves.append(node("default",state,nod,True))
        return moves
    
    def drumuri2(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        pieces:list[gs.piece]=place_piece(state,state.player_turn)
        for piece in pieces:
            if(piece.tileinfo[1]%2==1):
                state:gs.game_state=deepcopy(nod.state)
                state.add_piece("drum",state.player_turn,piece.tileinfo)
                pieces2:list[gs.piece]=place_piece(state,state.player_turn)
                for piece2 in pieces2:
                    if(piece2.tileinfo[1]%2==1):
                        state.add_piece("drum",state.player_turn,piece2.tileinfo)
                        moves.append(node("default",state,nod,True))
        return moves
        
    def resurse2(nod):
        moves:list[node]=list()
        for res1 in range(5):
            for res2 in range(5):
                state:gs.game_state=deepcopy(nod.state)
                state.hand[state.player_turn][res1]+=1
                state.hand[state.player_turn][res2]+=1
                moves.append(node("default",state,nod,True))
        return moves
    
    def soldat(nod):
        moves=[node("moveThief",nod.state,nod,False)]
        return moves


    def Build(nod):
        moves=list()
        state=deepcopy(nod.state)
        moves.append(node("drum",state,nod,False))
        moves.append(node("asezare",state,nod,False))
        moves.append(node("oras",state,nod,False))
        moves.append(node("dezvoltare",state,nod,False))
        return moves
    
    def buildAsezare(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        pieces:list[gs.piece]=place_piece(state,state.player_turn)
        for piece in pieces:
            if(piece.tileinfo[1]%2==0):
                state:gs.game_state=deepcopy(nod.state)
                moves.append(node("default",state.add_piece("asezare",state.player_turn,piece.tileinfo),nod,True))
        return moves

    def buildOras(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        upgrades:list[gs.piece]=upgradeable(state,state.player_turn)
        for oras in upgrades:
            state:gs.game_state=deepcopy(nod.state)
            moves.append(node("default",state.add_piece("oras",state.player_turn,oras.tileinfo),nod,True))
        return moves
    
    def buildDrum(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        pieces:list[gs.piece]=place_piece(state,state.player_turn)
        for piece in pieces:
            if(piece.tileinfo[1]%2==1):
                state:gs.game_state=deepcopy(nod.state)
                moves.append(node("default",state.add_piece("drum",state.player_turn,piece.tileinfo),nod,True))
        return moves
    
    def buildDezv(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        for i in range(5):
            state:gs.game_state=deepcopy(nod.state)
            moves.append(node("default",state.add_dezv(i,state.player_turn),nod,True))
        return moves



    def Trade(node):
        pass
    def tradeProposal(node):
        pass






            


            



    

