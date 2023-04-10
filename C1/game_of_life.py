import numpy as np
import time


class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=10):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen

    
    def update(self):
        new_board = np.copy(self._board)
        rows, cols = self._board.shape

        #iterate through board
        for row in range(rows):
            for col in range(cols):
                alive_neighbors = 0
                #iterate through neighbors
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0: #pass over current cell
                            continue
                        # get the neighbor indices (including wrapping around the board)
                        r = (row + i) % rows
                        c = (col + j) % cols
                        alive_neighbors += self._board[r, c] #get the living neighbors
                #if cell is alive with too few/too many neighbors, it dies
                if self._board[row, col] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[row, col] = 0
                #new cell is born
                else:
                    if alive_neighbors == 3:
                        new_board[row, col] = 1

        self._board = new_board


    def play(self, delay=.1):
        while self._gen < self._max_gen:
            # Start the generation by drawing the current board
            self.draw()
            
            # Next we update each of the cells according to the rules 
            self.update()

            # Increment the generation and sleep to make the visualization easier
            self._gen += 1
            time.sleep(delay)

    def time_run(self, gens=1000):
        start = time.time()
        for _ in range(gens):
            self.update()
        print(f'Average update time: {(time.time()-start)/gens*1000} ms')

    def draw(self):
        for row in self._board:   
            # Print a full block for each alive cell and an empty one for dead cells bounded by |
            print('|'.join(['▇' if c else ' ' for c in row]))

        print(f'Generation: {self._gen}')


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    g.time_run()
    g.play()  # Uncomment this to see the generational progression