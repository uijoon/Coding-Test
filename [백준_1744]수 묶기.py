import sys

def main():
    n = int(sys.stdin.readline())
    pos = []
    neg = []
    ans = 0

    for _ in range(n):
        num = int(sys.stdin.readline())
        if num == 1:
            ans += 1
        elif num > 0:
            pos.append(num)
        else :
            neg.append(num)

    pos.sort()
    neg.sort(reverse = True)

    if len(pos) % 2 == 1:
        pos.insert(0,1)
    if len(neg) % 2 == 1:
        neg.insert(0,1)

    while pos:
        n1 = pos.pop()
        n2 = pos.pop()
        ans += n1*n2
    while neg:
        n1 = neg.pop()
        n2 = neg.pop()
        ans += n1*n2
    print(ans)


    
main()