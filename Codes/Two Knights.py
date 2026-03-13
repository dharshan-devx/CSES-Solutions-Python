import sys
input = sys.stdin.readline

n = int(input())

for k in range(1, n + 1):
    ttl = k * k * (k*k-1) // 2
    attack = 4 * (k-1) * (k-2)
    print(ttl - attack)