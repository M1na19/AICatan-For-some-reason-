import montecarlo as mc
import game_state as gs
import random
first_player=0
tileconfig=[(10,4),(2,3),(9,0),(12,2),(6,1),(4,3),(10,1),(9,2),(11,0),(0,0),(3,0),(8,4),(8,0),(3,4),(4,2),(5,3),(5,1),(6,2),(11,3)]
sg=gs.game_state(tileconfig,first_player)
for i in range(2):
  for j in range(4):
    tile=random.randint(0,18)
    poz=random.randint(0,5)*2
    while not mc.check_avail(sg.tiles[tile].pieces[poz],2):
      tile=random.randint(0,18)
      poz=random.randint(0,5)*2
    
    sg.add_piece("asezare",j,(tile,poz))
    dir=random.randint(0,len(sg.tiles[tile].pieces[poz].neigh)-1)
    sg.add_piece("drum",j,sg.tiles[tile].pieces[poz].neigh[dir].tileinfo)

print(sg.players[0][0].tileinfo)
print(sg.players[0][1].tileinfo)
print()
for i in mc.place_piece(sg,0):
  print(i.tileinfo)
