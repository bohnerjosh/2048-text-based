# 2048-text-based
README

This game is a text-based remake of the popular online game 2048. The original game uses a 4x4 grid of squares
with numbers that are multiples of 2. These squares can be moved around with the arrow keys. When you
select a direction, the blocks will go as far in that direction as they can go before running into the
edge of the 4x4 grid or other blocks. 
When 2 or more blocks collide, 2 things can happen. If both blocks are of the same multiple of 2, 
they combine into the next multiple of 2 and continue in the direction selected. If the blocks are
not of the same multiple, they do not combine, and continue shifting until the edge of the 4x4 grid
is reached.
The game ends when at least one of the blocks reaches the number 2048, or there are no moves left as
a result of all 4x4 grid spaces filled with numbers that are different multiples of 2. 

My text based version contains all of the functionality of the original game above, but the visual
interface is text in the command line. Additionally, movement is based on inputs of the direction you
want the blocks to move in, not the arrow keys. Up is u, down is d, left is l, and right is r. Finally,
the command line is result of printing the lists directly to the screen. After trying a few different 
interfaces, I decided that printing these directly was the most time saving and efficient UI going forward.
