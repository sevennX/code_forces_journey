

def solve(n,commands):
    
    mem = []
    printed = set()
    for i in range(0,len(commands)):
        
        match commands[i]:
            case "1" : 
                mem.append(n[i])
            case "2" :
                if len(mem) > 0:
                    printed.add(mem.pop())
                else:
                    printed.add(i+1)
            case "3" :
                printed.add(i+1)
    k = len(n) - len(printed)
    
    print(k)
    if k > 0:
        print(" ".join(str(ele) for ele in n if not ele in printed))
    else:
        print("")


def main():
    t = int(input())
    
    for i in range(0,t):
        n = list(range(1,int(input())+1))
        commands = list(input())
        solve(n,commands)
        
        
if __name__ == "__main__":
    main()