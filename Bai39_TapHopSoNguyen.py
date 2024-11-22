mang_danhdau = [""] * 1001

def main(): 
    n, m = map(int, input().split())
    a = sorted(set(map(int, input().split())))
    b = sorted(set(map(int, input().split())))
    intersect = []
    a_minus_b = []
    b_minus_a = []
    for number in a: 
        mang_danhdau[number] = "a"
        a_minus_b.append(number)

    for number in b: 
        mang_danhdau[number] = mang_danhdau[number] + "b"
        if mang_danhdau[number] == "ab": 
            intersect.append(number)
            a_minus_b.remove(number)
        else: 
            b_minus_a.append(number)
    
    print(' '.join(map(str, intersect)))
    print(' '.join(map(str, a_minus_b)))
    print(' '.join(map(str, b_minus_a)))
    
if __name__ == "__main__":
    main()