# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:23:43 2021

@author: eugen
"""

import numpy as np

#Rota un array 180 gradoss
def rotateArray(array):
        res = array.copy()
        tam = len(array)
        for i in range(tam):
            for j in range(tam):
                res[i, tam-1-j] = array[tam-1-i, j]
        return res
    
class MiniMax:

    #Constructor, se declaran las matrices para ponderar la posicion de las piezas
    def __init__(self):
        self.wp = np.array([[ 0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ],
       [ 5. ,  5. ,  5. ,  5. ,  5. ,  5. ,  5. ,  5. ],
       [ 1. ,  1. ,  2. ,  3. ,  3. ,  2. ,  1. ,  1. ],
       [ 0.5,  0.5,  1. ,  2.5,  2.5,  1. ,  0.5,  0.5],
       [ 0. ,  0. ,  0. ,  2. ,  2. ,  0. ,  0. ,  0. ],
       [ 0.5, -0.5, -1. ,  0. ,  0. , -1. , -0.5,  0.5],
       [ 0.5,  1. ,  1. , -2. , -2. ,  1. ,  1. ,  0.5],
       [ 0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ]])
        self.bp = -rotateArray(self.wp)
        self.wn = np.array([[-5. , -4. , -3. , -3. , -3. , -3. , -4. , -5. ],
       [-4. , -2. ,  0. ,  0. ,  0. ,  0. , -2. , -4. ],
       [-3. ,  0. ,  1. ,  1.5,  1.5,  1. ,  0. , -3. ],
       [-3. ,  0.5,  1.5,  2. ,  2. ,  1.5,  0.5, -3. ],
       [-3. ,  0. ,  1.5,  2. ,  2. ,  1.5,  0. , -3. ],
       [-3. ,  0.5,  1. ,  1.5,  1.5,  1. ,  0.5, -3. ],
       [-4. , -2. ,  0. ,  0.5,  0.5,  0. , -2. , -4. ],
       [-5. , -4. , -3. , -3. , -3. , -3. , -4. , -5. ]])
        self.bn = -rotateArray(self.wn)
            
        self.wb = np.array([[-2. , -1. , -1. , -1. , -1. , -1. , -1. , -2. ],
       [-1. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. , -1. ],
       [-1. ,  0. ,  0.5,  1. ,  1. ,  0.5,  0. , -1. ],
       [-1. ,  0.5,  0.5,  1. ,  1. ,  0.5,  0.5, -1. ],
       [-1. ,  0. ,  1. ,  1. ,  1. ,  1. ,  0. , -1. ],
       [-1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. , -1. ],
       [-1. ,  0.5,  0. ,  0. ,  0. ,  0. ,  0.5, -1. ],
       [-2. , -1. , -1. , -1. , -1. , -1. , -1. , -2. ]])
        self.bb = -rotateArray(self.wb)
            
            
        self.wr = np.array([[ 0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0. ],
       [ 0.5,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  0.5],
       [-1. ,  0. ,  0.5,  1. ,  1. ,  0.5,  0. , -0.5],
       [-1. ,  0.5,  0.5,  1. ,  1. ,  0.5,  0.5, -0.5],
       [-1. ,  0. ,  1. ,  1. ,  1. ,  1. ,  0. , -0.5],
       [-1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. , -0.5],
       [-1. ,  0.5,  0. ,  0. ,  0. ,  0. ,  0.5, -0.5],
       [ 0. ,  0. ,  0. ,  0.5,  0.5,  0. ,  0. ,  0. ]])
            
        self.br = -rotateArray(self.wr)
        
        self.wq = np.array([
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2],
                [-1, 0., 0., 0., 0., 0., 0., -1],
                [-1, 0., 0.5, 0.5, 0.5, 0.5, 0., -1],
                [-0.5, 0., 0.5, 0.5, 0.5, 0.5, 0., -0.5],
                [0, 0., 0.5, 0.5, 0.5, 0.5, 0., -0.5],
                [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0., -1],
                [-1, 0., 0.5, 0., 0., 0., 0., -1],
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2]
                ])
        self.bq = -rotateArray(self.wq)
        
        self.wk = np.array([
            [ -3 ,  -4 ,  -4 ,  -5 ,  -5 ,  -4 ,  -4 ,  -3 ],
       [ -3 ,  -4 ,  -4 ,  -5 ,  -5 ,  -4 ,  -4 ,  -3 ],
       [ -3 ,  -4 ,  -4 ,  -5 ,  -5 ,  -4 ,  -4 ,  -3 ],
       [ -3 ,  -4 ,  -4 ,  -5 ,  -5 ,  -4 ,  -4 ,  -3 ],
       [ -2 ,  -3 ,  -3 ,  -4 ,  -4 ,  -3 ,  -3 ,  -2 ],
       [-1. ,  -2 ,  -2 ,  -2 ,  -2 ,  -2 ,  -2 , -1],
       [2 ,  2,  0. ,  0. ,  0. ,  0. ,  2, 2],
       [ 2 ,  3 ,  1 ,  0,  0,  1 ,  3 ,  2 ]
       ])
        self.bk = -rotateArray(self.wk)
        
        self.w_a_s = np.array([
                [0., 0., 0., 0., 0., 0., 0., 0.],
                [0., 0., 0., 0., 0., 0., 0., 0.],
                [0., 0., 0., 0., 0., 0., 0., 0.],
                [0., 0., 0., 0.3, 0.3, 0., 0., 0.],
                [0., 0., 0., 0.3, 0.3, 0., 0., 0.],
                [0., 0., 0., 0., 0., 0., 0., 0.],
                [0., 0., 0., 0., 0., 0., 0., 0.],
                [0., 0., 0., 0., 0., 0., 0., 0.]
                ])
        
        self.b_a_s = -rotateArray(self.w_a_s)
    
    
    
    #Algoritmo de minimax, se le pasa el tablero de ajedrez y la profundidad.
    #Devuelve el mejor resultado junto con el movimiento en formato uci
    def miniMax(self, board, depth):
        if depth == 0 or board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material():
            return (self.fitness(board), None)
        else:
            turn = board.turn
            moves = board.legal_moves
            
            #Maximizo el resultado para blancas
            if turn:    
                bestScore = -99999999999
                bestMove = False
                
                for move in moves:
                    board.push(move)
                    score, aux_move = self.miniMax(board, depth - 1)
                    board.pop()
                    if score > bestScore: 
                        bestScore = score
                        bestMove = move
                return (bestScore, bestMove)
            
            #Minimizo el resultado para negras
            else:
                bestScore = 9999999999
                bestMove = False
                
                for move in moves:
                    board.push(move)
                    score, aux_move = self.miniMax(board, depth - 1)
                    board.pop()
                    if score < bestScore:
                        bestScore = score
                        bestMove = move
                return (bestScore, bestMove)
        return
    
    
    
    #Algoritmo de minimax con alpha y beta, se le pasa el tablero de ajedrez y la profundidad.
    #Devuelve el mejor resultado junto con el movimiento en formato uci, por defecto
    #(alpha, beta) = (-infinity, infinity)
    def alphaBeta(self, board, depth, alpha, beta):
        #Si llega a un estado terminal vuelve hacia atras
        if depth == 0 or board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw():
            return (self.fitness(board), None)
        else:
            turn = board.turn
            moves = board.legal_moves
            
            #Maximiza blancas
            if turn:
                bestMove = False
                
                for move in moves:
                    board.push(move)
                    score, aux_move = self.alphaBeta(board, depth - 1, alpha, beta)
                    board.pop()
                    
                    if score > alpha:
                        bestMove = move
                        alpha = score
                        #Si se alcanza para para dejar de analizar mas nodos
                        if alpha >= beta:
                            break
                        
                return (alpha, bestMove)
            
            #Minimiza negras
            else:
                bestMove = False
                
                for move in moves:
                    board.push(move)
                    score, aux_move = self.alphaBeta(board, depth - 1, alpha, beta)
                    board.pop()
                    if score < beta:
                        beta = score
                        bestMove = move
                        #Si se alcanza para para dejar de analizar mas nodos
                        if beta <= alpha:
                            break
                        
                return (beta, bestMove)
    
    
    
    
    #Transforma un string de formato fen en una matriz con las piezas
    def fen_to_board(self, fen):
        board = []
        for row in fen.split('/'):
            brow = []
            for c in row:
                if c == ' ':
                    break
                elif c in '12345678':
                    brow.extend( ['--'] * int(c) )
                elif c == 'p':
                    brow.append( 'bp' )
                elif c == 'P':
                    brow.append( 'wp' )
                elif c > 'Z':
                    brow.append( 'b'+c.upper() )
                else:
                    brow.append( 'w'+c )
    
            board.append( brow )
        return board
    
    
    #Devuelve el valor material de cada pieza
    def getPieceValue(self, piece):
        if piece.upper() == "P":
            return 10
        if piece.upper() == "N":
            return 30
        if piece.upper() == "B":
            return 35
        if piece.upper() == "R":
            return 50
        if piece.upper() == "Q":
            return 90
        if piece.upper() == "K":
            return 50
        
        return 0
    
    
    #Devuelve el valor de la pieza en la posicion pos
    def getValueFromFitnessMat(self, piece_name, pos):
        nombre_pieza = piece_name.upper()
        
        if nombre_pieza == "WP":
            return self.wp[pos[0]][pos[1]]
        elif nombre_pieza == "BP":
            return self.bp[pos[0]][pos[1]]
        elif nombre_pieza == "WN":
            return self.wn[pos[0]][pos[1]]
        elif nombre_pieza == "BN":
            return self.bn[pos[0]][pos[1]]
        elif nombre_pieza == "WB":
            return self.wb[pos[0]][pos[1]]
        elif nombre_pieza == "BB":
            return self.bb[pos[0]][pos[1]]
        elif nombre_pieza == "WR":
            return self.wr[pos[0]][pos[1]]
        elif nombre_pieza == "BR":
            return self.br[pos[0]][pos[1]]
        elif nombre_pieza == "WQ":
            return self.wq[pos[0]][pos[1]]
        elif nombre_pieza == "BQ":
            return self.bq[pos[0]][pos[1]]
        elif nombre_pieza == "WK":
            return self.wk[pos[0]][pos[1]]
        elif nombre_pieza == "BK":
            return self.bk[pos[0]][pos[1]]
         
        return 0
        
    
    
    
          
    #Devuelve el ajuste de la posicion en base a si es mate y si es empate en caso
    #contrario realiza la evaluacion con las matrices de posicion de las piezas 
    # y el material correspondiente.
    def fitness(self, board):
        turn = board.turn
        
        if board.is_checkmate():
            if turn:
                return -999999
            else:
                return 999999
            
        if board.can_claim_draw() or board.is_stalemate() or board.is_insufficient_material():
            if turn:
                return 30
            else:
                return -30
            
        
        
        
        aux_board = self.fen_to_board(board.fen())
        
        res = 0
        i= 0
        for fil in aux_board:
            j = 0
            for col in fil:
                
                aux = self.getValueFromFitnessMat(col, [i, j])
                
                if col[0].upper() == "B":
                    res = res + ((-1) * self.getPieceValue(col[1])) + aux
                elif col[0].upper() == "W":
                    res = res + self.getPieceValue(col[1]) + aux
                j = j + 1
            i = i + 1
        return res
    




    