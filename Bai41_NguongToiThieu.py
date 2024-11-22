mang_danhdau = [0] * 90

def main(): 
    s = input()
    k = int(input())
    i = 0 
    a = set()
    while i + 1 <= len(s) - 1: 
        x = int(s[i]) * 10 + int(s[i + 1])
        a.add(x)
        mang_danhdau[x - 10] += 1
        i += 2
    result = [num for num in a if mang_danhdau[num - 10] >= k]
    if len(result) == 0: 
        print('NOT FOUND')
    else: 
        for i in sorted(result):
            print(i, mang_danhdau[i - 10])

if __name__ == "__main__":
    main()