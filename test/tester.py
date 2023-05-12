import simulation as s
import CardValue as cv
import random
#coeficients
range=10
top=10
varCoefficient=20
genLimit=10



prop=open("proportion.txt","r")

topValues=[]
for i in range(top):
    topValues.append([int(x) for x in prop.readline().split()])


def mutate(prop):#mutation function
    Array=[]
    for i in range(len(prop)):
        Array.append(prop[i]+random.uniform(-varCoefficient,varCoefficient))
    total=1
    for i in range(len(Array)):
        if(total>Array[i]):
            total-=Array[i]
        else:
            Array-=random.uniform(0,total)
            prop[i]=total
    if(total!=0):
        Array[random.uniform(0,len(Array))]+=total


def fitness(prop,gamestate):#fitness function
    return s.simulate(prop,gamestate)


def geneticAlgorithm(generation):
    if(generation<=genLimit):
        proportions=[]
        for topValue in topValues:
            for i in range(range):
                proportions.append(mutate(topValue))
        proportions=sorted(proportions,fitness())
        topValues.clear()
        for proportion in proportions[:10]:
            topValues.append(proportion)
        geneticAlgorithm(generation+1)
geneticAlgorithm(1)