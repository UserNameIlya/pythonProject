def SynchronizingTables(N,ids:list,salary:list):
    new_salary = [0] * N
    tuple_stuff = {}
    tuple_salary = {}
    for num_element in range(0,N):
        tuple_stuff[num_element] = ids[num_element]
        tuple_salary[num_element] = salary[num_element]

    rez_stuff = sorted(tuple_stuff.items(), key= lambda para: (para[1],para[0]))
    rez_salary = sorted(tuple_salary.items(), key= lambda para: para[1])

    for i in range(N):
        new_salary[rez_stuff[i][0]] = rez_salary[i][1]

    return new_salary

SynchronizingTables(4,[50, 1,1, 1024],[90000, 20000,50000, 100000])