# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:49:34 2021

@author: eugen
"""

import copy


class Board:
    def __init__(self, pieces, squares):
        self.pieces = pieces
        self.squares = squares
        self.isCheck = False
        self.lastMove = False
        self.lastPieceTaken = False
        self.lastPieceMoved = False
    
    
    
    
    
    def isKingAttacked(self, color):
        kingPos = self.findKingPos(color)
        
        color2 = -1
        if color == 0:
            color2 = 1
        else:
            color2 = 0
            
        moves = self.getPossibleMovesWithoutChecks(color2)
        for move in moves:
            if [move[2],move[3]] == kingPos:
                return True
        
        return False
    
    
    def isKingAttackedAfterMove(self, move):
        
        
        auxBoard = copy.deepcopy(self)
        if auxBoard.squares[move[0]][move[1]].piece == False:
            return True

        color = auxBoard.squares[move[0]][move[1]].piece.color
        kingPos = auxBoard.findKingPos(color)
        
        auxBoard.makeMove(move)
        
        if [move[0],move[1]] == kingPos:
            kingPos = [move[2],move[3]]
        
        color2 = -1
        if color == 0:
            color2 = 1
        else:
            color2 = 0
        
        moves = auxBoard.getPossibleMovesWithoutChecks(color2)
            
        for move in moves:
            if [move[2],move[3]] == kingPos:
                return True

        
        return False
    
    
    def revertLastMove(self):
        self.swapInSquares(self.lastMove)
        self.pieces.append(self.lastPieceTaken)
        self.squares[self.lastMove[2]][self.lastMove[3]]
        self.lastMove = False
        self.lastPieceTaken = False
        
    
    
    def findKingPos(self, color):
        for piece in self.pieces:
            if piece.name == "k" and piece.color == color:
                return [piece.pos.row - 1, piece.pos.col - 1]
    
    def getPiecePosInPieces(self, pos):
        i = 0
        while i < len(self.pieces):
            if self.pieces[i].pos.row == pos[0] + 1 and self.pieces[i].pos.col == pos[1] + 1:
                return i
            i = i + 1
    
    def getSquareByPos(self, pos):
        
        for fila in self.squares:
            for square in fila:
                if square.row == pos[0]+1 and square.col == pos[1]+1:
                    return square
        
        print("NO SE HA ENCONTRADO LA CASILLA")
        
    def attackedByPawn(self, pawn):
        if pawn.color == 0:
            res = []
            if pawn.pos.row+1 < 9 and pawn.pos.col-1 > 0:
                res.append(self.getSquareByPos([pawn.pos.row+1, pawn.pos.col-1]))
                
            if pawn.pos.row+1 < 9 and pawn.pos.col+1 < 9:
                res.append(self.getSquareByPos([pawn.pos.row+1, pawn.pos.col+1]))
            
            for r in res:
                print(r)
            
            return res
    
    
    def getPossibleMovesWithoutChecks(self, color):
        res = []
        
        for piece in self.pieces:
            
            if piece.color == color:
                aux = piece.getMoves(self)
                
                if aux:
                    for a in aux:
                        res.append(a)
                        #print(self.getSquareByPos([a[0], a[1]]).name + " -> " + self.getSquareByPos([a[2], a[3]]).name)
                
                
        return res
    
    def getPossibleMoves(self, color):
        res = []
        
        for piece in self.pieces:
            
            if piece.color == color:
                aux = piece.getMoves(self)
                
                if aux:
                    for a in aux:
                        res.append(a)
                        #print(self.getSquareByPos([a[0], a[1]]).name + " -> " + self.getSquareByPos([a[2], a[3]]).name)
        i = 0
        while i < len(res):
            if self.isKingAttackedAfterMove(res[i]):
                
                del res[i]
            else:
                i = i + 1
                
                
        return res
                
    def getAttackedSquares(self):
        for piece in self.pieces:
            if piece.name == "":
                self.attackedByPawn(piece)
    
                
    def swapInSquares(self, move):
        aux = self.squares[move[0]][move[1]].piece
        self.squares[move[0]][move[1]].piece = self.squares[move[2]][move[3]].piece
        self.squares[move[2]][move[3]].piece = aux
    
    
    
    def makeMove(self, move):
        if self.squares[move[0]][move[1]] != False:
            

            passant = self.isOnPassant(move)
            if passant != False:
                self.lastPieceTaken = self.squares[passant[0]][passant[1]].piece
                idx2 = self.getPiecePosInPieces([passant[0], passant[1]])
                self.squares[passant[0]][passant[1]].piece = False
                del self.pieces[idx2]

            idx = self.getPiecePosInPieces([move[0], move[1]])
            self.lastPieceMoved = self.pieces[idx]
            self.lastPieceTaken = self.squares[move[2]][move[3]].piece
            idx = self.getPiecePosInPieces([move[0], move[1]])
            idx2 = -1
                    
            if self.squares[move[2]][move[3]].piece != False:
                idx2 = self.getPiecePosInPieces([move[2], move[3]])
                    
                      
                    
            self.swapInSquares(move)
            self.pieces[idx].pos = self.getSquareByPos([move[2], move[3]])
                    
            if idx2 != -1:
                del self.pieces[idx2]
                self.squares[move[0]][move[1]].piece = False 
            self.lastMove = move
            
            
            
    
            
    def isOnPassant(self, move):
        res = False
        aux = self.squares[move[0]][move[1]].piece
        
        if aux != False:
            if move != False:
                    if self.lastPieceMoved != False and self.lastPieceMoved.name == "p" and aux.name == "p":
                        if aux.color == 0:
                            if move[2] == (move[0] + 1) and move[1] == (move[3] - 1): 
                                if self.squares[move[2]][move[3]].piece == False and self.squares[move[0]][move[3]].piece != False:
                                    p1 = self.squares[move[0]][move[3]].piece
                                    if p1.color == 1:
                                        res = [move[0], move[3]]
                            
                            if move[2] == (move[0] + 1) and move[1] == (move[3] + 1): 
                                if self.squares[move[2]][move[3]].piece == False and self.squares[move[0]][move[3]].piece != False:
                                    p1 = self.squares[move[0]][move[3]].piece
                                    if p1.color == 1:
                                        res = [move[0], move[3]]
                        else:
                            if move[2] == (move[0] - 1) and move[1] == (move[3] - 1): 
                                if self.squares[move[2]][move[3]].piece == False and self.squares[move[0]][move[3]].piece != False:
                                    p1 = self.squares[move[0]][move[3]].piece
                                    if p1.color == 0:
                                        res = [move[0], move[3]]
                            
                            if move[2] == (move[0] - 1) and move[1] == (move[3] + 1): 
                                if self.squares[move[2]][move[3]].piece == False and self.squares[move[0]][move[3]].piece != False:
                                    p1 = self.squares[move[0]][move[3]].piece
                                    if p1.color == 0:
                                        res = [move[0], move[3]]
        return res
            
    
    def getMovesByPos(self, pos):
        moves = self.squares[pos[0]][pos[1]].piece.getMoves(self)
        res = []
        
        for move in moves:
            if self.isKingAttackedAfterMove(move) == False:
                res.append(move)
        
        if len(res) <= 0:
            return -1
        
        return res
    



    
                
    
    def __str__(self):
        aux = [["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"],
               ["-","-","-","-","-","-","-","-"]]
        
        for piece in self.pieces:
            pos = [piece.pos.row, piece.pos.col]
            
            if piece.color == 0:
                aux[pos[0]-1][pos[1]-1] = piece.name.upper()
            else:
                aux[pos[0]-1][pos[1]-1] = piece.name
        
        res = ""
        i=7
        while i >= 0:
            j=7
            while j >= 0:
                res += " " + str(aux[i][j]) + " "
                j = j-1
            i=i-1
            res+="\n"
                
        return res
                
    