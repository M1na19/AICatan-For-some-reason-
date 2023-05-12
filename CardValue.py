#import game_state
class Myclass:
        def __init__(self,tile,settlement,value):
            self.tile = tile
            self.settlement = settlement
            self.value = value
            self.combined=[0,0,0,0,0]


def getTileArray(gameState):
    Array=[]
    for tile in gameState.tiles:
        Array.append(tile.resource)
    return Array


def getPiecesArray(gameState):
    Array=[]
    for i in range(len(gameState.tiles)):
        tilevalue=0
        for piece in gameState.tiles[i].pieces:
            if piece.name=="asezare":
                tilevalue+=1
            elif piece.name=="oras":
                tilevalue+=2
        Array.append(tilevalue)
    return Array


def getPorts(gameState,p):
    Array=[]
    for i in range(len(gameState.ports[p])-1):
        if(gameState.ports[p][i]==1):
            Array.append(i)
    return Array
        
        

def getValueArray(gameState):
    Array=[]
    for tile in gameState.tiles:
        Array.append(tile.values)
    return Array


def cardEvaluator(gameState,Player):
    #town city road card
    Port=getPorts(gameState,Player)
    # 0 1 2 3
    # lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
    CardValue=[1,1,1,1,1]
    CardNumber=[0,0,0,0,0]
    # tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule

    MapValue= Myclass(getTileArray(gameState),getPiecesArray(gameState),getValueArray(gameState))

    Cards =[[1, 1, 2, 3, 4], 
            [ 0, 1, 2, 3, 4],
            [ 0, 1, 2, 3, 4],
            [ 0, 1, 2, 3, 4]]

    # CU CAT VALOREA E MAI MICA CU ATAT ESTE MAI PRETIOASA

    for i in range(len(Cards)):
        for j in range(len(Cards[i])):
            if i!=Player :
                CardNumber[Cards[i][j]]+=1
            else:
                CardValue[Cards[i][j]]+=1
            
    for i in range(len(MapValue.tile)):
        MapValue.combined[MapValue.tile[i]]+=MapValue.settlement[i]*((MapValue.value[i]%7)*2.77777777778/100)

    for i in range(len(CardValue)):
        CardValue[i]+=MapValue.combined[i]
        CardValue[i]+=CardNumber[i]

    for i in range(len(Port)):
        CardValue[Port[i]]/=2
    for i in range(len(CardNumber)):
        print(CardValue[i])
    return CardValue