M_size = int(input())
M = list(map(int, input().split()))
N_size = int(input())
N = list(map(int, input().split()))
for i in sorted(list(set(M).difference(set(N)).union(set(N).difference(set(M))))):print(i)