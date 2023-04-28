import queue
import numpy as np
import game_state as gs
class node:
    def __init__(self):
        self.action="pass"
        self.state=gs.game_state()
        self.parent=node()
        self.kids=np.array()
    def __init__(self,name,state,parent):
        self.action=name
        self.state=state
        self.parent=parent
        self.kids=np.array()

class MonteCarlo_tree:
    def __init__(self):
        self.root=node()


def find_moves(x):
    state=x.state
    moves=np.array()
    if(x.hand[0]>0 and x.hand[1]>0):
        new_state=state.copy()
        new_state.hand[0]-=1
        new_state.hand[1]-=1
        q=queue.Queue()
        q.put(new_state.infrastructure[0].root)
        while not q.empty():
            now=q.get()
            for i in range(len(now.kids)):
                q.push(now.kids[i])



            


            



    

