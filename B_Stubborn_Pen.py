
import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    word = input().strip() 
    # 0 for red and 1 for blue
    pen = "R"
    manual_switches = 0
    for i in range(0,n):
        if pen != word[i]:
            pen = "R" if pen == "B" else "B"
            manual_switches +=1
        
        pen = "R" if pen == "B" else "B"
            
    print(manual_switches)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
