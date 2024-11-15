def isPythonFile(s): 
    if s[-3:] != ".py" and s[-3:] != ".PY" and s[-3:] != ".Py" and s[-3:] != ".pY":
        return "no"
    fileName = s[:-3]
    for index in range(len(fileName) - 3): 
        if (fileName[index] < 'a' or fileName[index] > 'z') and (fileName[index] < 'A' or fileName[index] > 'Z') and fileName[index] != '_':
            return "no"
    return 'yes' 

def main(): 
    s = input()    
    print(isPythonFile(s))

if __name__ == "__main__":
    main()