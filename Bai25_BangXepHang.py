def main(): 
    test = int(input())
    ls = []
    for _ in range(test): 
        name = input()
        slBai, slSub = map(int, input().split())
        ls.append((name, slBai, slSub))
    ls.sort(key = lambda x: (-x[1], x[2], x[0]))
    for infor in ls: 
        print(' '.join(map(str, infor)), end = "\n")

if __name__ == "__main__": 
    main()  