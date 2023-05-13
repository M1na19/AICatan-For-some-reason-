import sys
sys.path.append('/home/mihai/Github/AICatan-For-some-reason-')
import simulation as s
import evaluatoare.CardValue as cv
import random
#coeficients
var=10
top=10
varCoefficient=0.3
genLimit=10



prop=open("evaluatoare/test/proportion.txt","r")

topValues=[]
for i in range(top):
    topValues.append([float(x) for x in prop.readline().split()])
prop.close()

def mutate(prop):#mutation function
    Array=[]
    for i in range(len(prop)):
        Array.append(max(prop[i]+random.uniform(-varCoefficient,varCoefficient),0))
    total=1
    for i in range(len(Array)):
        if(total>Array[i]):
            total-=Array[i]
        else:
            Array[i]=random.uniform(0,total)
            total-=Array[i]
    if(total!=0):
        Array[random.randint(0,len(Array)-1)]+=total
    return Array


def fitness(prop):#fitness function
    return s.simulate(prop,simulationTurns)

simulationTurns=20
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
prop=open("evaluatoare/test/proportion.txt","w")
for topValue in topValues:
    for value in topValue:
        prop.write(str(value)+' ')
    prop.write('\n')