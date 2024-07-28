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
More guides and explanations: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
