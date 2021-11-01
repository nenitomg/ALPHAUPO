# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:58:37 2021

@author: eugen
"""
import Piece as pc
import Board as boa
import Square
import numpy as np

def setUpBoard():
        letters = ["H", "G", "F", "E", "D", "C", "B", "A"]
        squares = np.empty((8,8), dtype=object)
        
        for i in range(1,9):
            for j in range(1,9):
                
                squares[i-1][j-1] = Square.Square(i, j, (letters[j-1] + str(i)))

                
        pieces = []
        
        
        for i in range(0,8):
            pawn = pc.Pawn(squares[1][i], 0)
            squares[1][i].piece = pawn
            pawn2 = pc.Pawn(squares[6][i], 1)
            squares[6][i].piece = pawn2
            pieces.append(pawn)
            pieces.append(pawn2)
        
        ro = pc.Rook(squares[0][0], 0)
        squares[0][0].piece = ro
        ro2 = pc.Rook(squares[0][7], 0)
        squares[0][7].piece = ro2
        pieces.append(ro)
        pieces.append(ro2)
        
        ro = pc.Rook(squares[7][0], 1)
        squares[7][0].piece = ro
        ro2 = pc.Rook(squares[7][7], 1)
        squares[7][7].piece = ro2
        pieces.append(ro)
        pieces.append(ro2)
        
        ni = pc.Knight(squares[0][1], 0)
        squares[0][1].piece = ni
        ni2 = pc.Knight(squares[0][6], 0)
        squares[0][6].piece = ni2
        pieces.append(ni)
        pieces.append(ni2)
        
        ni = pc.Knight(squares[7][1], 1)
        squares[7][1].piece = ni
        ni2 = pc.Knight(squares[7][6], 1)
        squares[7][6].piece = ni2
        pieces.append(ni)
        pieces.append(ni2)
        
        bi = pc.Bishop(squares[0][2], 0)
        squares[0][2].piece = bi
        bi2 = pc.Bishop(squares[0][5], 0)
        squares[0][5].piece = bi2
        pieces.append(bi)
        pieces.append(bi2)
        
        bi = pc.Bishop(squares[7][2], 1)
        squares[7][2].piece = bi
        bi2 = pc.Bishop(squares[7][5], 1)
        squares[7][5].piece = bi2
        pieces.append(bi)
        pieces.append(bi2)
        
        que = pc.Queen(squares[0][4], 0)
        squares[0][4].piece = que
        kin = pc.King(squares[0][3], 0)
        squares[0][3].piece = kin
        pieces.append(que)
        pieces.append(kin)
        
        que = pc.Queen(squares[7][4], 1)
        squares[7][4].piece = que
        kin = pc.King(squares[7][3], 1)
        squares[7][3].piece = kin
        pieces.append(que)
        pieces.append(kin)
         
        """
        kin = pc.King(squares[7][6], 0)
        squares[7][6].piece = kin
        pieces.append(kin)
        
        
        ro1 = pc.Rook(squares[6][0], 1)
        squares[6][0].piece = ro1
        pieces.append(ro1)
        
        ro2 = pc.Rook(squares[0][0], 1)
        squares[0][0].piece = ro2
        pieces.append(ro2)
        """
        
        return boa.Board(pieces, squares)
        
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = setUpBoard()
        self.moves = []
        self.toMove = 0
        self.winner = False
        
    def makeMove(self, move):
        if self.board.squares[move[0]][move[1]].piece != False:
            if self.board.squares[move[0]][move[1]].piece.color == self.toMove:
                if move in self.board.getMovesByPos([move[0], move[1]]):
                    
                    if self.board.squares[move[0]][move[1]].piece.name == "p":
                        aux = self.board.getPiecePosInPieces([move[0], move[1]])
                        self.board.squares[move[0]][move[1]].piece.hasMoved = True
                        self.board.pieces[aux].hasMoved = True
                    
                    
                    self.board.makeMove(move)
                    """
                    idx = self.board.getPiecePosInPieces([move[0], move[1]])
                    idx2 = -1
                    
                    if self.board.squares[move[2]][move[3]].piece != False:
                        idx2 = self.board.getPiecePosInPieces([move[2], move[3]])
                    
                      
                    
                    self.board.swapInSquares(move)
                    self.board.pieces[idx].pos = self.board.getSquareByPos([move[2], move[3]])
                    
                    if idx2 != -1:
                        del self.board.pieces[idx2]
                        self.board.squares[move[0]][move[1]].piece = False  
                    """
                    
                
                    self.moves.append(move)
                    
                    
                    
                    if self.toMove == 0:
                        self.toMove = 1
                    else:
                        self.toMove = 0

                    if len(self.board.getPossibleMoves(self.toMove)) <= 0:
                        if self.board.isKingAttacked(self.toMove):
                            print("CHECKMATE")
                            if self.toMove == 0:
                                self.winner = "0-1"
                            else:
                                self.winner = "1-0"
                        else:
                            self.winner = "0-0"
                            print("STALEMATE")

                    return move

        print("El movimiento ", move , " es erroneo. Color a mover: ", self.toMove)
        return -1
    

    def makeMoveByNotation(self, notation):
        letters = ["H", "G", "F", "E", "D", "C", "B", "A"]
        aux = [int(notation[1]) - 1, letters.index(notation[0]), int(notation[3]) -1, letters.index(notation[2])]
        
        self.makeMove(aux)
        
        
        
        
    