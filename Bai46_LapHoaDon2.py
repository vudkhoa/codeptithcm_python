from datetime import datetime
price = {'1': 25, '2': 34, '3': 50, '4': 80}

class KhachHang: 
    def __init__(self, id, name, room, d1, d2, plus) -> None: 
        self.id = f'KH{str(id).zfill(2)}'
        self.name = name
        self.room = room
        self.days = (datetime.strptime(d2, "%d/%m/%Y") -
                    datetime.strptime(d1, "%d/%m/%Y")).days + 1
        self.plus = plus
        self.sum = self.days * price[self.room[0]] + self.plus
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + self.room + ' ' + str(self.days) + ' ' + str(self.sum) 

def main(): 
    a = [] 
    for i in range(int(input())): 
        a.append(KhachHang(i + 1, input(), input(), input().strip(), input().strip(), int(input())))
    for infor in sorted(a, key = lambda x: -x.sum):
        print(infor)

if __name__ == "__main__":
    main()