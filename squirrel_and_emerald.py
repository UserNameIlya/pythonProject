def squirrel(N):

    def fact(N):

        if N == 1 or N == 0:
            return 1
        else:
            return N * fact(N - 1)

    return (int(str(fact(N))[0]))

print(squirrel(0))