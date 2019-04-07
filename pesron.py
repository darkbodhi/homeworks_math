class Acquintance(object):

    def __init__(self):
        self.name = None
        self.byear = None
        self.pnumber = None

    def input(self):
        self.name = input("Введіть ім*я знайомого: ")
        self.byear = input("Введіть рік народження знайомого: ")
        self.pnumber = input("Введіть номер телефону знайомого: ")

    def print(self):
        print(self.name, self.byear, self.pnumber)

    def read_database(self):
        data_name = str(input("Please, insert the name of the file you want to import: "))
        f = open("data_name", "r")
        contents = f.read()
        print(contents)

    def create_database(self):
        data_name2 = str(input("Please, insert the name of the file you want to create: "))
        f = open("data_name2", "w+")
        f.write("{} : {} : {}".format(self.name, self.byear, self.pnumber))
        f.close()