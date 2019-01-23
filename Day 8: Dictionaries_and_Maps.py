# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phonebook = {}

for i in range(int(n)):
    k, phonebook[k] = input().split()
    
while n:
    name= input()
    print("{}={}".format(name, phonebook[name])) if name in phonebook else print("Not found")
    n-=1    
