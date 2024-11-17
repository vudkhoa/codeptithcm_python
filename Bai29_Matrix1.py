def ChuyenVi(a, n, m): 
    aT = []

    for i in range(m): 
        row = list()
        for j in range(n): 
            row.append(int(a[j][i]))
        aT.append(row)
    return aT

def caculation(a, aT, n, m): 
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            tong = 0 
            for k in range(m): 
                tong = tong + a[i][k] * aT[k][j]
            row.append(tong)
        result.append(row)
    return result

def pr(a): 
    for row in a: 
        for value in row: 
            print(value, end = " ")
        print()

def main(): 
    test = int(input())
    result = []
    for _ in range(test):
        a = []
        n, m = map(int, input().split())
        for i in range(n): 
            row = list(map(int, input().split()))
            a.append(row)        
        aT = ChuyenVi(a, n, m)
        result.append(caculation(a, aT, n, m))
    for matrix in result: 
        pr(matrix)

if __name__ == "__main__":
    main()