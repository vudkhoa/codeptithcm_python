def convert(sNumber): 
    result = 0
    for i in range(3 - (len(sNumber) % 3)):
        sNumber = "0" + sNumber
    i = 0
    while i < len(sNumber):
        result = result * 10 + (int(sNumber[i]) * 4 + int(sNumber[i+1]) * 2 + int(sNumber[i+2]))
        i += 3
    
    print(result)

def main(): 
    convert(input().strip())

if __name__ == "__main__":
    main()