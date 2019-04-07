x = float(input("Please, insert the value of x for calculation of approximation of function 1/(1+x): "))
approximation_range = input("Please, insert the approximation level: ")
n = int(1)
tailor_row = []
if x > 1 or x < -1:
    raise Exception("Values of x should be between 1 and -1.")
else:
    tailor_row.append(1)
    for i in (0, approximation_range):
        z = - x**n + x**(n+1)
        tailor_row.append(z)
        n += 2
    print(sum(tailor_row))