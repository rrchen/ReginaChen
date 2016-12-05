a = [2,4,10,16]

def multiply(list, multiple):
    for i in range(len(list)):
        list[i] *= multiple
    return list

b = multiply(a, 5)
print b
