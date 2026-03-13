import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
exp_sum = n*(n+1) // 2
actual_sum = sum(arr)
print(exp_sum - actual_sum)