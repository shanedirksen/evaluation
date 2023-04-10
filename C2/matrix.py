import numpy as np

class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))
    
    def largest_index(self, matrix):
        max_val = matrix[0, 0]
        max_index = (0, 0)

        #iterate through the matrix
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                if matrix[row, col] > max_val:
                    max_val = matrix[row, col]
                    max_index = (row, col)

        return max_index

    def convolve(self, kernel, matrix):
        rows, cols = matrix.shape
        k_rows, k_cols = kernel.shape
        #get the padding
        pad_rows = k_rows // 2
        pad_cols = k_cols // 2

        #initialize padded matrix
        padded_matrix = np.zeros((rows + 2 * pad_rows, cols + 2 * pad_cols))
        padded_matrix[pad_rows:-pad_rows, pad_cols:-pad_cols] = matrix

        #convolve
        convolved_matrix = np.zeros_like(matrix)
        for row in range(rows):
            for col in range(cols):
                convolved_matrix[row, col] = np.sum(padded_matrix[row:row + k_rows, col:col + k_cols] * kernel)

        return convolved_matrix

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run() 