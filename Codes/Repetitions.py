import sys
input = sys.stdin.readline

s = input()
cur_cnt = 1
maxi = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        cur_cnt += 1
    else:
        cur_cnt = 1
    maxi = max(maxi, cur_cnt)
print(maxi)
        