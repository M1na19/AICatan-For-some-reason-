import montecarlo as mc
import game_state as gs
first_player=0
tileconfig=[(10,4),(2,3),(9,0),(12,2),(6,1),(4,3),(10,1),(9,2),(11,0),(0,0),(3,0),(8,4),(8,0),(3,4),(4,2),(5,3),(5,1),(6,2),(11,3)]
sg=gs.game_state(tileconfig,first_player)
sg.add_piece("asezare")
