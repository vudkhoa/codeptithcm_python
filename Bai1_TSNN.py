def find_min(s):
    i = 0
    sum = int(0)
    min = None
    while i < len(s): 
        sum = 0
        while i < len(s) and '0' <= s[i] <= '9': 
            sum = sum * 10 + int(s[i])
            i += 1
        if min == None and sum != 0: 
            min = sum
        elif min != None and sum != 0 and sum < min: 
            min = sum
        i += 1
    return min

def main() : 
    n = int(input())
    for test in range(n) : 
        s = input() 
        print(find_min(s))



if __name__ == "__main__": 
    main()