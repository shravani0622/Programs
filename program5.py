#program for fibonacii
def fibonacii(n):
    A=[0,1]
    for i in range(2,n):
        A.append(A[i-1]+A[i-2])
    print("Display the fibonacii series",A)
    return A
n=int(input("Enter the size of array: "))
fibonacii(n)
