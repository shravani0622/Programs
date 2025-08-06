#How manny numbers are smaller than current number
def acc_data(A):
    size=int(input("Enter the size of list: "))
    for i in range(size):
        a=int(input("Enter the values: "))
        A.append(a)
    print(A)

def check(A,K): 
    found=[] 
    for i in range(len(A)): 
        if A[i]<K: 
            found.append(A[i]) 
    print(len(found)) 
    
def main():
    list=[]
    acc_data(list)
    key=int(input("Enter the current value to be compare: "))
    check(list,key)
main()



