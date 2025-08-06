#program of factorial
def factorialnum(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorialnum(n-1)

def main():
    n = int(input("Enter a number to find its factorial: "))
    result = factorialnum(n)
    print(f"The factorial of {n} is {result}")
main()