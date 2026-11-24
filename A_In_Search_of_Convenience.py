import math

def solve(x,y,R):
    
    x_res = 0
    while x_res < x - R:
        
        #adjust x_res
        break
        
    #print(x_res+" "+y-math.sqrt(pow(R,2) - pow( (x-x_res) ,2)))

def main():
    
    t = int(input())
    
    for i in range(0,t):
        [x,y,R] = [int(num) for num in input().split(" ")]
        solve(x,y,R)
        
        
if __name__ == "__main__":
    main()