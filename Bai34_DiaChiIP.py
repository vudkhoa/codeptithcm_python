def isIp(string): 
    ls = list(string.split('.'))
    if len(ls) != 4: 
        return False
    for value in ls: 
        num = int(value)
        if num < 0 or num > 255: 
            return False
    
    return True

def main(): 
    for index in range(int(input())): 
        try:
            string = input()
            if isIp(string):
                print("YES")
            else: 
                print("NO")
        except: 
            print("NO")

if __name__ == "__main__":
    main()