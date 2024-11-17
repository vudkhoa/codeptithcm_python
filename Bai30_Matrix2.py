def Transpose(a, n, m): 
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
            row.append(str(tong))
        result.append(row)
    return result

def pr(a): 
    for row in a: 
        print(' '.join(row))

def main(): 
    test_case = int(input())
    data = []
    while True:
        try: data.extend(map(int, input().split()))
        except: break
    index = 0
    for t in range(test_case):
        n, m = data[index], data[index+1]
        index += 2
        a = []
        for i in range(n): a.append([0]*m)
        while len(data) - index < n*m: data.append(0)
        for i in range(n):
            for j in range(m): a[i][j] = data[index+j]
            index +=m
        aT = Transpose(a, n, m)
        result_matrix = caculation(a, aT, n, m)
        pr(result_matrix)

if __name__ == "__main__":
    main()