def isEven(sNumber):
    i = len(sNumber) - 1 
    return sNumber[i] == '0' or sNumber[i] == '2' or sNumber[i] == '4' or sNumber[i] == '6' or sNumber[i] == '8'
def main(): 
    sNumber = input()
    if (isEven(sNumber)): 
        print("CHAN", end = "")
    else: 
        print("LE", end = "")

if __name__ == "__main__": 
    main()