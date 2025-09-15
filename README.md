# Blackjack Game

A console-based implementation of the classic Blackjack card game in Python.

## Game Rules

This implementation follows standard Blackjack rules:

- **Objective**: Get as close to 21 as possible without going over
- **Card Values**: 
  - Number cards (2-10): Face value
  - Face cards (J, Q, K): 10 points
  - Aces: 1 or 11 (automatically adjusted to prevent busting)
- **Blackjack**: An Ace and a 10-value card in the first two cards
- **Dealer Rules**: Must hit on 16 or less, must stand on 17 or more
- **Win Conditions**:
  - Blackjack beats all other hands
  - Higher total wins (without exceeding 21)
  - If both bust, dealer wins
  - Equal totals result in a push (tie)

## Core Features Implemented

- Standard 52-card deck with proper shuffling
- Correct card dealing order (alternating between player and dealer)
- Proper Ace handling (soft/hard hands)
- Blackjack detection and payouts
- Dealer AI following standard casino rules
- Automatic deck reshuffling when cards run low
- Win condition evaluation

## How to Run

1. Ensure you have Python 3.x installed
2. Navigate to the game directory
3. Run the game:
   ```
   python blackjack.py
   ```

## How to Play

1. The game deals two cards to you and two to the dealer (one face down)
2. Choose to **Hit** (h) for another card or **Stand** (s) to keep your current total
3. Try to get as close to 21 as possible without going over
4. The dealer will then play according to standard rules
5. The winner is determined and you can choose to play another round

## Game Controls

- `h` or `hit`: Request another card
- `s` or `stand`: Keep current hand total
- `y`: Play another round
- `n`: Quit the game

## Additional Features

- **Automatic Ace Adjustment**: Aces automatically switch between 1 and 11 to prevent unnecessary busting
- **Deck Management**: Automatic reshuffling when the deck gets low
- **Clear Game State Display**: Shows current hands and values throughout the game
- **Input Validation**: Handles invalid user inputs gracefully

This implementation focuses on the core Blackjack experience with clean, readable code structure.