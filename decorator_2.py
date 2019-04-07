def parent():

    def type_check(*args):
        if args == int():
            return
        else:
            exit()

    def medium_var(a, b, c):
        a = int(input("Please, insert the first variable: "))
        b = int(input("Please, insert the second variable: "))
        c = int(input("Please, insert the third variable: "))
        return((a + b + c)/3)