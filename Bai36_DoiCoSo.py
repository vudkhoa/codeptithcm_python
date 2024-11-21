cha = []

def convert(a, b): 
    result = []
    while a != 0: 
        result.append(a % b)
        a //= b
    for value in reversed(result): 
        if value > 9: 
            print(cha[value - 10], end = "")
        else: 
            print(value, end = "")

def main(): 
    for i in range(ord('A'), ord('Z') + 1, 1): 
        cha.append(chr(i))
    for index in range(int(input())):
        a, b = map(int, input().split())
        convert(a, b)
        print()

if __name__ == "__main__":
    main()