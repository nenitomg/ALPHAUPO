# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:46:57 2021

@author: eugen
"""

class Piece:
  def __init__(self, pos, color):
    self.pos = pos
    self.color = color
    


class Pawn(Piece):
    name = "p"
    hasMoved=False
    
    def getMoves(self, board):
        res = []
        i = self.pos.row-1
        j = self.pos.col -1
        
        
        if self.color == 1:
            if self.hasMoved == False and board.squares[i-1][j-1].piece == False and board.squares[i-2][j].piece == False:
                res.append([i, j, i-2, j])
            
            if board.squares[i-1][j].piece == False:
                res.append([i, j, i-1, j])
            
            if i > 0 and j > 0:
                if board.squares[i-1][j-1].piece != False and board.squares[i-1][j-1].piece.color != self.color:
                    res.append([i, j, i-1, j-1])

            if i > 0 and j+2 < 9:
                if board.squares[i-1][j+1].piece != False and board.squares[i-1][j+1].piece.color != self.color:
                    res.append([i, j, i-1, j+1])
               
            move = board.lastMove
            
            if move != False:
                if move[2] == 3 and move[0] == 1 and board.lastPieceMoved.name == "p":
                    i = self.pos.row - 1
                    j = self.pos.col - 1
                    
                    if i == 3:
                        if (j - 1) >= 0 and (j - 1) == move[3]:
                            res.append([i, j, (i - 1), (j - 1)])
                        if (j + 1) < 9 and (j + 1) == move[3]:
                            res.append([i, j, (i - 1), (j + 1)])

        

        i = self.pos.row-1
        j = self.pos.col -1
        
        if self.color == 0:
            if self.hasMoved == False and board.squares[i+1][j].piece == False and board.squares[i+2][j].piece == False:
                res.append([i, j, i+2, j])
            
            if board.squares[i+1][j].piece == False:
                res.append([i, j, i+1, j])
            
            
            if self.pos.row+1 < 9 and self.pos.col-1 > 0:
                if board.squares[i+1][j-1].piece != False and board.squares[i+1][j-1].piece.color != self.color:
                    res.append([i, j, i+1, j-1])
                        
            if i + 2 < 9 and j + 2 < 9:
                if board.squares[i+1][j+1].piece != False and board.squares[i+1][j+1].piece.color != self.color:
                    res.append([i, j, i+1, j+1])
            
            move = board.lastMove
            
            
            
            if move != False:

                if move[2] == 4 and move[0] == 6 and board.lastPieceMoved.name == "p":
                    i = self.pos.row - 1
                    j = self.pos.col - 1
                    
                    if i == 4:
                        if (j - 1) >= 0 and (j - 1) == move[3]:
                            res.append([i, j, (i + 1), (j - 1)])
                        if (j + 1) < 9 and (j + 1) == move[3]:
                            res.append([i, j, (i + 1), (j + 1)])
                    
                
            
        return res
    
    
    
class Knight(Piece):
    name = "n"
    
    def getMoves(self, board):
        res = []
        
        if self.pos.row - 2 > 0 and self.pos.col + 1 < 9:
            if board.squares[self.pos.row-2-1][self.pos.col+1-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-2-1, self.pos.col-1+1])
            elif board.squares[self.pos.row-2-1][self.pos.col+1-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-2-1, self.pos.col-1+1])
                
                
        if self.pos.row - 2 > 0 and self.pos.col - 1 > 0:
            if board.squares[self.pos.row-2-1][self.pos.col-1-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-2-1, self.pos.col-1-1])
            elif board.squares[self.pos.row-2-1][self.pos.col-1-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-2-1, self.pos.col-1-1])
                
        if self.pos.row - 1 > 0 and self.pos.col + 2 < 9:
            if board.squares[self.pos.row-1-1][self.pos.col+2-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-1-1, self.pos.col+2-1])
            elif board.squares[self.pos.row-1-1][self.pos.col+2-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-1-1, self.pos.col+2-1])
          
        if self.pos.row + 1 < 9 and self.pos.col + 2 < 9:
            if board.squares[self.pos.row+1-1][self.pos.col+2-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+1-1, self.pos.col+2-1])
            elif board.squares[self.pos.row+1-1][self.pos.col+2-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+1-1, self.pos.col+2-1])
        
        if self.pos.row + 2 < 9 and self.pos.col + 1 < 9:
            if board.squares[self.pos.row+2-1][self.pos.col+1-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+2-1, self.pos.col+1-1])
            elif board.squares[self.pos.row+2-1][self.pos.col+1-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+2-1, self.pos.col+1-1])
        
        if self.pos.row + 2 < 9 and self.pos.col -1 > 0:
            if board.squares[self.pos.row+2-1][self.pos.col-1-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+2-1, self.pos.col-1-1])
            elif board.squares[self.pos.row+2-1][self.pos.col-1-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+2-1, self.pos.col-1-1])
        
        if self.pos.row + 1 < 9 and self.pos.col -2 > 0:
            if board.squares[self.pos.row+1-1][self.pos.col-2-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+1-1, self.pos.col-2-1])
            elif board.squares[self.pos.row+1-1][self.pos.col-2-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row+1-1, self.pos.col-2-1])
        
        if self.pos.row - 1 > 0 and self.pos.col - 2 > 0:
            if board.squares[self.pos.row-1-1][self.pos.col-2-1].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-1-1, self.pos.col-2-1])
            elif board.squares[self.pos.row-1-1][self.pos.col-2-1].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, self.pos.row-1-1, self.pos.col-2-1])

        
        

        return res
    
class Bishop(Piece):
    name = "b"
    
    def getMoves(self, board):
        res = []
        i = self.pos.row
        j = self.pos.col
        
        ##Diagonal arriba izquierda
        while (i < 8) and (j < 8):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=9
            else:
                i=9
            
            i = i + 1
            j = j + 1
            
        ##Diagonal abajo izquierda
        i = self.pos.row - 2
        j = self.pos.col
        while (i >= 0) and (j < 8):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=-1
            else:
                i=-1
            
            i = i - 1
            j = j + 1
            
         ##Diagonal abajo derecha
        i = self.pos.row - 2
        j = self.pos.col - 2
        while (i >= 0) and (j >= 0):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=-1
            else:
                i=-1
            
            i = i - 1
            j = j - 1
            
        
        ##Diagonal abajo derecha
        i = self.pos.row
        j = self.pos.col - 2
        while (i < 8) and (j >= 0):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=9
            else:
                i=9
            
            i = i + 1
            j = j - 1
        
        
        
        return res
    
    
class Rook(Piece):
    name = "r"
    
    
    def getMoves(self, board):
        res = []
        col = self.pos.col-1
        fil = self.pos.row-1
        
        i = self.pos.row
        while i < 8:
            if board.squares[i][col].piece == False:
                res.append([fil, col, i, col])
            elif board.squares[i][col].piece.color != self.color:
                res.append([fil, col, i, col])
                i = 8
            else:
                i = 8
            i = i + 1
            
        i = self.pos.row - 2
        while i >= 0:
            if board.squares[i][col].piece == False:
                res.append([fil, col, i, col])
            elif board.squares[i][col].piece.color != self.color:
                res.append([fil, col, i, col])
                i = -1
            else:
                i = -1
            i = i - 1
            
            
        j = self.pos.col
        while j < 8:
            if board.squares[fil][j].piece == False:
                res.append([fil, col, fil, j])
            elif board.squares[fil][j].piece.color != self.color:
                res.append([fil, col, fil, j])
                j = 8
            else:
                j = 8
            j = j + 1
            
        
            
        j = self.pos.col - 2
        while j >= 0:
            if board.squares[fil][j].piece == False:
                res.append([fil, col, fil, j])
            elif board.squares[fil][j].piece.color != self.color:
                res.append([fil, col, fil, j])
                j = -1
            else:
                j = -1
            j = j - 1
        
            
        
        
        return res
    
        
    
    
class Queen(Piece):
    name = "q"
    
    def getMoves(self, board):
        res = []
        col = self.pos.col-1
        fil = self.pos.row-1
        
        i = self.pos.row
        while i < 8:
            if board.squares[i][col].piece == False:
                res.append([fil, col, i, col])
            elif board.squares[i][col].piece.color != self.color:
                res.append([fil, col, i, col])
                i = 8
            else:
                i = 8
            i = i + 1
            
        i = self.pos.row - 2
        while i >= 0:
            if board.squares[i][col].piece == False:
                res.append([fil, col, i, col])
            elif board.squares[i][col].piece.color != self.color:
                res.append([fil, col, i, col])
                i = -1
            else:
                i = -1
            i = i - 1
            
            
        j = self.pos.col
        while j < 8:
            if board.squares[fil][j].piece == False:
                res.append([fil, col, fil, j])
            elif board.squares[fil][j].piece.color != self.color:
                res.append([fil, col, fil, j])
                j = 8
            else:
                j = 8
            j = j + 1
            
        
            
        j = self.pos.col - 2
        while j >= 0:
            if board.squares[fil][j].piece == False:
                res.append([fil, col, fil, j])
            elif board.squares[fil][j].piece.color != self.color:
                res.append([fil, col, fil, j])
                j = -1
            else:
                j = -1
            j = j - 1
            
        i = self.pos.row
        j = self.pos.col
        
        ##Diagonal arriba izquierda
        while (i < 8) and (j < 8):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=9
            else:
                i=9
            
            i = i + 1
            j = j + 1
            
        ##Diagonal abajo izquierda
        i = self.pos.row - 2
        j = self.pos.col
        while (i >= 0) and (j < 8):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=-1
            else:
                i=-1
            
            i = i - 1
            j = j + 1
            
         ##Diagonal abajo derecha
        i = self.pos.row - 2
        j = self.pos.col - 2
        while (i >= 0) and (j >= 0):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=-1
            else:
                i=-1
            
            i = i - 1
            j = j - 1
            
        
        ##Diagonal abajo derecha
        i = self.pos.row
        j = self.pos.col - 2
        while (i < 8) and (j >= 0):
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            elif board.squares[i][j].piece.color != self.color:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
                i=9
            else:
                i=9
            
            i = i + 1
            j = j - 1
        
        
        
        
        return res

    
    
class King(Piece):
    name = "k"
    
    def getMoves(self, board):
        res = []
        
        
        i = self.pos.row
        j = self.pos.col
        
        
        if i < 8 and j < 8:
            if board.squares[i][j].piece == False:
                res.append([self.pos.row-1, self.pos.col-1, i, j])
            
            else:
                if board.squares[i][j].piece.color != self.color:
                    res.append([self.pos.row-1, self.pos.col-1, i, j])
          
            
          
        
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        
        if (i + 1) < 8 and (j - 1) >= 0:
            if board.squares[i + 1][j - 1].piece == False:
                res.append([i, j, i + 1, j - 1])
            else:
            
                if board.squares[i + 1][j - 1].piece.color != self.color:
                    res.append([i, j, i + 1, j - 1])
            
            
            
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        if (i - 1) >= 0 and (j + 1) < 8:
            if board.squares[i - 1][j + 1].piece == False:
                res.append([i, j, i - 1, j + 1])
            else:
            
                if board.squares[i - 1][j + 1].piece.color != self.color:
                    res.append([i, j, i - 1, j + 1])
        
        
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        if (i - 1) >= 0 and (j - 1) >= 0:
            if board.squares[i - 1][j - 1].piece == False:
                res.append([i, j, i - 1, j - 1])
            else:
                if board.squares[i - 1][j - 1].piece.color != self.color:
                    res.append([i, j, i - 1, j - 1])
            
        
        
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        if (i + 1) < 8:
            if board.squares[i + 1][j].piece == False:
                res.append([i, j, i + 1, j])
            else:
                if board.squares[i + 1][j].piece.color != self.color:
                    res.append([i, j, i + 1, j])
            
            
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        if (i - 1) >= 0:
            if board.squares[i - 1][j].piece == False:
                res.append([i, j, i - 1, j])
            else:
                if board.squares[i - 1][j].piece.color != self.color:
                    res.append([i, j, i - 1, j])
        
        
        
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        if (j + 1) < 8:
            if board.squares[i][j + 1].piece == False:
                res.append([i, j, i, j + 1])
            else:
                if board.squares[i][j + 1].piece.color != self.color:
                    res.append([i, j, i, j + 1])
        
        
        
        
        i = self.pos.row - 1
        j = self.pos.col - 1
        
        if (j - 1) >= 0:
            if board.squares[i][j - 1].piece == False:
                res.append([i, j, i, j - 1])
            else:
                if board.squares[i][j - 1].piece.color != self.color:
                    res.append([i, j, i, j - 1])
        
        
        
        
        return res