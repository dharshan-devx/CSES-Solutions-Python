import sys
input = sys.stdin.readline

for _ in range(int(input())):
    y,x = map(int,input().split())
    
    layer = max(y,x)
    square = layer * layer
    
    if layer % 2 == 0:
        if y == layer:
            ans = square - (x-1)
        else:
            ans = (layer - 1) * (layer - 1) + y 
    else:
        if x == layer:
            ans = square - (y - 1)
        else:
            ans = (layer - 1) * (layer - 1) + x 
    print(ans)