import math

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def instance_to(self, other): 
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) 

def main(): 
    test = int(input())
    for _ in range(test):
        x, y, x1, y1 = map(float, input().split())

        p1 = Point(x, y)
        p2 = Point(x1, y1)

        print(f'{p1.instance_to(p2):.4f}')

if __name__ == "__main__":
    main()