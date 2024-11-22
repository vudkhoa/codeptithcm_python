def main(): 
    file = open('DATA.in', 'r')
    a = [] 
    for line in file:
        for j in line.split():
            try: 
                x = int(j)
                if x > (1<<63): a.append(j)
            except: 
                a.append(j)
    print(' '.join(sorted(a)))

if __name__ == "__main__":
    main()