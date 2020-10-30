from random import randint
from random import choice
from time import sleep

# Functions

def PrintBoard():
  for j in range(5):
    print("")
  for i in range(4):
    print(board[i])

def getLoc(board, locations):
  for i in range(4):
    for j in range(4):
      num = board[i][j]
      if num != 0:
        tempLst = [i, j, num]
        locations.append(tempLst)

def getZeros(board, zeroLoc):
  for i in range(4):
    for j in range(4):
      num = board[i][j]
      if num == 0:
        tempLst = [i, j]
        zeroLoc.append(tempLst)

# Add number to board
def RandNumGen(zeroLoc, board):
  randZero = choice(zeroLoc)
  randY = randZero[0]
  randX = randZero[1]
  i = randint(0, 3)
  if i <= 3:
    board[randY][randX] = 2
  else:
    board[randY][randX] = 4

def checkforZeros(board):
  for lst in board:
    if 0 in lst:
      return False
  return True

def checkfor2048(board):
  for lst in board:
    if 2048 in lst:
      return True
  return False

def moveNums(board, locations, direction):
  if direction == "u":
    for num in locations:
      if num[2] != 0 and num[0] != 0:
        while num[0] != 0:
          transferY = num[0]
          transferX = num[1]
          if board[transferY-1][transferX] == 0:
            board[transferY-1][transferX] = num[2]
            board[transferY][transferX] = 0
          elif board[transferY-1][transferX] != num[2]:
            break
          else:
            board[transferY-1][transferX] = num[2] * 2
            board[transferY][transferX] = 0
          num[0] -= 1
        #board[locations[num]][([0]+1)] = num
        #board[locations[num]][0] = 0
  elif direction == "d":
    for num in locations:
      if num[2] != 0 and num[0] != 3:
        while num[0] != 3:
          transferY = num[0]
          transferX = num[1]
          if board[transferY+1][transferX] == 0:
            board[transferY+1][transferX] = num[2]
            board[transferY][transferX] = 0
          elif board[transferY+1][transferX] != num[2]:
            break
          else:
            board[transferY+1][transferX] = num[2] * 2
            board[transferY][transferX] = 0
          num[0] += 1
  elif direction == "l":
    for num in locations:
      if num[2] != 0 and num[1] != 0:
        while num[1] != 0:
          transferY = num[0]
          transferX = num[1]
          if board[transferY][transferX-1] == 0:
            board[transferY][transferX-1] = num[2]
            board[transferY][transferX] = 0
          elif board[transferY][transferX-1] != num[2]:
            break
          else:
            board[transferY][transferX-1] = num[2] * 2
            board[transferY][transferX] = 0
          num[1] -= 1
  elif direction == "r":
    for num in locations:
      if num[2] != 0 and num[0] != 3:
        while num[1] != 3:
          transferY = num[0]
          transferX = num[1]
          if board[transferY][transferX+1] == 0:
            board[transferY][transferX+1] = num[2]
            board[transferY][transferX] = 0
          elif board[transferY][transferX+1] != num[2]:
            break
          else:
            board[transferY][transferX+1] = num[2] * 2
            board[transferY][transferX] = 0
          num[1] += 1

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

locations = [] 
zeroLoc = []

# Random numbers for the beginning of the getattr
for x in range(2):
  i = randint(0, 3)
  j = randint(0, 3)
  k = randint(0, 3)
  if i <= 3:
    board[j][k] = 2 
  else: 
    board[j][k] = 4

PrintBoard()

# Everything works in powers of 2
# Dictionary contains ints in multiples of 2. 0 means an empty space
# Depending on player input, move numbers
# grab all the blocks that have numbers and their location in a dictionary

# Game loop
while True:
  print("")
  player = input("Enter a direction\n").lower()
  if player == "u":
    direction = player
  elif player == "d":
    direction = player
  elif player == "l":
    direction = player
  elif player == "r":
    direction = player
  else:
    print("Sorry, I didn't understand that")
    print("")
    PrintBoard()
    continue
  print("")
  getLoc(board, locations)
  moveNums(board, locations, direction)
  getZeros(board, zeroLoc)
  RandNumGen(zeroLoc, board)
  gameEnd = checkforZeros(board)
  gameEnd2 = checkfor2048(board)
  #print(locations)
  locations.clear()
  zeroLoc.clear()
  PrintBoard()
  if gameEnd2:
    sleep(1)
    print("You have gotten to 2048! You Win!")
  if gameEnd:
    sleep(1)
    print("")
    print("You have run out of moves. Game over!")
    break
  