

def compress(s):
    
    
    prev = s[0]
    res = prev
    for i in range(1,len(s)):
        if s[i] != prev:
            res+=s[i]
            prev=s[i]
        
    return res
    

def solve(s):
    
    seen = set()
    res = 1 # of trying not to change
    
    middle = s[1:-1]
    for i in range(1,len(s)-1):
        
        compressed = compress(middle[1:i]+str(1-int(middle[i]))+middle[i+1:])
        if compressed not in seen:
            res+=1
            seen.add(compressed)
            
    return res


def main():
    t = int(input())
    
    for i in range(0,t):
        solve(input())
        
        
if __name__ == "__main__":
    main()