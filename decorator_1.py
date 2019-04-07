def parent():

    def input_number(number):
        number = int(input("Please, insert the number: "))
        return(number)

    def correct_number(number):
        a = int(input("Please, insert the lower border: "))
        b = int(input("Please, insert the upper border: "))
        if not a < b:
            raise Exception("Error. Lower border should be less than upper one.")
        elif a > number > b:
            return(number)
        else:
            number = a + ((b - a)/2)
            return(number)
