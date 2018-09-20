##Read Me:

Knight Tour possible positions
given the problem statement as 

Problem: Given a 8x8 chess board which is numbered from 1 to 64. 
You are given indexes of two squares, the start square and finish square. 
Please write a program to find all possible paths(limit to 10  paths) a knight can take from the start square to finish square. 
If no paths are possible print  ‘No path is possible’

how to run the code
>>> python KnighTour.py -h

usage: KnighTour.py [-h] [--dim DIM] [--start_idx START] [--finish_idx FINISH]

Possible Kinight Moves in Chess Board in py

optional arguments:
  -h, --help           show this help message and exit
  --dim DIM            mention the chess board diminesion (deafult 8)
  --start_idx START    mention the index of start square, default(0)
  --finish_idx FINISH  mention the index of finish square, default(0)
  
>>> python KnighTour.py --dim 8 --start_idx 1 --finish_idx 1

Results:
-----Board Elements-----
[39, 46, 15, 2, 21, 36, 17, 4]
[14, 1, 38, 45, 16, 3, 20, 35]
[47, 40, 13, 22, 37, 64, 5, 18]
[12, 23, 48, 61, 44, 19, 34, 63]
[49, 60, 41, 30, 55, 62, 43, 6]
[24, 11, 56, 59, 42, 29, 54, 33]
[57, 50, 9, 26, 31, 52, 7, 28]
[10, 25, 58, 51, 8, 27, 32, 53]
-------------------------
possible paths : [(1, 1), (0, 3), (1, 5), (0, 7), (2, 6), (4, 7), (6, 6), (7, 4), (6, 2), (7, 0), (5, 1), (3, 0), (2, 2), (1, 0), (0, 2), (1, 4), (0, 6), (2, 7), (3, 5), (1, 6), (0, 4), (2, 3), (3, 1), (5, 0), (7, 1), (6, 3), (7, 5), (6, 7), (5, 5), (4, 3), (6, 4), (7, 6), (5, 7), (3, 6), (1, 7), (0, 5), (2, 4), (1, 2), (0, 0), (2, 1), (4, 2), (5, 4), (4, 6), (3, 4), (1, 3), (0, 1), (2, 0), (3, 2), (4, 0), (6, 1), (7, 3), (6, 5), (7, 7), (5, 6), (4, 4), (5, 2), (6, 0), (7, 2), (5, 3), (4, 1), (3, 3), (4, 5), (3, 7), (2, 5)]
No path is possible!
