def main(): 
    number = int(input())
    format_number = "{:,}".format(number)
    print(format_number)

if __name__ == "__main__":
    main()