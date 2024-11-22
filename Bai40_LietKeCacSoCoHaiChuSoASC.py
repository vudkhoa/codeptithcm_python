def main(): 
    s = input()
    a = set()
    i = 0
    while i + 1 < len(s) - 1: 
        x = int(s[i]) * 10 + int(s[i + 1])
        a.add(x)
        i += 2
    
    aS = sorted(a)
    print(' '.join(map(str, aS)))
    

if __name__ == "__main__":
    main()