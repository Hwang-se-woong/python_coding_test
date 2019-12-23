my_list = set()
my_list2 = set()

N, M = map(int, input().split())

for i in range(N):
    my_list.add(input())

for i in range(M):
    my_list2.add(input())
answer = list(my_list & my_list2)
answer.sort()
print(len(answer))

for e in sorted(answer):
    print(e)
