def main(): 
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    s = input()
    while s != "0":
        parts = s.split(" ", 1) 
        
        k = int(parts[0])
        code = parts[1].strip()
        s = ""
        for character in code: 
            index = ((P.find(character) + 1) + k) % 28
            s = s + P[index - 1]
        print(''.join(reversed(s)))
        s = input()
    

if __name__ == "__main__":
    main()