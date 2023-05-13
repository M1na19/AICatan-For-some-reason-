import pickle
import evaluatoare.CardValue as cval

##############Things from the game code######################################################################################################################################################

Port=[2,1]
# 0 1 2 3
Player=0
#dezvoltari:@0 victory pct,@1 hot,@2 2resurse,@3 2 drumuri,@4 monopol

DevelopmentCards=[2,1,1,2,3]

# lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
CardValue=[1,1,1,1,1]

# tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule
class Myclass:
    def __init__(self,tile,settlement,value,combined):
        self.tile = tile
        self.settlement = settlement
        self.value = value
        self.combined= combined

MapValue= Myclass([0,1,2,3,4,0,1,2,3],[1,1,1,1,1,1,2,2,2],[4,3,12,5,6,8,2,9,10],[0,0,0,0,0])

city=2
town=3
roads=4

BiggestArmy=[3,4,2,1]
BiggestRoad=[5,6,7,8]

##############Things from the game code######################################################################################################################################################

def Calculate_PositionValue(Port,Player,MapValue,DevelopmentCards,city,town,roads,BiggestArmy,BiggestRoad):
    ############### The variables
    resourceProduction=0
    expansion=0
    developmentvalue=0
    LRaLA=0
    VP=0
    #1 Resource Production
    for i in range(len(MapValue.tile)):
        MapValue.combined[MapValue.tile[i]]+=MapValue.settlement[i]*(MapValue.value[i]%7)
        resourceProduction+=MapValue.combined[MapValue.tile[i]]
    #2 Expansion
    expansion+=city*3+town*2+roads+len(Port)
    #3 Development Cards
    for i in range(len(DevelopmentCards)):
        if i==0:
            developmentvalue+=1.5*DevelopmentCards[i]
        if i==1:
            developmentvalue+=1.75*DevelopmentCards[i]
        if i==2:
            developmentvalue+=1*DevelopmentCards[i]
        if i==3:
            developmentvalue+=2*DevelopmentCards[i]
        if i==4:
            developmentvalue+=3*DevelopmentCards[i]
    #4. Longest Road and Largest Army
    soldati=0
    mare=0
    mare2=0
    for i in range(len(BiggestArmy)):
        if BiggestArmy[i]>mare2:
            mare2=BiggestArmy[i]
    if BiggestArmy[Player]==mare2:
        LRaLA+=2
    else:
        LRaLA+=2-(mare2-(mare2-BiggestArmy[Player]))/BiggestArmy[Player]
    for i in range(len(BiggestRoad)):
        if BiggestRoad[i]>mare:
            mare=BiggestRoad[i]

    if BiggestRoad[Player]==mare:
        LRaLA+=2
    else:
        LRaLA+=2-(mare-(mare-BiggestRoad[Player]))/BiggestRoad[Player]
    #5. Victory Points
    rezvp=0
    if BiggestArmy[Player]==mare2:
        rezvp+=2
    if BiggestRoad[Player]==mare:
        rezvp+=2
    rezvp=rezvp+town+city*2+DevelopmentCards[0]
    #6. COMBINAREA VARIABILELOR
    rez=0
    rez=resourceProduction+expansion+developmentvalue+LRaLA+VP
    return rez

Calculate_PositionValue(Port,Player,MapValue,DevelopmentCards,city,town,roads,BiggestArmy,BiggestRoad)