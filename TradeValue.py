import pickle
import CardValue as cval

#town city road card
Port0=[2,1]
Port1=[3,4]
Priority0="town"
Priority1="city"
# 0 1 2 3
Player0=0
Player1=1
# lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
CardValue0=[1,1,1,1,1]
CardValue1=[1,1,1,1,1]

# tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule
class Myclass:
    def __init__(self,tile,settlement,value,combined):
        self.tile = tile
        self.settlement = settlement
        self.value = value
        self.combined= combined

MapValue0= Myclass([0,1,2,3,4,0,1,2,3],[1,1,1,1,1,1,2,2,2],[4,3,12,5,6,8,2,9,10],[0,0,0,0,0])
MapValue1= Myclass([0,1,2,3,4,0,1,2,3],[1,1,1,1,1,1,2,2,2],[4,3,12,5,6,8,2,9,10],[0,0,0,0,0])

Cards =[[1, 1, 2, 3, 4], 
        [ 0, 1, 2, 3, 4],
        [ 0, 1, 2, 3, 4],
        [ 0, 1, 2, 3, 4]]

Player0Cards=[0,1,2,3,4,0,1,2]
Player1Cards=[0,0,2,3,0,0,1,2]

# FUNCTIE DE SUMA LOL
def _sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return(sum)

# This is where the code begins

Player0CardsValue=cval.Calculate_CardValue(Port0,Priority0,Player0,CardValue0,MapValue0)
Player1CardsValue=cval.Calculate_CardValue(Port1,Priority1,Player1,CardValue1,MapValue1)

Trade0=[0,0,0,0,0]
Trade1=[0,0,0,0,0]

for i in range(len(Player0Cards)):
    Trade0[Player0Cards[i]]+=1
for i in range(len(Player1Cards)):
    Trade1[Player1Cards[i]]+=1

for i in range(len(Player0CardsValue)):
    Trade0[i]*=Player0CardsValue[i]
    Trade1[i]*=Player1CardsValue[i]

totalvalue0=_sum(Trade0)
totalvalue1=_sum(Trade1)

if totalvalue0>totalvalue1:
    print("GOOD TRADE FOR NO 0")
else:
    print("GOOD TRADE FOR NO 1")
