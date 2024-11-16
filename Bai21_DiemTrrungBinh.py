def main(): 
    n = int(input())
    ls = []
    ls = sorted(list(map(float, input().split())))
    min = ls[0]
    max = ls[n - 1]
    i = 0
    j = n - 1
    while min != -1 or max != -1:
        if ls[i] == min: 
            i += 1
        else:
            min = -1
        if ls[j] == max:
            j -= 1
        else: 
            max = -1

    diemTB = 0

    for index in range(i, j + 1): 
        diemTB += ls[index]
    print(f"{diemTB / (j - i + 1):.2f}")
if __name__ == "__main__":
    main()