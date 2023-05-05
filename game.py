import montecarlo as mc
import game_state as gs
import random
first_player=0
tileconfig=[(10,4),(2,3),(9,0),(12,2),(6,1),(4,3),(10,1),(9,2),(11,0),(0,0),(3,0),(8,4),(8,0),(3,4),(4,2),(5,3),(5,1),(6,2),(11,3)]
sg=gs.game_state(tileconfig,first_player)
for i in range(2)
  for j in range(4)
    tile=random.randint(0,18)
    poz=random.randint(0,11)
    while not mc.check_avail(sg.tiles[tile].pieces[poz],2)
      tile=random.randint(0,18)
      poz=random.randint(0,11)
    sg.add_piece("asezare",i,tile,poz)
    sg.add_piece("oras",i,sg.tiles[tile].pieces[poz].neigh[random.randint(0,len(sg.tiles[tile].pieces[poz].neigh))].tileinfo[0],sg.tiles[tile].pieces[poz].neigh[random.randint(0,len(sg.tiles[tile].pieces[poz].neigh))].tileinfo[1
