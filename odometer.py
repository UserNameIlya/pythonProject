def odometer(list):

    if len(list) == 2:
       return list[0] * list[1]
    else:
        return list[0] * list[1] + odometer(list[2:])