import numpy as np

def generate_matrix():
    """Generate a random 2x2 matrix with elements between 1 and 9."""
    return np.random.randint(1, 10, size=(2, 2))

def get_user_matrix():
    """Prompt the user to input a 2x2 matrix."""
    matrix = []
    print("Enter the elements of the 2x2 matrix row by row, separated by spaces:")
    for i in range(2):
        row = input(f"Row {i+1}: ").split()
        if len(row) != 2:
            print("Error: Please enter exactly two numbers per row.")
            return get_user_matrix()
        matrix.append([int(num) for num in row])
    return np.array(matrix)

def play_game():
    """Main game loop."""
    print("Welcome to the Matrix Addition Game!")
    
    # Generate two random 2x2 matrices
    matrix1 = np.array([[2],[3]])
    matrix2 = generate_matrix()
    
    # Calculate the correct sum
    correct_sum = matrix1 + matrix2
    
    print("Matrix 1:")
    print(matrix1)
    
    print("Matrix 2:")
    print(matrix2)
    
    # Get the user's answer
    user_sum = get_user_matrix()
    
    # Check if the user's answer is correct
    if np.array_equal(user_sum, correct_sum):
        print("Congratulations! You got it right!")
    else:
        print("Oops! That's not correct.")
        print("The correct sum is:")
        print(correct_sum)


play_game()
