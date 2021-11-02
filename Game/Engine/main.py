# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:55:27 2021
@author: eugen
"""

import sys
sys.path.insert(1, 'MiniMax')
import MiniMax as mm
import chess
import time
import chess.pgn





#Hace que el motor de ajedrez juege contra si mismo y guarda los resultados en la carpeta
#engines/games/ con el nombre de nombre_archivo se le pasa la profundidad a la que se quiere
#jugar si quiere usar minimax(engine = False), para minimax con alpha y beta(engine = True)
#Se le pasa tambien el evento, el sitio, la fecha, quien va con blancas, quien va con negras
#y el nombre del archivo

def playAgainstItself(depth, engine_name, evento, sitio, fecha, con_blancas, con_negras, nombre_archivo):
    game = chess.pgn.Game()
    game.headers["Event"] = evento
    game.headers["Site"] = sitio
    game.headers["Date"] = fecha
    game.headers["White"] = con_blancas
    game.headers["Black"] = con_negras
    
    
    print(game)
    board = game.board()
    node = game.game()
    
    engine = mm.MiniMax()
    
    
    #alphabeta
    if (engine_name):
        alpha = -float("inf")
        beta = float("inf")
        iteration = 0
        
        while (board.is_checkmate() != True) and (board.is_stalemate() != True) and (board.is_insufficient_material() != True) and (board.can_claim_draw() != True):
            start_time = time.time()
            move = engine.alphaBeta(board, depth, alpha, beta)[1]
            board.push(move)
            node = node.add_variation(move)
            print("\nTiempo Alpha-beta iteracion( ", iteration," ) / ", move,": ", (time.time() - start_time))
            print(board)
            iteration = iteration + 1
        
    
    #minimax
    else:
        while (board.is_checkmate() != True) and (board.is_stalemate() != True) and (board.is_insufficient_material() != True) and (board.can_claim_draw() != True):
            start_time = time.time()
            move = engine.miniMax(board, depth)[1]
            board.push(move)
            node = node.add_variation(move)
            print("\nTiempo Alpha-beta iteracion( ", iteration," ) / ", move,": ", (time.time() - start_time))
            print(board)
            iteration = iteration + 1
    
    print(game, file=open("games/" + nombre_archivo, "w"), end="\n\n")


#Main

depth = 5
engine = True

evento = "Quinta partida de minMax alpha-beta profundidad 5"
sitio = "Local"
fecha = "2021/11/1"
con_blancas = "Alphaupo MiniMax alpha-beta depth 5"
con_negras = "Alphaupo MiniMax alpha-beta depth 5"
nombre_archivo = "miniMaxAlphaBetaGame6-depth5.pgn"


playAgainstItself(depth, engine, evento, sitio, fecha, con_blancas, con_negras, nombre_archivo)



#problemas
"""
engine = mm.MiniMax()
board = chess.Board("8/8/8/4p3/6P1/P7/1P1k1KP1/8 b - - 0 51")


move = engine.alphaBeta(board, 7, -float("inf"), float("inf"))
print("Movimiento alphabeta: ", str(move[1]))
"""









