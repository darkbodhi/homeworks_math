def parent():

    def delete_repeat(contents):
        set(contents)


    def read_file(data_file):
        data_file = str(input("Please, input the name of the file to read from: "))
        f = open("data_file", "r")
        f.open()
        contents = []
        contents.append(f.readlines())
        f.close()
        return(contents)