########################################
# HW 3 Tic-Tac-Toe MiniMax Algorithm
# Inspiration from AIMA,Russell,Novig, Shiffman
#######################################
# positive infinity
import random
p_inf = float("inf")
# negative infinity
n_inf = float("-inf")

board = [
  ['', '', ''],
  ['', '', ''],
  ['', '', '']

];

scores = {'X': 10,'O': -10,'tie': 0}
ai = 'X'
human = 'O'
currentPlayer = human

def check_for_winner():
    ####################Your code here####################
    # Code that checks for a winner
    ######################################################
    for i in range(3):#checks rows and columns
        if((board[i][0]==ai and board[i][1]==ai and board[i][2]==ai) or (board[0][i]==ai and board[1][i]==ai and board[2][i]==ai)):
            return scores['X']
        if((board[i][0]==human and board[i][1]==human and board[i][2]==human)or(board[0][i]==human and board[1][i]==human and board[2][i]==human)):
            return scores['O']
        #checks for diagnals
    if((board[0][0]==ai and board[1][1]==ai and board[2][2]==ai)or(board[0][2]==ai and board[1][1]==ai and board[2][0]==ai)):
        return scores['X']
    if((board[0][0]==human and board[1][1]==human and board[2][2]==human)or(board[0][2]==human and board[1][1]==human and board[2][0]==human)):
        return scores['O']
    if(board[0][0]!=''and board[0][1]!=''and board[0][2]!=''and board[1][0]!=''and board[1][1]!=''and board[1][2]!=''and board[2][0]!=''and board[2][1]!=''and board[2][2]!=''):
        return scores['tie']
    return 1
def minimax(board, depth, isMaximizing):
 ####################Your code here####################
 # Your implementation of minimax
 # Recursively alternates between min and max
 ######################################################
    if(check_for_winner()!=1):
        return check_for_winner()
    if(isMaximizing):
        best_val=n_inf
        for i in range(3):
            for j in range(3):
                if(board[i][j]==''):
                    board[i][j]=ai
                    value =minimax(board,depth+1,False)
                    board[i][j]=''
      #              print("maxi i: ",i," j: ",j," val: ",value," best_val:",best_val)
                    best_val=max(best_val,value)
        return best_val
    else:
        best_val=p_inf
        for i in range(3):
             for j in range(3):
                 if(board[i][j]==''):
                     board[i][j]=human
                     value =minimax(board,depth+1,True)
                     board[i][j]=''
                #     print("mini i: ",i," j: ",j," val: ",value," best_val:",best_val)
                     best_val=min(best_val,value)
        return best_val
    return 0
def find_best_move():
 ####################Your code here####################
 # Finds the best move for AI starts the minimax recursion
 ######################################################
    best_move=[-1,-1]
    best_val=n_inf
    for i in range(3):
       for j in range(3):
           if(board[i][j]==''):
              board[i][j]=ai
              val = minimax(board,0,False)#finds the value of the sugessted move
              board[i][j]=''
              if(best_val < val):#is the suggested move the current best move
                  best_move[0]=i
                  best_move[1]=j
                  best_val=val
    board[best_move[0]][best_move[1]]=ai#make the best move
def display_board():
    for i in range(3):
        print("",board[i][0],"","|","",board[i][1],"","|","",board[i][2])
        if(i<2):
            print("============")
def main ():
 ####################Your code here####################
 # Have 'X' make the first move.
 # In a loop
 # Display the board
 # Read in input from the command line to 
 # determine where 'O' would like to move.
 # After 'O' makes his move, run your minimax 
 # algorithm to decide where 'X' should move.
 # After every move print the current state of the board
 # After every move check for a winner.
 ######################################################
    print("Giving the human player a random starting move")
    r=random.randrange(3)
    c=random.randrange(3)
    board[r][c]=human
    print("Ai goes first")
    ai_r=random.randrange(3)
    ai_c=random.randrange(3)
    while(ai_r==r and ai_c==c):
            ai_r=random.randrange(3)
            ai_c=random.randrange(3)
    board[ai_r][ai_c]=ai
    display_board()
    while(check_for_winner()==1):
        move=input("Which cell would you like to put an O in? starting from the top left 0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2\n")
        row_col=move.split(",")
        if(len(row_col)>=2):
            row_col[0]=int(row_col[0])
            row_col[1]=int(row_col[1])
        while(len(row_col)<2 or row_col[0]>2 or row_col[0]<0 or row_col[1]>2 or row_col[1]<0 or(board[row_col[0]][row_col[1]]!='')):
            print("You entered an invalid move")
            move=input("Which cell would you like to put an O in? starting from the top left 0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2\n")
            row_col=move.split(",")
            if(len(row_col)>=2):
                row_col[0]=int(row_col[0])
                row_col[1]=int(row_col[1])
        board[row_col[0]][row_col[1]]="O"
        display_board()
        if(check_for_winner()==1):
            print("X's Move:")
            find_best_move()
            display_board()
    if(check_for_winner()==scores['O']): print("YOU WIN!!!")
    elif(check_for_winner()==scores['X']): print("AI WINS!!!")
    else: print("DRAW~")
#Calls on main
main()

