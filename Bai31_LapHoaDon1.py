class Customer:
    def __init__(self, id, name, value1, value2):
        self.id = "KH" 
        if id < 10: 
            self.id += "0"
        self.id += str(id)
        self.name = name
        self.value1 = value1
        self.value2 = value2
        self.cost = 0

    def set_cost(self): 
        x = self.value2 - self.value1
        if x > 100:
            self.cost += 50 * 100 + 50 * 150 + (x - 100) * 200
            self.cost += self.cost * 0.05  
        elif x > 50:
            self.cost += 50 * 100 + (x - 50) * 150
            self.cost += self.cost * 0.03  
        else:
            self.cost += x * 100
            self.cost += self.cost * 0.02

    def pr(self): 
        print(self.id, self.name, f'{self.cost:.0f}')

def main(): 
    ls = []
    for t in range(int(input())):
        ls.append(Customer(t+1, input(), int(input()), int(input())))
        ls[t].set_cost()

    sorted_ls = sorted(ls, key=lambda x: x.cost, reverse=True)
    for index, cus in enumerate(sorted_ls):
        cus.pr()
        

if __name__ == "__main__":
    main()