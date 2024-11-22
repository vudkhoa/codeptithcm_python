def main():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    count = [0] * len(a)
    for i in range(1, len(a)): 
        if a[i] - a[i - 1] <= k: 
            count[i] = count[i - 1]
        else: 
            count[i] = count[i - 1] + 1
    print(count[len(a) - 1] + 1)

if __name__ == "__main__":
    main()