class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to store non-zero elements with (row, col) as the key

    # Method to set a value in the sparse matrix
    def set_value(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value  # Store non-zero values
        elif (row, col) in self.data:
            del self.data[(row, col)]  # Remove the entry if value is 0

    # Method to get the value from the sparse matrix
    def get_value(self, row, col):
        return self.data.get((row, col), 0)  # Default to 0 if not found

    # Method to add another sparse matrix to the current one
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of the same dimensions for addition.")
        
        result = SparseMatrix(self.rows, self.cols)
        
        # Add all non-zero values from the first matrix
        for (row, col), value in self.data.items():
