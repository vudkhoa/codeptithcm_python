import math 

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def instance_to(self, other): 
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) 

    def is_collinear(self, p2, p3): 
        return (p2.y - self.y) * (p3.x - self.x) == (p3.y - self.y) * (p2.x - self.x)

class Triangle: 
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.c1 = self.p1.instance_to(self.p2)
        self.c2 = self.p1.instance_to(self.p3)
        self.c3 = self.p2.instance_to(self.p3)

    def perimeter(self):
        return self.c1 + self.c2 + self.c3
    
    def area(self): 
        return  1/4 * math.sqrt((self.c1 + self.c2 + self.c3) * (self.c1 - self.c2 + self.c3)
                * (self.c1 + self.c2 - self.c3) * (-self.c1 + self.c2 + self.c3))

def main(): 
    a = [] 
    t = int(input())
    for _ in range(t): 
        a += [float(i) for i in input().split()]
    for i in range(t): 
        p1 = Point(a[i * 6 + 0], a[i * 6 + 1])
        p2 = Point(a[i * 6 + 2], a[i * 6 + 3])
        p3 = Point(a[i * 6 + 4], a[i * 6 + 5])
        if p1.is_collinear(p2, p3): 
            print("INVALID")
        else: 
            tri = Triangle(p1, p2, p3)
            print(f'{tri.area():.2f}')
    

if __name__== "__main__": 
    main()