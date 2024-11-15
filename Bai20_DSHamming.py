def siveHamming(n): 
    lsHamming = [] 
    i2 = i3 = i5 = 0
    lsHamming.append(1)
    tmp = 1
    while tmp < n: 
        tmp2 = lsHamming[i2] * 2
        tmp3 = lsHamming[i3] * 3
        tmp5 = lsHamming[i5] * 5
        tmp = min(tmp2, tmp3, tmp5)
        lsHamming.append(tmp)
        
        if tmp == tmp2:
            i2 += 1
        if tmp == tmp3:
            i3 += 1
        if tmp == tmp5: 
            i5 += 1
    return lsHamming

def binary_search(number, lsHamming): 
    l = 0 
    r = len(lsHamming) - 1
    while l <= r:
        mid = (l + r) // 2  
        if number == lsHamming[mid]:
            return mid  
        elif number < lsHamming[mid]:
            r = mid - 1 
        else: 
            l = mid + 1  
    return -1  

def main(): 
    lsHamming = siveHamming(1000000000000000000)
    test = int(input())
    for _ in range(test): 
        number = int(input())
        index = binary_search(number, lsHamming)
        if index != -1:
            print(index + 1)
        else:
            print("Not in sequence")
if __name__ == "__main__":
    main()

# 1 2 3 4 5 6 8 9 10
# 1
# 2 -> i2 = 1, i3 = 0, i5 = 0
# 3 -> i2 = 1, i3 = 1, i5 = 0
# 4 -> i2 = 2, i3 = 1, i5 = 0 
# 5 -> i2 = 2, i3 = 1, i5 = 1