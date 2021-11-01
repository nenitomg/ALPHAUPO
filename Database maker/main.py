# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:52:34 2021

@author: eugen
"""

import database_loader as dbl




#MAIN


files = dbl.getFiles('pgn_games')
dbl.deleteTables()

for file in files:
    print("Executing for: " + file)
    games = dbl.getGames(file)
    dbl.createTableGames(games)

print("Eliminando filas innecesarias")
dbl.eliminaFilas()