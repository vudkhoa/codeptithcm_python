def caculation(sNumber):
    tong = int(0)
    tich = int(1)
    check_tich = False
    for index in range(len(sNumber)): 
        if index % 2 == 0:
            tong += int(sNumber[index])
        if index % 2 == 1:
            if sNumber[index] != "0": 
                check_tich = True
                tich *= int(sNumber[index])
    if check_tich == True:
        print(tong, tich)
    else: 
        print(tong, 0)    

def main(): 
    test = int(input())
    for _ in range(test): 
        sNumber = input()
        caculation(sNumber)


if __name__ == "__main__":
    main()