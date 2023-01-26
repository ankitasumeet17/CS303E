
#  File: Chess.py

#  Description: how can we place eight queens on a regular chess board such that no queen can capture another using 12 distinct solutions that can generate all other solutions 

#  Student Name: Ankita Sumeet 

#  Student UT EID: as96977

#  Partner Name: Jingwen (Ivy) Lou

#  Partner UT EID: JL75477 

#  Course Name: CS 313E

#  Unique Number: A12

#  Date Created: 10/18/21

#  Date Last Modified: 10/18/21

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col, counter):
    if (col == self.n):
      counter[0] += 1
      return True
    else:
      for i in range(self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col + 1, counter)
          self.board[i][col] = '*'


  # if the problem has a solution print the board
  def solve (self, counter):
    self.recursive_solve(0, counter)


def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)
  
  # place the queens on the board and count the solutions
  counter = [0]
  game.solve(counter)

  # print the number of solutions
  x = counter[0]
  print(x)
 
if __name__ == "__main__":
  main()
