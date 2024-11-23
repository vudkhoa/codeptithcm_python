a = []
a.append(int(100))
a.append(int(500))
a.append(int(200))

class KhachHang:
    def __init__(self, id, hoTen, s):
        self.id = f'KH{str(id).zfill(2)}'
        self.hoTen = hoTen
        self.loai = s[0]
        self.soDau = int(s[1])
        self.soCuoi = int(s[2])
        self.total = 0
        self.trongDinhMuc = 0
        self.vuotDinhMuc = 0
        self.VAT = 0
        self.chuanHoa()
        self.caculation()
    
    def chuanHoa(self): 
        lsHoTen = list(map(str.capitalize, self.hoTen.split()))
        self.hoTen = ""
        for index in range(len(lsHoTen) - 1):
            self.hoTen = self.hoTen + lsHoTen[index] + ' '
        self.hoTen += lsHoTen[len(lsHoTen) - 1]
    
    def caculation(self): 
        self.total = self.soCuoi - self.soDau
        dinhMuc = a[ord(self.loai) - 65]
        if self.total <= dinhMuc: 
            self.trongDinhMuc = self.total * 450
        else: 
            self.trongDinhMuc = dinhMuc * 450
            self.vuotDinhMuc = (self.total - dinhMuc) * 1000
            self.VAT = self.vuotDinhMuc * 0.05
        self.total = 0
        self.total = self.trongDinhMuc + self.vuotDinhMuc + self.VAT

        
        

    def __str__(self) -> str:
        return self.id + ' ' + self.hoTen + ' ' + str(self.trongDinhMuc) + ' ' + str(self.vuotDinhMuc) + ' ' + str(f'{self.VAT:.0f}') + ' ' + str(f'{self.total:.0f}')



def main(): 
    customer = [] 
    for index in range(int(input())): 
        customer.append(KhachHang(index + 1, input(), input().split()))
        
    for cus in sorted(customer, key=lambda x: -x.total):
        print(cus)

if __name__ == "__main__":
    main()