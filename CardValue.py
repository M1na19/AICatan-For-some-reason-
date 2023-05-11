import pickle

Player=0
# lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
CardValue=[1,1,1,1,1]
CardNumber=[0,0,0,0,0]

class Myclass:
    tile=[0]
    settlement=[0]
    value=[0]

MapValue= Myclass()


Cards =[[1, 1, 2, 3, 4], 
        [ 0, 1, 2, 3, 4],
        [ 0, 1, 2, 3, 4],
        [ 0, 1, 2, 3, 4]]

for i in range(len(Cards)):
    for j in range(len(Cards[i])):
        if i!=Player :
            CardNumber[Cards[i][j]]+=1
        else:
            CardValue[Cards[i][j]]+=1
        
for i in range(len(CardNumber)):
    print(CardNumber[i])