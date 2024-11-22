def main(): 
    for _ in range(int(input())):
        s = input()
        dem = 0 
        note = 0
        ls = []
        for char in s:
            if char == '(': 
                dem += 1 
                note = dem
                print(dem, end = " ")
                ls.append(dem)
            elif char == ')':
                print(ls.pop(), end = " ")
        print()

if __name__ == "__main__":
    main()