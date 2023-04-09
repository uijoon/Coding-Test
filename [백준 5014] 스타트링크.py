import sys
from queue import Queue

def main():
    F,S,G,U,D = map(int,sys.stdin.readline().split())

    check = [0 for _ in range(F + 1)]

    q = Queue()

    q.put((S,0))

    check[S] = 1

    while not q.empty():
        cur, but = q.get()

        if cur == G:
            print(but)
            return

        for nex in (cur+U,cur-D):
            n_but = but + 1

            if 0<nex<=F and check[nex] == 0:
                check[nex] = 1
                q.put((nex,n_but))
    print("use the stairs")

    return 0


main()