import numpy as np

def TakeList():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    
    
    print("Enter the entries in a single line (separated by space): ")
    
    # User input of entries in a 
    # single line separated by space
    entries = list(map(int, input().split()))
    
    # For printing the matrix
    matrix = np.array(entries).reshape(R, C)
    return(matrix)

print("1. Multiply a matrix with constant ")
print("2. Add two matrices")
print("2. Subtract two matrices")
print("4. Multiply matrices")
print("5. Raise the matrix to constant power")
print("6. Find the transpose oe a matrix")
print("7. Find the square root of a matrix")
print("8. Compute the matrix determinant")
print("9. Compute the eigenvalues and eigenvectors of a square matrix")
print("10. Compute the inverse of a square matrix")
print("11. solve the system Ax=b whre A is a square matrix")
a=int(input("What do want to do?"))

match a:
    case 1:
        print("Enter the matrix")
        matrix=TakeList()
        x=int(input("Enter the constant:"))
        print("The result is:")
        print(matrix*x)

    case 2:
        print("Enter the first matrix")
        x=TakeList()
        print("Enter the second matrix")
        y=TakeList()
        print("The result is:")
        print(x+y)

    case 3:
        print("Enter the first matrix")
        x=TakeList()
        print("Enter the second matrix")
        y=TakeList()
        print("The result is:")
        print(x-y)

    case 4:
        print("Enter the first matrix")
        x=TakeList()
        print("Enter the second matrix")
        y=TakeList()
        print("The result is:")
        z=x.dot(y)
        print(z)

    case 5:
        print("Enter the matrix first")
        matrix=TakeList()
        x=int(input("Enter the constant:"))
        print("The result is:")
        print(matrix**x)

    case 6:
        print("Enter the matrix")
        x=TakeList()
        print("The matrix before transposing")
        print(x)
        print("The matrix after transposing")
        print(x.T)

    case 7:
        print("Enter the matrix")
        x=TakeList()
        print(np.sqrt(x))

    case 8:
        print("Enter the matrix")
        x=TakeList()
        print(np.linalg.det(x))

    case 9:
        print("Enter the matrix")
        x=TakeList()
        print(np.linalg.eig(x))

    case 10:
        print("Enter the matrix")
        x=TakeList()
        print(np.linalg.inv(x))

    case 11:
        print("Enter A matrix")
        a=TakeList()
        print("Enter b matrix")
        b=TakeList()
        print("The result is:")
        print(np.linalg.solve(a, b))

    case default:
            print ("Invalid choise!!")    












