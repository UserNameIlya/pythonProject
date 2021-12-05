def SynchronizingTables(N,ids:list,salary:list):
    new_salary = [0] * N
    tuple_stuff =[]
    tuple_salary = []

    for number_stuff in range(N):
        tuple_stuff.append((number_stuff, ids[number_stuff]))
    for number_salary in range(N):
        tuple_salary.append((number_salary, salary[number_salary]))

    for i in range(N-1):
        if tuple_stuff[i][1] > tuple_stuff[i+1][1]:
            tuple_stuff[i],tuple_stuff[i+1] = tuple_stuff[i+1],tuple_stuff[i]

    for i in range(N-1):
        if tuple_salary[i][1] > tuple_salary[i+1][1]:
            tuple_salary[i],tuple_salary[i+1] = tuple_salary[i+1],tuple_salary[i]

    for new_i in range(N):
        new_salary[tuple_stuff[new_i][0]] = tuple_salary[new_i][1]
    return new_salary
