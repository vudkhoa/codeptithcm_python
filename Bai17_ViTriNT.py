def eratosthenes():
    prime = [True] * 501 
    prime[0] = prime[1] = False
    for i in range(2, 501):
        if prime[i]: 
            for j in range(i * i, 501, i):
                prime[j] = False
    return prime

def check(sNumber, prime):
    for index in range(len(sNumber)):
        if prime[int(sNumber[index])] == True and prime[index] == False:
            return "NO"
    return "YES" 

def main(): 
    prime = eratosthenes()
    test = int(input())
    for _ in range(test): 
        sNumber = input()
        print(check(sNumber, prime))

if __name__ == "__main__":
    main()