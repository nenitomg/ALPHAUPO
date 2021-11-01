# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:50:44 2021

@author: eugen
"""

class Square:
    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name
        self.piece = False
    
    def __str__(self):
        return "Nombre: " + self.name + "\nPosicion: [" + str(self.row) + ", " + str(self.col) + "]"
    