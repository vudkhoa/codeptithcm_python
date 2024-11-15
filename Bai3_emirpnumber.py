from math import sqrt

def isPrime(number):
    if number < 2:
        return False
    for index in range(2, int(sqrt(number)) + 1):
        if number % index == 0:
            return False
    return True

def rev(number): 
    # Đảo ngược số bằng cách chuyển thành chuỗi, đảo chuỗi, rồi chuyển lại thành số nguyên
    numberTmp = str(number)
    return int(numberTmp[::-1])

def isEmirp(number, rev_number):
    # Kiểm tra nếu số là số nguyên tố và số đảo ngược của nó cũng là số nguyên tố, và hai số khác nhau
    return isPrime(number) and isPrime(rev_number) and (number != rev_number)

def main():
    n = int(input())

    for test in range(n): 
        length = int(input())
        list = []
        for number in range(2, length):
            rev_number = rev(number)
            if isEmirp(number, rev_number) and (rev_number > number) and (rev_number < length):
                list.append(str(number))
                list.append(str(rev_number))
        print(" ".join(list))

if __name__ == "__main__":
    main()
