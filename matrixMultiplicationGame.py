import numpy as np

def generate_2x3matrix():
    """Generate a random 2x2 matrix with elements between 1 and 9."""
    return np.random.randint(-2, 5, size=(2, 3))

def generate_3x2matrix():
    """Generate a random 2x2 matrix with elements between 1 and 9."""
    return np.random.randint(-2, 5, size=(3, 2))

def get_user_matrix(product_rows,product_columns):
    """Prompt the user to input a 2x2 matrix."""
    matrix = []
    print(f"Enter the elements of the {product_rows}x{product_columns} matrix row by row, separated by spaces:")
    for i in range(product_rows):
        row = input(f"Row {i+1}: ").split()
        if len(row) != product_columns:
            print("Error: Please enter exactly two numbers per row.")
            return get_user_matrix(product_rows,product_columns)
        matrix.append([int(num) for num in row])
    return np.array(matrix)

def play_game():
    """Main game loop."""
    print("Welcome to the Matrix Addition Game!")
    
    # Generate two random 2x2 matrices
    matrix1 = generate_2x3matrix()
    matrix2 = generate_3x2matrix()
    
    # Calculate the correct sum
    correct_product = matrix1 @ matrix2
    
    print("Matrix 1:")
    print(matrix1)
    
    print("Matrix 2:")
    print(matrix2)
    
    product_rows  = correct_product.shape[0]
    product_columns  = correct_product.shape[1]
    
    # Get the user's answer
    user_product = get_user_matrix(product_rows,product_columns)
    
    # Check if the user's answer is correct
    if np.array_equal(user_product, correct_product):
        print("Congratulations! You got it right!")
    else:
        print("Oops! That's not correct.")
        print("The correct sum is:")
        print(correct_product)


play_game()
