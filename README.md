
# 4x4 Tic-Tac-Toe with Depth-Limited Minimax 🎮🧠

This project implements a 4x4 Tic-Tac-Toe game with an AI player that uses a depth-limited version of the minimax algorithm. The AI has three difficulty levels: Easy, Medium, and Hard.

## Features ✨
- 🤖 AI opponent using the Minimax algorithm with alpha-beta pruning
- 🎯 4x4 grid for more challenging gameplay
- 🆚 Human vs AI mode with three difficulty levels

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone git@github.com:marielouisehanna/Tic_Tac_Toe_Minimax_Project.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play 🎮
- Run the game with:
   ```bash
   python main.py
   ```
- Choose your difficulty level and play against the AI!

## AI Difficulty Levels 💡
- **Easy**: The AI looks 1-2 moves ahead.
- **Medium**: The AI looks 3-4 moves ahead.
- **Hard**: The AI looks further ahead and makes the best possible decisions.

## Minimax Algorithm 🧠
The AI uses the Minimax algorithm with alpha-beta pruning to efficiently search through game states, evaluating moves based on a heuristic that considers winning and blocking strategies.
