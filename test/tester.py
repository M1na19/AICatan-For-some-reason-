import sys
sys.path.append('/home/mihai/Github/AICatan-For-some-reason-')
import simulation as s
import CardValue as cv
import random
#coeficients
var=10
top=10
varCoefficient=0.1
genLimit=100



prop=open("test/proportion.txt","r")

topValues=[]
for i in range(top):
    topValues.append([float(x) for x in prop.readline().split()])


def mutate(prop):#mutation function
    Array=[]
    for i in range(len(prop)):
        Array.append(prop[i]+random.uniform(-varCoefficient,varCoefficient))
    total=1
    for i in range(len(Array)):
        if(total>Array[i]):
            total-=Array[i]
        else:
            Array[i]-=random.uniform(0,total)
            prop[i]=total
    if(total!=0):
        Array[random.randint(0,len(Array)-1)]+=total
    return Array


def fitness(prop):#fitness function
    return s.simulate(prop)


def geneticAlgorithm(generation):
    if(generation<=genLimit):
        proportions=[]
        for topValue in topValues:
            for i in range(var):
                proportions.append(mutate(topValue))
        proportions=sorted(proportions,key=lambda x: fitness(x))
        topValues.clear()
        for proportion in proportions[:10]:
            topValues.append(proportion)
        geneticAlgorithm(generation+1)
geneticAlgorithm(1)