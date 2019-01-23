# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())


def even_odd(S):
    for i in range(0, len(S)):
        if i%2==0:
            print(S[i], end="") 
    print(" ", end="")
    for i in range(0, len(S)):        
        if i%2!=0:
            print(S[i], end="")
    print("")        

for i in range(n):
    S=input()
    even_odd(S)

