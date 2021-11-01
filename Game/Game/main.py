# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:14:44 2021

@author: eugen
"""

import Game

g = Game.Game("","")

#g.makeMoveByNotation("E2E4")
#g.makeMoveByNotation("E7E5")
#g.makeMoveByNotation("F1B5")
#g.makeMoveByNotation("C7C6")
#g.makeMoveByNotation("B5C4")
#g.makeMoveByNotation("D7D6")
#g.makeMoveByNotation("D1F3")
#g.makeMoveByNotation("A7A5")
#g.makeMoveByNotation("F3F7")


#PASTOR
"""
g.makeMoveByNotation("E2E4")
g.makeMoveByNotation("E7E5")
g.makeMoveByNotation("F1C4")
g.makeMoveByNotation("B8C6")
g.makeMoveByNotation("D1H5")
g.makeMoveByNotation("F8C5")
g.makeMoveByNotation("H5F7")
"""

#CAPTURA AL PASO


import time
start_time = time.time()


g.makeMoveByNotation("E2E4")
g.makeMoveByNotation("D7D6")
g.makeMoveByNotation("E4E5")
g.makeMoveByNotation("F7F5")
g.makeMoveByNotation("E5D6")
g.makeMoveByNotation("E7D6")
g.makeMoveByNotation("A2A4")
g.makeMoveByNotation("D6D5")
g.makeMoveByNotation("A4A5")
g.makeMoveByNotation("D5D4")
g.makeMoveByNotation("C2C4")
g.makeMoveByNotation("D4C3")
g.makeMoveByNotation("D1A4")

print("--- %s seconds ---" % (time.time() - start_time))


#print(g.board.isOnPassant([3,4,2,5]))

#print(g.board.getMovesByPos([7,3]))
#print(g.board.getPossibleMoves(1))
