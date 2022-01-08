n, m = map(int,input().split())
arr = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
print(len(list(set(arr).intersection(A)))-len(list(set(arr).intersection(B))))
# print(sum([(i in A) - (i in B) for i in arr]))

'''
n, m = map(int,input().split())
arr = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
happiness = 0
for i in arr:
    for j in A:
        if i==j:
            happiness += 1
    for j in B:
        if i==j:
            happiness -= 1
print(happiness)
'''