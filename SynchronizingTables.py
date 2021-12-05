def SynchronizingTables(N,ids:list,salary:list):
    new_salary = [0] * N
    tuple_stuff =[]
    tuple_salary = []

    for number_stuff in range(N):
        tuple_stuff.append((number_stuff, ids[number_stuff]))
    for number_salary in range(N):
        tuple_salary.append((number_salary, salary[number_salary]))

    for pos in range(N-1):
        for k in range(pos+1,N):
            if tuple_stuff[k][1] < tuple_stuff[pos][1]:
                tuple_stuff[k],tuple_stuff[pos] = tuple_stuff[pos],tuple_stuff[k]

    for pos in range(N-1):
        for k in range(pos+1,N):
            if tuple_salary[k][1] < tuple_salary[pos][1]:
                tuple_salary[k], tuple_salary[pos] = tuple_salary[pos], tuple_salary[k]

    for new_i in range(N):
        new_salary[tuple_stuff[new_i][0]] = tuple_salary[new_i][1]
    return new_salary