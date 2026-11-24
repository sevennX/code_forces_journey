


def solve(word):
    
    if len(word) < 10 :
        print(word)
    else:
        print(word[0]+str(len(word)-2)+word[-1])


def main():
    t = int(input())
    
    for i in range(t):
        solve(input())
    


if __name__ == "__main__" :
    main()