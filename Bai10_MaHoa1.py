def MaHoa(s): 
    i = 0
    while i <= len(s) - 1:
        count = 1
        while (i + 1 <= len(s) - 1 and s[i + 1] == s[i]): 
            count += 1
            i += 1
        print(count, end = "")
        print(s[i], end = "")
        i += 1
    print()

def main(): 
    t = int(input())
    for test in range(t): 
        MaHoa(input())

if __name__ == "__main__":
    main()