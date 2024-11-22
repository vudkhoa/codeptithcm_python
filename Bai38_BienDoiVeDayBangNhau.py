def qhd(a, n): 
    result = [(int(0), int(-1))] * n
    resulti = [(int(0), int(-1))] * n
    resultj = [(int(0), int(-1))] * n
    aS = sorted(a, key = lambda x: x[0])
    i = 0
    j = n - 1 
    fmin = (10000 * 200 + 1, -1)
    while i < n: 
        if i == 0: 
            resulti[i] = (0, aS[i][1])
        else: 
            x = aS[i][0] - aS[i - 1][0]
            resulti[i] = (resulti[i - 1][0] + x * i, aS[i][1])
    
        if j == n - 1:
            resultj[j] = (0, aS[j][1])
        else: 
            x = aS[j + 1][0] - aS[j][0]
            resultj[j] = (resultj[j + 1][0] + x * i, aS[j][1])    
        

        if j <= i:
            result[i] = (resulti[i][0] + resultj[i][0],resulti[i][1])

            result[j] = (resulti[j][0] + resultj[j][0], resulti[j][1])

            if fmin[0] > result[j][0] or (fmin[0] == result[j][0] and fmin[1] > result[j][1]) :
                fmin = (result[j][0], result[j][1])
            
            if fmin[0] > result[i][0] or (fmin[0] == result[i][0] and fmin[1] > result[i][1]) :
                fmin = (result[i][0], result[i][1])   
          
        i += 1
        j -= 1
    return fmin
    

def main(): 
    n = int(input())
    data = input()
    a = [(int(value), int(index)) for index, value in enumerate(data.strip().split())]
    fmin = qhd(a, n)
    print(fmin[0], a[fmin[1]][0])

if __name__ == "__main__":
    main()