#Sum oF two number
def list(A):
    size=int(input("Enter the size of list: "))
    for i in range(size):
        ls=int(input("Enter the value of list: "))
        A.append(ls)
    print("List is ",A)

def add(A,Sum):
    for i in range(A[0],len(A)):
        for j in range(i+1,len(A)):
            if i+j==Sum:
                print(f"Addition of {i} and {j} is {Sum}")
            

def main():
    a=[]
    list(a)
    sum=int(input("Enter the expect sum of number"))
    add(a,sum)
main()