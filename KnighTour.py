# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:59:41 2018
https://www.dailycodingproblem.com/blog/knights-tour/
@author: Mathu_Gopalan
"""

#Kinght Tour Puzzle
'''
Problem: Given a 8x8 chess board which is numbered from 1 to 64. 
You are given indexes of two squares, the start square and finish square. 
Please write a program to find all possible paths(limit to 10  paths) a knight can take from the start square to finish square. 
If no paths are possible print  ‘No path is possible’

'''
#creating a class
import sys, argparse
class KnightMoves:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.board = []
        self.create_board()
    
    def create_board(self):
        for i in range(self.h):
            self.board.append([0]*self.w)
    
           
    def print_board(self):       
        print ("-----Board Elements-----")
        for elem in self.board:
            print (elem)
        print ("-------------------------")
    
    def generate_possible_moves(self, cur_pos):
        possible_pos = []
        move_deltas = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_deltas:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x<0 or new_x >= self.h):
                continue
            elif (new_y <0 or new_y >= self.w):
                continue
            
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos
    
    def knights_moves_helper(self, to_visit):
        
        neighbor_list = self.generate_possible_moves(to_visit)
        empty = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty.append(neighbor)

        scores = []
        for e in empty:
            score = [e, 0]
            moves = self.generate_possible_moves(e)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours
    
    def knight_play(self, n, path, to_visit):
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)
        
        if n == self.w * self.h: #If no paths are possible print  ‘No path is possible’
            self.print_board()
            
            print ("possible paths :", path)
            print ("No path is possible!")
            sys.exit()
        else:
            sorted_neighbours = self.knights_moves_helper(to_visit)
            for neighbor in sorted_neighbours:
                self.knight_play(n+1, path, neighbor)

            
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
               path.pop()
               print ("Going back to: ", path[-1])
            except IndexError:                
                print ("No path found")
                sys.exit()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Possible Kinight Moves in Chess Board in py')
    parser.add_argument('--dim', dest="dim", action="store", type=int, default=8,
                        help ="mention the chess board diminesion, deafult (8)")
    parser.add_argument('--start_idx', dest="start", action="store", type=int, default=0,
                        help ="mention the index of start square, default(0)")
    parser.add_argument('--finish_idx', dest ="finish", action="store", type=int, default=0,
                         help="mention the index of finish square, default(0)")
    pa = parser.parse_args()
    dim=pa.dim
    start_index=pa.start
    finish_index=pa.finish
    kt = KnightMoves(dim, dim)
    kt.knight_play(1,[],(start_index,finish_index))
    kt.print_board()



