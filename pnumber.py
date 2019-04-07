database_name = str(input("Please, input the name of the database: "))
phone_dict = {"Name": None,  "Number": None}
text_inf = str()
num_inf = int()
f = open("database_name" "rt")
f1 = f.readlines()
for text_inf in f1:
    phone_dict['Name'] = text_inf
for num_inf in f1:
    phone_dict['Number'] = num_inf
f.close()
print(phone_dict)