import pygame
import os


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
   
    def isSelected(self):
        return self.selected
    
    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)
    
    def draw(self):
        pass

    def change_pos(self, pos):
        self.row = pos[0]
        self.col[1]
    
class Bishop(Piece):
    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        return moves

class King(Piece):
    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        return moves

class Rook(Piece):
        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []
            return moves

class Knight(Piece):
        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []
            return moves

class Queen(Piece):
        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []
            return moves

class Pawn(Piece):
        def valid_moves(self, board):
            i = self.row
            j = self.col

            moves = []
            return moves