import sys,os

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import evaluatoare.CardValue as cv
from copy import deepcopy
import random
import asyncio
from backend.features import cost,check_avail,place_piece,upgradeable,winned,random_config
import backend.game_state as gs
import evaluatoare.TradeValue as tv
import evaluatoare.PositionValue as pv
import time
import backend.features as features

threadNr=1000
discountFactor=0.8



class node:
    def __init__(self,name,state,parent):
        self.name=name
        self.value=0
        if(parent!=None):
            self.depth=parent.depth+1
        else:self.depth=0
        self.state=state
        self.parent=parent
        self.children:list[node]=[]
        if(parent!=None):
            self.usedDezv=parent.usedDezv
            parent.children.append(self)
        else:
            self.usedDezv=False
    
    async def branch(self,AIplayer,threads:int,deadline):
        print(self.state.player_turn,self.name,self.depth)
        if(winned(self.state,self.state.player_turn)==True ):
            self.value=10
        elif(time.time()>deadline):
            self.value=pv.Calculate_PositionValue(self.state,AIplayer,features.dezvoltari)
        else:
            moves=treeFunctions.zar(self,AIplayer)
            tasks=[]
            for i in range(min(round(threads),len(moves))):
                randAction=random.randint(0,len(moves)-1)
                task=asyncio.create_task(moves[randAction].branch(AIplayer,max(1,threads-len(moves)),deadline))
                moves.remove(moves[randAction])
                tasks.append(task)
            results=await asyncio.gather(*tasks)
            self.value=(sum(results)/len(results))*discountFactor
        return self.value                
    
    #aici daca am spre ex oponentul joaca o dezvoltare nu pot sa stiu ce dezvoltare va juca
   
            

class MonteCarlo_tree:
    def __init__(self,startstate,AIplayer):
        self.start=node("default",startstate,None)
        self.AIplayer=AIplayer
        self.nextMoves:list[node]=treeFunctions.default(self.start,self.AIplayer)
    async def makeBranch(self):
        tasks=[]
        for possibility in self.nextMoves:
            task=asyncio.create_task(possibility.branch(self.AIplayer,threadNr/len(self.nextMoves),time.time()+10))
            tasks.append(task)
        await asyncio.gather(*tasks)

            


        

        


#toate mutarile posibile, btw fuck u mache trb efectiv sa facem sah

async def best_move(gamestate,AIplayer):
    mc=MonteCarlo_tree(gamestate,AIplayer)
    await mc.makeBranch()
    k=mc.start
    bestAction=k.children[0]
    for action in k.children:
        if(bestAction.value<action.value):
            bestAction=action
    print(bestAction.name)
    return bestAction

