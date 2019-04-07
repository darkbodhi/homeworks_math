class Polynom(object):
    pass

    def __init__ (self):
        self.coeficcient = float(None)
        self.power = int(None)
        self.var = x

    def construct_member(self):
        self.coefficient = input("Insert the coefficient of the member: ")
        self.power = input("Insert the power of the member: ")
        y = self.coeficcient*self.var**self.power
        list = []
        list.append(y)

    def find_derivative(self):
        y2 = self.coeficcient*self.power*self.var**(self.power-1)
        list2 = []
        list2.append(y2)

    def construct_polynom(self):
        print(sum(list))

    def construct_derpolynom(self):
        print(sum(list2))