
import evaluatoare.CardValue as cval
from queue import Queue
import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.game_state import game_state as gs,piece
##############Things from the game code######################################################################################################################################################


##############Things from the game code######################################################################################################################################################

def Calculate_PositionValue(gamestate:gs,player,dezvoltari):
    ############### The variables
    resourceProduction=0
    developmentvalue=0
    LRaLA=0
    VP=0
    #1 Resource Production
    for tile in gamestate.tiles:
        if(tile.index!=gamestate.hottile):
            for piece in tile.pieces:
                if(piece.name=="asezare" and piece.player==player):
                    resourceProduction+=(7-abs(tile.value-7))/7*0.5
                if(piece.name=="oras" and piece.player==player):
                    resourceProduction+=(7-abs(tile.value-7))/7
                if(piece.name=="drum" and piece.player==player):
                    resourceProduction+=(7-abs(tile.value-7))/7*0.1

        
    #2 Expansion
    expansion=gamestate.constructi[player][0]*2+gamestate.constructi[player][1]+gamestate.constructi[player][0]/2
    #3 Development Cards
    developmentvalue=dezvoltari[player][1]*0.5+dezvoltari[player][2]*0.6+dezvoltari[player][3]*0.8+dezvoltari[player][4]
    #4. Longest Road and Largest Army
    if(gamestate.biggestArmy[0]==player):LRaLA+=2
    if(gamestate.biggestRoad[0]==player):LRaLA+=2
    #5. Victory Points
    VP=dezvoltari[player][0]
    #6. COMBINAREA VARIABILELOR
    rez=0
    rez=resourceProduction+expansion+developmentvalue+LRaLA+VP
    return rez

