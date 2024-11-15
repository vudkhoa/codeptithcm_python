def giaiThua(number): 
    result = int(1)
    for i in range(number): 
        result *= (i + 1)
    return result

def tachSo(number):
    sum = int(0)
    while number > 0: 
        sum += giaiThua(number % 10)
        number //= 10
    return sum

def main(): 
    t = int(input())
    for test in range(t): 
        number = int(input())
        if (number == tachSo(number)): 
            print("Yes", end = "\n")
        else : 
            print("No", end = "\n")

if __name__ == "__main__": 
    main()