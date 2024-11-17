import math

def eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]

def sive(n, ls_prime):
    count = 0

    for p in ls_prime:
        if p ** 8 <= n:
            count += 1
    
    for i in range(len(ls_prime)):
        p1 = ls_prime[i] ** 2
        for j in range(i + 1, len(ls_prime)):
            p2 = ls_prime[j] ** 2
            p = p1 * p2
            if p <= n:
                count += 1
            else:
                break  
    return count

def main():
    n = int(input())
    ls_prime = eratosthenes(int(math.sqrt(n)) + 1)
    print(sive(n, ls_prime))

if __name__ == "__main__":
    main()
