


def solve(slices):
    [a,b] = slices
    
    if a<=b:
        print(-1)
    else:
        print(min(b,a-b))
        


def main():
    t = int(input())
    
    for i in range(0,t):
        slices = [int(a) for a in input().split(" ")]
        solve(slices)
    

if __name__ == "__main__":
    main()