class treeFunctions:
    def default(nod:node,AIplayer):
        moves=list()
        if(features.can_buy(nod.state,nod.state.player_turn,[1,1,0,0,0]) or features.can_buy(nod.state,nod.state.player_turn,[0,0,1,1,1]) or features.can_buy(nod.state,nod.state.player_turn,[0,0,2,0,3])):
            moves+=treeFunctions.Build(nod)
        if(((AIplayer==nod.state.player_turn and sum(nod.state.dezvoltari)>0) or AIplayer!=nod.state.player_turn) and nod.usedDezv==False):
            moves+=treeFunctions.playDezvoltare(nod)
        if(sum(nod.state.hand[nod.state.player_turn])>0):
            moves+=treeFunctions.Trade(nod)
        moves+=treeFunctions.pas(nod)
        return moves
    

    def zar(nod,AIplayer):
        moves:list[node]=list()
        nod.state.player_turn=(nod.state.player_turn+1)%nod.state.number_of_players
        for i in range(2,13):
            state:gs.game_state=deepcopy(nod.state)
            if i!=7:
                state.zar(i)
                sendNode=deepcopy(nod)
                sendNode.state=state
                moves+=treeFunctions.default(sendNode,AIplayer)
            else:
                moves+=treeFunctions.discard(nod)
        return moves
    
    def pas(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        moves.append(node('pass',state,nod))
        return moves
    
    def moveThief(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        originalTile=state.hottile
        for i in range(19):
            if(i!=state.hottile):
                nod.state.hottile=i
                moves+=treeFunctions.steal(nod)
        nod.state.hottile=originalTile
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
                        newNode=node("steal",state,nod)
                        newNode.usedDezv=True
                        moves.append(newNode)
        return moves

    def discard(nod):
        valueofCards:list[int]=[0,0,0,0,0]
        worstCard=0
        state:gs.game_state=deepcopy(nod.state)
        for player in range(state.number_of_players):
            if sum(state.hand[player])>7:
                for _ in range(round(sum(state.hand[player])/2)):
                    for i in range(5):
                        tryState:gs.game_state=deepcopy(state)
                        tryState.hand[player][i]-=1
                        valueofCards[i]=cv.cardEvaluator(tryState,player)[i]
                        if(valueofCards[i]<valueofCards[worstCard]):
                            worstCard=i
                    state.hand[player][worstCard]-=1
        sendNode=deepcopy(nod)
        sendNode.state=state
        return treeFunctions.moveThief(sendNode)
                
                



    def playDezvoltare(nod):
        moves=list()
        state:gs.game_state=deepcopy(nod.state)
        if(state.dezvoltari[4]>0):
            moves+=treeFunctions.monopol(nod)
        if(state.dezvoltari[2]>0):
            moves+=treeFunctions.resurse2(nod)
        if(state.dezvoltari[3]>0):
            moves+=treeFunctions.drumuri2(nod)
        if(state.dezvoltari[1]>0):
            moves+=treeFunctions.soldat(nod)
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
            newNode=node("monopol",state,nod)
            newNode.usedDezv=True
            moves.append(newNode)
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
                        newNode=node("2drum",state,nod)
                        newNode.usedDezv=True
                        moves.append(newNode)
        return moves
        
    def resurse2(nod):
        moves:list[node]=list()
        for res1 in range(5):
            for res2 in range(5):
                state:gs.game_state=deepcopy(nod.state)
                state.hand[state.player_turn][res1]+=1
                state.hand[state.player_turn][res2]+=1
                newNode=node("2resurse",state,nod)
                newNode.usedDezv=True
                moves.append(newNode)
        return moves
    
    def soldat(nod):
        moves=treeFunctions.moveThief(nod)
        return moves


    def Build(nod):
        moves=list()
        state:gs.game_state=deepcopy(nod.state)
        if(features.can_buy(state,state.player_turn,[1,1,1,1,0])):
            moves+=treeFunctions.buildAsezare(nod)
        if(features.can_buy(state,state.player_turn,[1,1,0,0,0])):
            moves+=treeFunctions.buildDrum(nod)
            pass
        if(features.can_buy(state,state.player_turn,[0,0,2,0,3])):
            moves+=treeFunctions.buildOras(nod)
        if(features.can_buy(state,state.player_turn,[0,0,1,1,1])):
            moves+=treeFunctions.buildDezv(nod)
        return moves
    
    def buildAsezare(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        pieces:list[gs.piece]=place_piece(state,state.player_turn)
        for piece in pieces:
            if(piece.tileinfo[1]%2==0 and check_avail(piece,2)):
                state:gs.game_state=deepcopy(nod.state)
                state.add_piece("asezare",state.player_turn,piece.tileinfo)
                moves.append(node("asezare",state,nod))
        return moves

    def buildOras(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        upgrades:list[gs.piece]=upgradeable(state,state.player_turn)
        for oras in upgrades:
            state:gs.game_state=deepcopy(nod.state)
            state.add_piece("oras",state.player_turn,oras.tileinfo)
            moves.append(node("oras",state,nod))
        return moves
    
    def buildDrum(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        pieces:list[gs.piece]=place_piece(state,state.player_turn)
        for piece in pieces:
            if(piece.tileinfo[1]%2==1):
                state:gs.game_state=deepcopy(nod.state)
                state.add_piece("drum",state.player_turn,piece.tileinfo)
                moves.append(node("drum",state,nod))
        return moves
    
    def buildDezv(nod):
        moves:list[node]=list()
        state:gs.game_state=deepcopy(nod.state)
        for i in range(5):
            state:gs.game_state=deepcopy(nod.state)
            state.add_dezv(i,state.player_turn)
            moves.append(node("dezvoltare",state,nod))
        return moves



    def Trade(nod):#for this version trade 1 for 1
        moves:list[int]=list()
        state:gs.game_state=deepcopy(nod.state)
        cardsValue:list[int]=cv.cardEvaluator(state,state.player_turn)
        bestCard=0
        for i in range(len(cardsValue)):
            if(cardsValue[i]>cardsValue[bestCard]):
                bestCard=i
        for i in range(5):
            if(state.hand[state.player_turn][i]>0):
                for player in range(state.number_of_players):
                    if(player!=state.player_turn and state.hand[player][bestCard]>0):
                        if(tv.checkTradeProposal(state,[i],[bestCard],state.player_turn,player)==True):
                            state:gs.game_state=deepcopy(nod.state)
                            state.hand[player][bestCard]-=1
                            state.hand[state.player_turn][i]-=1
                            state.hand[player][i]+=1
                            state.hand[state.player_turn][bestCard]+=1
                            moves.append(node("Trade",state,nod))
        return moves
        


# features.dezvoltari=[[0 for j in range(5)] for i in range(4)]
# gamestate=gs.game_state(random_config(),1,4)
# gamestate.add_piece("asezare",0,[0,6])
# gamestate.add_piece("asezare",1,[1,6])
# gamestate.add_piece("asezare",2,[2,6])
# gamestate.add_piece("asezare",3,[3,6])
# gamestate.add_piece("asezare",0,[4,6])
# gamestate.add_piece("asezare",1,[5,6])
# gamestate.add_piece("asezare",2,[6,6])
# gamestate.add_piece("asezare",3,[7,6])
# gamestate.hand[1]=[0,0,1,1,0]
# gamestate.dezvoltari=[1,1,0,0,0]
# asyncio.run(best_move(gamestate,1))



            


            



    

