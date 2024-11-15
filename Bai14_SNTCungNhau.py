def isNTCN(n1, n2): 
    if (n1 > n2):
        n1, n2 = n2, n1
    while n1 != 0:
        n1, n2 = n2 % n1 ,n1
    return n2 == 1


def main(): 
    t = int(input())
    for _ in range(t):
        sNumber = input()
        num1 = int(sNumber)
        num2 = int(sNumber[::-1])
        if isNTCN(num1, num2): 
            print("YES")
        else: 
            print("NO")

if __name__ == "__main__":
    main()