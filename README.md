# Othello-Pygame-AI-Project
>>> Artificial Intelligence (AI) final project #01 - Summer 2024

# Project summary
||| In the name of Allah ||| <br />
Implementation of a digital Othello game using minimax (alpha-beta pruning) algorithm and Pygame library. <br />
All functions and variables are written in a Python file <code>Othello - Execute.py</code>; run it to play. <br />
Read the guides and explanations of this projcet in the <code>Othello - Review.pdf</code> file.

# Minimax algorithm
Minimax is a backtracking algorithm used in decision-making and game theory to determine the best move for a player, provided that your opponent also plays optimally. It is commonly employed in two-player turn-based games like Tic-Tac-Toe, Backgammon, Mancala, Chess and etc. <br />
In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible (zero-sum). <br />
For eaxmple in a board game (zero-sum game), every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game. <br />

More guides and explanations: 
- Link #01: [GeeksForGeeks - Minimax](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
- Link #02: [Youtube #1 - Minimax](https://www.youtube.com/watch?v=6ELUvkSkCts)
- Link #03: [Youtube #2 - Minimax](https://www.youtube.com/watch?v=KU9Ch59-4vw&vl=en)
- Link #04: [Aparat - Minimax](https://www.aparat.com/v/l1Tba)
- Link #05: [Youtube - Minimax for TicTocToe](https://www.youtube.com/watch?v=5y2a0Zhgq0U)

## Minimax tree example
![Minimax-tree](https://github.com/user-attachments/assets/d483b0d9-4215-4b10-b328-98b8b2467c1e)

## Alpha-Beta Pruning algorithm
Alpha-Beta pruning is not actually a new algorithm, but rather an optimization technique for the minimax algorithm. It reduces the computation time by a huge factor. This allows us to search much faster and even go into deeper levels in the game tree. It cuts off branches in the game tree which need not be searched because there already exists a better move available. It is called Alpha-Beta pruning because it passes 2 extra parameters in the minimax function, namely alpha and beta. <br />

Let’s define the parameters alpha and beta with the pruning condition:
- **Alpha**: the best value that the maximizer currently can guarantee at that level or above. 
- **Beta**: the best value that the minimizer currently can guarantee at that level or below.
- **Pruning**: for each node, if **beta ≤ alpha**, subtree of this node is pruned.

See the links below: 
- Link #01: [GeeksForGeeks - AlphaBeta Minimax](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)
- Link #02: [Youtube #1 - AlphaBeta Minimax](https://www.youtube.com/watch?v=l-hh51ncgDI)
- Link #03: [Youtube #2 - AlphaBeta Minimax](https://www.youtube.com/watch?v=xBXHtz4Gbdo)
- Link #04: [Aparat #1 - AlphaBeta Minimax](https://www.aparat.com/v/t58lw2n)
- Link #05: [Aparat #2 - AlphaBeta Minimax](https://www.aparat.com/v/e685m0d)

# Game user interfaces
![1- Welcome menu and Game board](https://github.com/user-attachments/assets/7266a4b7-e4a1-4a91-8696-163f37182b7e)
![3- Win and Lose menu](https://github.com/user-attachments/assets/55f0aed4-787f-49b3-b80f-3ee7cadff746)

