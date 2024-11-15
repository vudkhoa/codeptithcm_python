def sum(sNumber): 
    sum = 0
    for value in sNumber: 
        sum = sum + int(value)
    return str(sum)
def isThuanNghich(sNumber): 
    if len(sNumber) <= 1:
        return "NO"
    sNumber_reversed = sNumber[::-1]
    if sNumber != sNumber_reversed: 
        return "NO"
    return "YES"

def main(): 
    t = int(input())
    for _ in range(t): 
        sNumber = input()
        print(isThuanNghich(sum(sNumber)))

if __name__ == "__main__":
    main()