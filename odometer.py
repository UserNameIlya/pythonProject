def odometer(list):
    distance = 0
    for i in range(0,len(list),2):
        if i == 0:
            distance = list[i] * list[i+1]
        else:
            distance = distance + list[i] * (list[i+1] - list[i-1])
    return distance