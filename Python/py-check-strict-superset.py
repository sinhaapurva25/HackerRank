# A = list(map(int,input().split()))
# N = int(input())
# N_arr = []
# [N_arr.append(list(map(int,input().split()))) for i in range(N)]
# output = 1
# for i in range(N):

#     if len(N_arr[i]) < len(A):
#         output *=0
#     else:
#         count = 0
#         for j in A:
#             if j in N_arr[i]:
#                 count += 1
#         if count >= len(A):
#             output *=1
#         else:
#             output *=0
# print(bool(output))

# ----------------------------------------------------------------

A = list(map(int,input().split()))
N = int(input())

N_arr = []

[N_arr.append(list(map(int,input().split()))) for i in range(N)]

output = 1
for i in range(N):
    count = 0

    if len(N_arr[i]) < len(A):
        output *=0

    for j in A:
        if j in N_arr[i]:
            count += 1
    if count == len(A):
        output *=1
    else:
        output *=0

print(bool(output))