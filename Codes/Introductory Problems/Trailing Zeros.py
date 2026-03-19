import sys
input = sys.stdin.readline

n = int(input())
i = 5

cnt = 0
while i <= n:
    cnt += n // i
    i *= 5
print(cnt)