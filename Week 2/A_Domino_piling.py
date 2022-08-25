# create a Rectangular Board Size of MxN 
x, y = input().split()
### 
#we want to place as many dominoes as possible on the board so as to meet the following conditions
#1. Each domino completely covers two squares.
#2. No two dominoes overlap.Each domino lies entirely inside the board. 
#3. It is allowed to touch the edges of the board
###

### Solution==> since one Domino Piece occupy 2x1 area and 
# their can't be a half Domino Piece 
# We should have a floor Divsion of the maxmum area by area of each Domino Piece which is 2x1
Board = int(x) * int(y)
print(Board//2)

