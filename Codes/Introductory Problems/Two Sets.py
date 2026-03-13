import sys
input = sys.stdin.readline

n = int(input())

s = n * (n + 1) // 2

if s % 2:
    print("NO")
else:
    print("YES")

    target = s // 2
    set1 = []
    set2 = []

    for i in range(n,0,-1):
        if i <= target:
            set1.append(i)
            target -= i
        else:
            set2.append(i)

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)