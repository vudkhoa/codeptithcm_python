def LamTron(sNumber): 
    num_list = list(sNumber)
    i = len(num_list) - 1

    while i > 0: 
        if (num_list[i] >= '5'): 
            num_list[i] = 0
            num_list[i - 1] = str(int(num_list[i - 1]) + 1)
        else: 
            num_list[i] = 0
        i -= 1
        
    for character in num_list: 
        print(character, end = "")
    print()

def main() : 
    t = int(input())
    for test in range(t): 
        LamTron(input())

if __name__ == "__main__": 
    main()