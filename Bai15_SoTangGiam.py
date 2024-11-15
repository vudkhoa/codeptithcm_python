def isTangGiam(s):
    if len(s) < 3: 
        return "NO"
    i = 0
    # 0 -> tang, 1 -> Giam
    TH = 0
    while i < len(s) - 1: 
        if TH == 0: 
            if (s[i] > s[i + 1]): 
                TH = 1
            elif (s[i] == s[i + 1]):
                return "NO"
        else: 
            if (s[i] <= s[i + 1]):
                return "NO"
        i += 1
    return "YES"

def main(): 
    t = int(input())
    for _ in range(t): 
        s = input()
        print(isTangGiam(s))

if __name__ == "__main__":
    main()