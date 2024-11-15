def find_max(s):
    i = 0
    sum = int(0)
    max = None
    while i < len(s): 
        sum = 0
        while i < len(s) and '0' <= s[i] <= '9': 
            sum = sum * 10 + int(s[i])
            i += 1
        if max == None and sum != 0: 
            max = sum
        elif max != None and sum != 0 and sum > max: 
            max = sum
        i += 1
    return max

def main() : 
    n = int(input())
    for test in range(n) : 
        s = input() 
        print(find_max(s))



if __name__ == "__main__": 
    main()