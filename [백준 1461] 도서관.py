import sys

def book_pop(book,m):
    global answer
    while book:
        loc = book[-1]
        answer += loc*2
        for _ in range(m):
            try:
                book.pop()
            except:
                return


def main():

    n,m = map(int,sys.stdin.readline().split())
    it = map(int,sys.stdin.readline().split())

    pos = []
    neg = []
    max_num = 0

    global answer
    answer = 0

    for num in it:
        max_num = max(max_num,abs(num))
        if num > 0:
            pos.append(num)
        else :
            neg.append(-num)

    pos.sort()
    neg.sort()

    book_pop(pos,m)
    book_pop(neg,m)

    print(answer - max_num)


   
main()