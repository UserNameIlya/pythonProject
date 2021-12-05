def SynchronizingTables(N,ids:list,salary:list):
    new_salary = [0] * N
    tuple_stuff = {}
    tuple_salary = {}
    for num_element in range(0,N):
        tuple_stuff[ids[num_element]] = num_element
        tuple_salary[salary[num_element]] = num_element

    rez_stuff = sorted(tuple_stuff.items(), key= lambda para: para[0])
    rez_salary = sorted(tuple_salary.items(), key= lambda para: para[0])

    for i in range(N):
        new_salary[rez_stuff[i][1]] = rez_salary[i][0]

    return new_salary,rez_stuff,rez_salary

print(SynchronizingTables(3,[50, 1, 1024],[90000, 20000, 100000]))