def main(): 
    n, m = map(int, input().split())
    arr = []
    for i in range(n): 
        row = list(map(int, input().split()))
        for value in row: 
            arr.append(value)
    fmax = max(arr)
    fmin = min(arr)
    f = fmax - fmin
    check = False
    ans = []
    while f in arr: 
        i = arr.index(f)
        v1 = i // m
        v2 = i - m * v1
        ans.append(f'Vi tri [{v1}][{v2}]')
        check = True
        arr[i] = None

    if check == False: 
        print('NOT FOUND')
    else:
        print(f) 
        print('\n'.join(ans))

if __name__ == "__main__":
    main()