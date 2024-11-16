import math

def main(): 
    test = int(input())
    for _ in range(test): 
        x, y, x1, y1 = map(float, input().split())
        distance =  math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        print(f"{distance:.4f}")

if __name__ == "__main__":
    main()