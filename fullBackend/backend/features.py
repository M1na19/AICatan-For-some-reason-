import random
import queue
import game_state as gs
dezvoltari=[[]]
def random_config():
    tiles=19
    tileprop=[4,3,4,4,3,1]
    diceprop=[0,0,1,2,2,2,2,0,2,2,2,2,1]
    tileconfig=[]
    while tiles>0:
        r=random.randint(-1,4)
        d=random.randint(2,12)
        while(tileprop[r]<=0):
            r=random.randint(-1,4)
        tileprop[r]-=1
        if(r==-1):
            d=0
        else:
            while(diceprop[d]<=0):
                d=random.randint(2,12)
            diceprop[d]-=1
        tileconfig.append((d,r))
        tiles-=1
    return tileconfig
def dice():
    return (random.randint(1,6),random.randint(1,6))

def dezvoltare():
    return random.randint(0,4)

def cost(gamestate,arr,player):
    for i in range(len(arr)):
        gamestate.hand[player][i]-=arr[i]
def can_buy(gamestate,player,arr):
    for i in range(len(arr)):
        if(gamestate.hand[player][i]<arr[i]):
            return False
    return True
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
            if(ngh.player==-1 and (ngh.tileinfo[1]%2==1 or check_avail(ngh,2))):
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
def winned(gamestate:gs.game_state,player):
    LAorLR=0
    if(gamestate.biggestArmy[0]==player):LAorLR+=2
    if(gamestate.biggestRoad[0]==player):LAorLR+=2
    if(gamestate.puncte[player]+dezvoltari[player][0]+LAorLR>=10):
        return True
    else:
        return False
def ceaMaiMareArmata(gamestate:gs.game_state,player):
    if(gamestate.biggestArmy[0]==player):
        return True
    else: return False

def celMaiMareDrum(gamestate:gs.game_state,player):
    roadSize=checkRoadSize(gamestate,player)
    if(roadSize>gamestate.biggestRoad[1]):
        gamestate.biggestRoad=[player,roadSize]
        return True
    if(gamestate.biggestRoad[0]==player):
        return True
    else: 
        return False

def checkRoadSize(gamestate:gs.game_state,player):
    adiacenta=[[]]
    count=0
    frecv=dict()
    q=queue.Queue()

    for road in gamestate.players[player][0].neigh:
        if(road.player==player):
            q.put(road)
    for road in gamestate.players[player][1].neigh:
        if(road.player==player):
            q.put(road)

    while(q.empty()==False):
        now=q.get()
        if(now in frecv):
            continue
        else:
            adiacenta.append([])
            frecv[now]=count
            count+=1
            for neigh in now.neigh:
                for road in neigh.neigh:
                    if road in frecv and road.player==player:
                        adiacenta[frecv[now]].extend([0 for i in range(len(adiacenta[frecv[now]])-1,frecv[road])])
                        adiacenta[frecv[now]][frecv[road]]=1
                        adiacenta[frecv[road]].extend([0 for i in range(len(adiacenta[frecv[road]])-1,frecv[now])])
                        adiacenta[frecv[road]][frecv[now]]=1
                    else:
                        q.put(road)
    maxim=0
    for i in range(count):
        for j in range(count):
            if(i!=j):
                for k in range(count):
                    if(i!=k and j!=k and len(adiacenta[i])>k and len(adiacenta[k])>j):
                        adiacenta[i].extend([0 for i in range(len(adiacenta[i])-1,j)])
                        adiacenta[j].extend([0 for i in range(len(adiacenta[j])-1,i)])
                        if(adiacenta[i][j]<adiacenta[i][k]+adiacenta[k][j]):
                            adiacenta[i][j]=adiacenta[j][i]=adiacenta[i][k]+adiacenta[k][j]

                        if(maxim<adiacenta[i][j]):
                            maxim=adiacenta[i][j]
                    else:
                        adiacenta[i].extend([0 for i in range(len(adiacenta[i])-1,k)])
                        adiacenta[j].extend([0 for i in range(len(adiacenta[j])-1,k)])
                    
    return maxim


