import numpy as np

def input_matrix(rows, cols):
    """Function to input a matrix from the user."""
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, name):
    """Function to display a matrix."""
    print(f"\n{name} Matrix:")
    print(matrix)

def matrix_operations():
    """Main function to perform matrix operations."""
    print("Welcome to the Matrix Operations Tool!")
    
    # Input dimensions of the first matrix
    rows1 = int(input("Enter the number of rows for Matrix 1: "))
    cols1 = int(input("Enter the number of columns for Matrix 1: "))
    matrix1 = input_matrix(rows1, cols1)
    display_matrix(matrix1, "Matrix 1")
    
    # Input dimensions of the second matrix (if needed)
    rows2, cols2 = rows1, cols1
    if input("Do you want to input a second matrix? (yes/no): ").lower() == "yes":
        rows2 = int(input("Enter the number of rows for Matrix 2: "))
        cols2 = int(input("Enter the number of columns for Matrix 2: "))
        matrix2 = input_matrix(rows2, cols2)
        display_matrix(matrix2, "Matrix 2")
    else:
        matrix2 = None
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            if matrix2 is not None and matrix1.shape == matrix2.shape:
                result = matrix1 + matrix2
                display_matrix(result, "Addition Result")
            else:
                print("Error: Matrices must have the same dimensions for addition.")
        
        elif choice == "2":
            if matrix2 is not None and matrix1.shape == matrix2.shape:
                result = matrix1 - matrix2
                display_matrix(result, "Subtraction Result")
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")
        
        elif choice == "3":
            if matrix2 is not None and cols1 == rows2:
                result = np.dot(matrix1, matrix2)
                display_matrix(result, "Multiplication Result")
            else:
                print("Error: Number of columns in Matrix 1 must equal number of rows in Matrix 2 for multiplication.")
        
        elif choice == "4":
            print("\nChoose a matrix to transpose:")
            print("1. Matrix 1")
            print("2. Matrix 2")
            transpose_choice = input("Enter your choice (1-2): ")
            if transpose_choice == "1":
                result = np.transpose(matrix1)
                display_matrix(result, "Transpose of Matrix 1")
            elif transpose_choice == "2" and matrix2 is not None:
                result = np.transpose(matrix2)
                display_matrix(result, "Transpose of Matrix 2")
            else:
                print("Invalid choice or Matrix 2 not available.")
        
        elif choice == "5":
            print("\nChoose a matrix to calculate the determinant:")
            print("1. Matrix 1")
            print("2. Matrix 2")
            det_choice = input("Enter your choice (1-2): ")
            if det_choice == "1":
                if matrix1.shape[0] == matrix1.shape[1]:
                    result = np.linalg.det(matrix1)
                    print(f"Determinant of Matrix 1: {result}")
                else:
                    print("Error: Matrix must be square to calculate the determinant.")
            elif det_choice == "2" and matrix2 is not None:
                if matrix2.shape[0] == matrix2.shape[1]:
                    result = np.linalg.det(matrix2)
                    print(f"Determinant of Matrix 2: {result}")
                else:
                    print("Error: Matrix must be square to calculate the determinant.")
            else:
                print("Invalid choice or Matrix 2 not available.")
        
        elif choice == "6":
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    matrix_operations()