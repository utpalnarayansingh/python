if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b=set(arr)
    c=list(b)
    print(c)
    print(c[len(c)-2])