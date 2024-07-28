# Othello-Pygame-AI-Project
>>> Artificial Intelligence (AI) final project #01 - Summer 2024

# Project summary
||| In the name of Allah ||| <br />
--------------------------- <br />
Implementation of a digital Othello game using minimax (alpha-beta pruning) algorithm and Pygame library. <br />
All functions and variables are written in a Python file < Othello.py >. Read the guides and explanations of this projcet in the < Othello - Review.pdf > file ...

# Minimax Algorithm
Minimax is a backtracking algorithm used in decision-making and game theory to determine the best move for a player, provided that your opponent also plays optimally. It is commonly employed in two-player turn-based games like Tic-Tac-Toe, Backgammon, Mancala, Chess and etc. <br />
In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible. <br />
Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game. <br />

More guides and explanations: 
- Link #01: [GeeksForGeeks - Minimax](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
- Link #02: [Youtube #1 - Minimax](https://www.youtube.com/watch?v=6ELUvkSkCts)
- Link #03: [Youtube #2 - Minimax](https://www.youtube.com/watch?v=KU9Ch59-4vw&vl=en)
- Link #04: [Aparat - Minimax](https://www.aparat.com/v/l1Tba)
- Link #05: [Youtube - Minimax for TicTocToe](https://www.youtube.com/watch?v=5y2a0Zhgq0U)

## Minimax tree example
![Minimax-tree](https://github.com/user-attachments/assets/d483b0d9-4215-4b10-b328-98b8b2467c1e)

## Minimax Alpha-Beta Pruning Algorithm
