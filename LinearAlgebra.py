import numpy as np


def takelist():
    r = int(input("Enter the number of rows:"))
    c = int(input("Enter the number of columns:"))

    print("Enter the entries in a single line (separated by space): ")

    # User input of entries in a 
    # single line separated by space
    entries = list(map(int, input().split()))

    # For printing the matrix
    return np.array(entries).reshape(r, c)


print("1. Multiply a matrix with constant\n"
      " 2. Add two matrices\n"
      "3. Subtract two matrices\n"
      "4. Multiply matrices\n"
      "5. Raise the matrix to constant power\n"
      "6. Find the transpose oe a matrix\n"
      "7. Find the square root of a matrix\n"
      "8. Compute the matrix determinant\n"
      "9. Compute the eigenvalues and eigenvectors of a square matrix\n"
      "10. Compute the inverse of a square matrix\n"
      "11. solve the system Ax=b where A is a square matrix\n")
a = int(input("What do want to do?"))

match a:
    case 1:
        print("Enter the matrix")
        matrix = takelist()
        x = int(input("Enter the constant:"))
        print("The result is:")
        print(matrix * x)

    case 2:
        print("Enter the first matrix")
        x = takelist()
        print("Enter the second matrix")
        y = takelist()
        print("The result is:")
        print(x + y)

    case 3:
        print("Enter the first matrix")
        x = takelist()
        print("Enter the second matrix")
        y = takelist()
        print("The result is:")
        print(x - y)

    case 4:
        print("Enter the first matrix")
        x = takelist()
        print("Enter the second matrix")
        y = takelist()
        print("The result is:")
        z = x.dot(y)
        print(z)

    case 5:
        print("Enter the matrix first")
        matrix = takelist()
        x = int(input("Enter the constant:"))
        print("The result is:")
        print(matrix ** x)

    case 6:
        print("Enter the matrix")
        x = takelist()
        print("The matrix before transposing")
        print(x)
        print("The matrix after transposing")
        print(x.T)

    case 7:
        print("Enter the matrix")
        x = takelist()
        print(np.sqrt(x))

    case 8:
        print("Enter the matrix")
        x = takelist()
        print(np.linalg.det(x))

    case 9:
        print("Enter the matrix")
        x = takelist()
        print(np.linalg.eig(x))

    case 10:
        print("Enter the matrix")
        x = takelist()
        print(np.linalg.inv(x))

    case 11:
        print("Enter A matrix")
        a = takelist()
        print("Enter b matrix")
        b = takelist()
        print("The result is:")
        print(np.linalg.solve(a, b))

    case default:
        print("Invalid choise!!")
