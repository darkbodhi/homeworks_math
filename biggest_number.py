data_name = str(input("Please, insert the name of the file to import data from: "))
f = open("data_name", "r")
z = int()
number_list1 = []
number_list2 = []
contents = f.read()
for line in contents:
    number_list1.append()
    z = number_list1.max()
    number_list2.append(z)
    number_list1.clear()
f.close()
print(number_list2.max())