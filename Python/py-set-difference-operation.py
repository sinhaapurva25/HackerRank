n = int(input())
English = set(list(map(int,input().split())))
f = int(input())
French = set(list(map(int,input().split())))
print(len(English.difference(French)))