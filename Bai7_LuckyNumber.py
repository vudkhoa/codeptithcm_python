def isSoMayMan(sNumber): 
    count = 0
    for cha in sNumber: 
        if cha == '4' or cha == '7':
            count += 1
    return count == 4 or count == 7

def main(): 
    sNumber = input()
    if isSoMayMan(sNumber): 
        print("YES")
    else: 
        print("NO")

if __name__ == "__main__": 
    main()