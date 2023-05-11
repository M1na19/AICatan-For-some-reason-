import pickle

#town city road card
port=2
priority="town"
# 0 1 2 3
Player=0
# lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
CardValue=[1,1,1,1,1]
CardNumber=[0,0,0,0,0]
# tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule
class Myclass:
    def __init__(self,tile,settlement,value,combined):
        self.tile = tile
        self.settlement = settlement
        self.value = value
        self.combined= combined

MapValue= Myclass([0,1,2,3,4,0,1,2,3],[1,1,1,1,1,1,2,2,2],[4,3,12,5,6,8,2,9,10],[0,0,0,0,0])

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
    CardValue[i]*=MapValue.combined[i]
    CardValue[i]*=CardNumber[i]

if priority=="town" :
    CardValue[0]/=1.5
    CardValue[1]/=1.5
    CardValue[2]/=1.5
    CardValue[3]/=1.5
if priority=="city" :
    CardValue[2]/=1.75
    CardValue[4]/=2
if priority=="road" :
    CardValue[0]/=1.5
    CardValue[1]/=1.5
if priority=="card" :
    CardValue[2]/=1.5
    CardValue[3]/=1.5
    CardValue[4]/=1.5

CardValue[port]/=2
for i in range(len(CardNumber)):
    print(CardValue[i])