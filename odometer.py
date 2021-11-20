def odometr(list):

    if len(list) == 2:
       return list[0] * list[1]
    else:
        return list[0] * list[1] + odometr(list[2:])


print(odometr([10,1,20,2]))