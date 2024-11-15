def GiaiMa(s):
    char = ""
    for value in s: 
        if value >= '2' and value <= '9':
            i = int(value)
            for i in range(i - 1): 
                print(char, end ="")
        elif value != '1':
            print(value, end = "")
            char = value 
    print()

def main(): 
    t = int(input())
    for test in range(t): 
        GiaiMa(input())

if __name__ == "__main__": 
    main()