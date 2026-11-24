def solve(point):
    [a , b] = point
    res = 0
    if (abs(b) > a + 1):
        print(-1)
    else:
        if ( (a%2==0) and (b%2==0) ) or ( (a%2!=0) and (b%2!=0) ) :
            print(a) 
        else:
            print(a + 1)
    
    
    
        


def main():
    t = int(input())

    for _ in range(t):
        solve([int(num) for num in input().strip().split(" ")])


if __name__ == "__main__":
    main()
