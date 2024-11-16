def sum(sNumber): 
    sum = int(0)
    for value in sNumber: 
        sum += int(value)
    return sum


def main():
    test = int(input()) 
    for _ in range(test):
        n = int(input())
        ls = [] 
        ls = list(map(str, input().split()))

        new_ls = [(sum(map(int, value)), int(value)) for value in ls]
        
        new_ls.sort(key=lambda x: (x[0], x[1]))
        for tong, value in new_ls: 
            print(value, end = ' ')
        print()


if __name__ == "__main__":
    main()