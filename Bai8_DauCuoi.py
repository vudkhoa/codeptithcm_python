def isDauCuoi(sNumber): 
    s1 = sNumber[:2]
    s2 = sNumber[-2:]
    return s1 == s2

def main(): 
    t = int(input())
    for test in range(t): 
        sNumber = input()
        if isDauCuoi(sNumber): 
            print("YES")
        else: 
            print("NO")

if __name__ == "__main__": 
    main()