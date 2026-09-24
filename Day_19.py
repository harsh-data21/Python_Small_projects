#Day_19
class TicTacToe:
     def __init__(self,n):
         self.n = n
         self.board = [[0]*n for _ in range(n)]
         
         # creating move function
         
     def move(self, row, col, player):
         self.board[row][col] = player
         
         #Row check 
         
         row_win = True
         for c in range(self.n):
             if self.board[row][col] != player:
                row_win = False
                break
            
         # Column check
         
         col_win = True
         for r in range(self.n):
             if self.board[r][col] != player:
                col_win = False
                break

                  # Diagonal check
                  
         dag_win = True
         if row == col:
           for i in range(self.n):
               if self.board[i][i] != player:
                  diag_win = False
                  break       

            #anti diagonal check
            
         anti_diag_win = True
         if row + col == self.n - 1:
                  for i in range(self.n):
                      if self.board[i][self.n-i-1] != player:
                         anti_diag_win = False
                         break
                     
       # Return Winner
       
         if row_win or col_win or diag_win or anti_diag_win:
            return player
         return 0
                              
    

if __name__ == "__main__":

    game = TicTacToe(3)

    print(game.move(0,0,1))
    print(game.move(0,2,2))
    print(game.move(1,1,1))
    print(game.move(1,2,2))
    print(game.move(2,2,1))