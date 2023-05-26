#import game_state
valueCity=1
valueTown=0.8
valueDezv=0.6
valueRoad=0.4
townResources=[1,1,1,1,0]
roadResources=[1,1,0,0,0]
cityResources=[0,0,2,0,3]
dezvResources=[0,0,1,1,1]
def getPorts(gameState,p):
    Array=[]
    for i in range(len(gameState.ports[p])-1):
        if(gameState.ports[p][i]==1):
            Array.append(i)
    return Array
def closenessToConstruction(myCards):
    closeToCity=0
    closeToRoad=0
    closeToDezv=0
    closeToTown=0
    for i in range(len(townResources)):
        closeToTown+=min(townResources[i],myCards[i])
    for i in range(len(cityResources)):
        closeToCity+=min(cityResources[i],myCards[i])
    for i in range(len(dezvResources)):
        closeToDezv+=min(dezvResources[i],myCards[i])
    for i in range(len(roadResources)):
        closeToRoad+=min(roadResources[i],myCards[i])
    closeToRoad/=sum(roadResources)
    closeToCity/=sum(cityResources)
    closeToTown/=sum(townResources)
    closeToDezv/=sum(dezvResources)
    return (closeToTown+closeToDezv+closeToRoad+closeToCity)/(valueCity+valueDezv+valueRoad+valueTown)

weightPort=-0.1
weightRareness=0.3
weightUsefull=0.8
def cardEvaluator(gameState,Player):
    portValue=[0,0,0,0,0]
    rarenessValue=[0,0,0,0,0]
    usefullValue=[0,0,0,0,0]
    #town city road card
    Port=getPorts(gameState,Player)
    Port3_1=gameState.ports[Player][5]
    # 0 1 2 3
    # lemn=0 argila=1 fan=2 oaie=3 piatra=4 index
    CardValue=[0,0,0,0,0]
    CardNumber=[0,0,0,0,0]
    # tileurile cu ce fel sunt, cate orase sunt si case adunate casa=1 oras=2, ce valoare are tileul, combinare pt calcule


    Cards=gameState.hand
    playerHand=Cards[0]
    #pt a vedea cat de rar este o carte intre  celelalte vedem ce proportie din cartile totale este
    for i in range(len(Cards)):
        for j in range(len(Cards[i])):
            CardNumber[j]+=1
            
    for i in range(len(CardNumber)):
        rarenessValue[i]=1-CardNumber[i]/sum(CardNumber) #daca nu fac 1-cu cat e mai mica valaorea cu ata e mai worth
    #pana aici
    #si mai bine as putea sa calculez cat de apropea de a construi cv sunt curent si dupa ce extrag cartea
    current=closenessToConstruction(playerHand)
    for i in range(len(playerHand)):
        playerHand[i]+=1
        usefullValue[i]=closenessToConstruction(playerHand)-current
        playerHand[i]-=1
    #pt un port de 2:1 resursa valoarea este 1 pt un port 3:1 valoarea este 0.5
    for i in range(len(Port)):
        if(Port[i]==1):
            portValue[i]=1
        elif(Port3_1==1):
            portValue[i]=0.5
    for i in range(len(CardValue)):
        CardValue[i]=portValue[i]*weightPort+rarenessValue[i]*weightRareness+usefullValue[i]*weightUsefull
    return CardValue