


def solve(n,k):
    
    if k >= n:
        print(k*2)
    else:
        print(pow(2,(n-k+1))+(k-1)*2)

def main():
    
    t = int(input())
    
    for i in range(0,t):
        [n , k] = [int(ele) for ele in input().strip().split(" ")] 
        solve(n,k)
        
        
if __name__ == "__main__":
    
    main()