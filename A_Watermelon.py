import sys

input = sys.stdin.readline

def solve(w):
    
    if w > 2 and (w%2 == 0):
        print("YES")
    else:
        print("NO")
    


def main():
    t = int(input())

    #for _ in range(t):
        #w = int(input())
    solve(t)


if __name__ == "__main__":
    main()