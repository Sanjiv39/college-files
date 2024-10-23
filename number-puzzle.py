import random

class Puzzle:
    def __init__(self):
        self.state = self.initialize_puzzle()
    
    def initialize_puzzle(self):
        """Initialize the puzzle with a random configuration."""
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(puzzle)
        return puzzle
    
    def display(self):
        """Display the current state of the puzzle."""
        print("\nCurrent puzzle state:")
        for i in range(3):
            print(self.state[i * 3:(i + 1) * 3])
        print()
    
    def find_zero(self):
        """Find the position of the blank space (0) in the puzzle."""
        return self.state.index(0)

    def is_solvable(self):
        """Check if the puzzle is solvable."""
        inversions = 0
        for i in range(len(self.state)):
            for j in range(i + 1, len(self.state)):
                if self.state[i] != 0 and self.state[j] != 0 and self.state[i] > self.state[j]:
                    inversions += 1
        return inversions % 2 == 0
    
    def move(self, direction):
        """Move the blank space in the specified direction."""
        zero_index = self.find_zero()
        row, col = divmod(zero_index, 3)
        if direction == "up" and row > 0:
            self.state[zero_index], self.state[zero_index - 3] = self.state[zero_index - 3], self.state[zero_index]
        elif direction == "down" and row < 2:
            self.state[zero_index], self.state[zero_index + 3] = self.state[zero_index
            + 3], self.state[zero_index]
        elif direction == "left" and col > 0:
            self.state[zero_index], self.state[zero_index - 1] = self.state[zero_index -
            1], self.state[zero_index]
        elif direction == "right" and col < 2:
            self.state[zero_index], self.state[zero_index + 1] = self.state[zero_index
            + 1], self.state[zero_index]
    
    def play(self):
        """Start the game."""
        print("Welcome to the 8-Puzzle Game!")
        self.display()
        while True:
            if self.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
                print("Congratulations! You've solved the puzzle!")
                break
            move = input("Enter your move (up, down, left, right) or 'quit' to exit:").strip().lower()
            if move == "quit":
                print("Thanks for playing!")
                break
            elif move in ["up", "down", "left", "right"]:
                self.move(move)
                self.display()
            else:
                print("Invalid move. Please try again.")

if __name__ == "__main__":
    puzzle = Puzzle()

# Ensure the puzzle is solvable
    while not puzzle.is_solvable():
        puzzle = Puzzle()
puzzle.play()