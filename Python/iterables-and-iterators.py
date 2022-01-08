# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr = [i.lower() for i in input().split()]
arr = arr[:N+1]
print(arr)