def generate_magic_square(n):
    """
    Generates a magic square of order n.
    
    Args:
        n (int): The order of the magic square (must be >= 1).
    
    Returns:
        list[list[int]]: A 2D list representing the magic square.
    """
    if n < 1:
        raise ValueError("Order must be at least 1")
    if n == 2:
        raise ValueError("Magic square of order 2 does not exist")
        
    if n % 2 != 0:
        return _odd_magic_square(n)
    elif n % 4 == 0:
        return _doubly_even_magic_square(n)
    else:
        return _singly_even_magic_square(n)

def _odd_magic_square(n):
    """
    Generates an odd order magic square using the Siamese method.
    """
    magic_square = [[0] * n for _ in range(n)]
    
    # Start position for 1 is the middle of the first row
    i, j = 0, n // 2
    
    num = 1
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        
        # Move up and right
        new_i, new_j = (i - 1) % n, (j + 1) % n
        
        # If the cell is already filled, move down instead
        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
            
    return magic_square

def _doubly_even_magic_square(n):
    """
    Generates a doubly even order magic square (n % 4 == 0).
    Uses the method of inverting values on the diagonals of 4x4 subgrids.
    """
    magic_square = [[(i * n + j + 1) for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Check if the cell is on the diagonal of a 4x4 subgrid
            # A 4x4 subgrid covers rows r to r+3 and cols c to c+3 where r%4==0, c%4==0
            # Diagonals condition in 0-indexed 4x4 block: 
            # Main diag: r == c, Anti diag: r + c == 3
            # Global coordinates:
            # Main diagonal condition: i % 4 == j % 4
            # Anti diagonal condition: (i % 4 + j % 4) == 3
            
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                magic_square[i][j] = (n * n + 1) - magic_square[i][j]
                
    return magic_square

def _singly_even_magic_square(n):
    """
    Generates a singly even order magic square (n % 4 == 2) using the LUX method.
    """
    size = n // 2
    half_square = _odd_magic_square(size)
    
    magic_square = [[0] * n for _ in range(n)]
    
    # Quadrants:
    # A B
    # C D 
    # But usually filled: Top-Left (A), Bottom-Right (B), Top-Right (C), Bottom-Left (D)
    # The LUX method uses a specific pattern of L, U, X blocks.
    
    # We will build it block by block.
    # Pattern assignment for the size x size grid of 2x2 blocks:
    # Top k rows: L
    # Next 1 row: U
    # Bottom k-1 rows: X
    # Middle U is swapped with L above it.
    
    k = (size - 1) // 2
    
    # Create the block pattern grid
    # L = 0, U = 1, X = 2 (just for internal logic)
    # Actually, let's define the 2x2 patterns directly.
    # L: [[4, 1], [2, 3]]
    # U: [[1, 4], [2, 3]]
    # X: [[1, 4], [3, 2]]
    
    # The numbers in the blocks are derived from the half_square values.
    # If half_square[r][c] is v, then the 4 values in the 2x2 block are:
    # 4*(v-1) + 1, 4*(v-1) + 2, 4*(v-1) + 3, 4*(v-1) + 4
    # The pattern determines how these 1,2,3,4 are placed.
    
    L_pattern = [[4, 1], [2, 3]]
    U_pattern = [[1, 4], [2, 3]]
    X_pattern = [[1, 4], [3, 2]]
    
    # Initialize pattern grid
    pattern_grid = [['L'] * size for _ in range(size)]
    
    # Set patterns according to LUX rules
    # First k+1 rows are L (wait, rule is k rows L, 1 row U, k-1 rows X)
    # Let's recheck Conway's LUX method specifics for n = 4k+2.
    # m = n/2 = 2k+1.
    # Rows 0 to k: L
    # Row k+1: U
    # Rows k+2 to 2k: X
    # Swap the U in the center (row k+1, col k) with the L above it (row k, col k)
    
    for r in range(size):
        for c in range(size):
            if r <= k:
                pattern_grid[r][c] = 'L'
            elif r == k + 1:
                pattern_grid[r][c] = 'U'
            else:
                pattern_grid[r][c] = 'X'
                
    # Swap clean-up
    pattern_grid[k][k] = 'U'
    pattern_grid[k+1][k] = 'L'
    
    for r in range(size):
        for c in range(size):
            val = half_square[r][c]
            start = 4 * (val - 1)
            
            pat = None
            if pattern_grid[r][c] == 'L':
                pat = L_pattern
            elif pattern_grid[r][c] == 'U':
                pat = U_pattern
            elif pattern_grid[r][c] == 'X':
                pat = X_pattern
                
            # Fill the 2x2 block in the main magic square
            for pr in range(2):
                for pc in range(2):
                    magic_square[2*r + pr][2*c + pc] = start + pat[pr][pc]

    return magic_square

def print_magic_square(square):
    """
    Prints the magic square in a formatted way.
    """
    n = len(square)
    # Calculate max width of a number for alignment
    max_val = n * n
    width = len(str(max_val)) + 2
    
    print(f"Magic Square of Order {n}:")
    print(f"Magic Constant: {n * (n*n + 1) // 2}")
    for row in square:
        print("".join(f"{num:>{width}}" for num in row))
    print("-" * 20)

def verify_magic_square(square):
    """
    Verifies if a square is a valid magic square.
    """
    n = len(square)
    magic_constant = n * (n*n + 1) // 2
    
    # Verify rows
    for r in range(n):
        if sum(square[r]) != magic_constant:
            return False, f"Row {r} sum is {sum(square[r])}, expected {magic_constant}"
            
    # Verify columns
    for c in range(n):
        col_sum = sum(square[r][c] for r in range(n))
        if col_sum != magic_constant:
             return False, f"Col {c} sum is {col_sum}, expected {magic_constant}"
             
    # Verify diagonals
    diag1 = sum(square[i][i] for i in range(n))
    if diag1 != magic_constant:
        return False, f"Main diagonal sum is {diag1}, expected {magic_constant}"
        
    diag2 = sum(square[i][n-1-i] for i in range(n))
    if diag2 != magic_constant:
        return False, f"Anti diagonal sum is {diag2}, expected {magic_constant}"

    # Verify all numbers are unique and from 1 to n*n
    flattened = [num for row in square for num in row]
    if sorted(flattened) != list(range(1, n*n + 1)):
        return False, "Not all numbers from 1 to n*n are present"
        
    return True, "Valid Magic Square"

if __name__ == "__main__":
    orders = [3, 4, 6]
    for n in orders:
        ms = generate_magic_square(n)
        print_magic_square(ms)
        is_valid, msg = verify_magic_square(ms)
        print(f"Verification: {msg}\n")
