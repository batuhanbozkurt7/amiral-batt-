print ("""  
  ___    _/ |~
  \\ ,`--' ooo'---+
   \^            |
 ~~~~   -- '' -'-'""")

import random
board = []


for x in range(0,5):
  board.append(["o"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print("amiral battıya hoşgeldin")
print("2 kişilik")

player_1 = input("birinci oyuncu adı: ")
player_2 = input("ikinci oyuncu adı: ")
players = [player_1, player_2]

def random_player(players):
    return random.choice(players)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

if random_player(players) == player_1:
  print(player_1, "başla")
else:
  print(player_2, "başla")
  
ship_row_1 = random_row(board)
ship_col_1 = random_col(board)


ship_row_2 = random_row(board)
ship_col_2 = random_col(board)


print_board(board)

player_start = random_player(players)




hit_count = 0

for turn in range(4):
     guess_row = int(input("birinci tahmin (izin verilen değerler: 0-4) "))
     guess_col = int(input("ikinci tahmin(izin verilen değerler: 0-4) "))

     if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("tebrikler")
            if hit_count == 1:
                   print("savaş gemisini vurdun") 
            elif hit_count == 2:
                   print("ikinci savaş gemisini vurdun")
                   print_board(board)
                   break
     else:
            if(guess_row<=4 or guess_col<=0):
              if(board[guess_row][guess_col] == "X"):
                   print ("tahmin ettin.")
              else:
                 print ("savaşı kaçırdın")
                 board[guess_row][guess_col] = "X"
            else:
              print ("KAPTAAAN dağa taşa ateş ediyorsun.")
            print (turn + 1, "turn")
     print_board(board)
    
print ("birinci kişi")    
print (ship_row_1)
print (ship_col_1)

print ("ikinci kişi")    
print (ship_row_2)
print (ship_col_2)



