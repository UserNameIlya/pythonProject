def ConquestCampaign(N, M, L, battalion):

    day = 1
    # Создаем площадь
    kingdom_s = []
    for i in range(N):
        kingdom = []
        for j in range(M):
            kingdom.append(0)
        kingdom_s.append(kingdom)

    #Получаем  координаты для высадки
    def get_coordinat(L,battalion):
        for a in range(L):
            coordinate_x = battalion[a * 2]
            coordinate_y = battalion[a * 2 + 1]
            kingdom_s[coordinate_x - 1][coordinate_y - 1] = 1
        return kingdom_s

    # Поле пустое?
    def check_full(x,y):
        if kingdom_s[x][y] == 0:
            return True
        else:
            return False

    #  Мы уже были ранее в этом поле
    def check_priviosly(x,y):
        if kingdom_s[x][y] == 1:
            return True

   # Заполняем окрестноси

    def get_neighbors(x,y):
        if y > 0 and kingdom_s[x][y - 1] == 0:
            kingdom_s[x][y - 1] = 1
        if y + 1 < M and kingdom_s[x][y + 1] == 0:
            kingdom_s[x][y + 1] = 1
        if x > 0 and kingdom_s[x - 1][y] == 0:
            kingdom_s[x - 1][y] = 1
        if x + 1 < N and kingdom_s[x + 1][y] == 0:
            kingdom_s[x + 1][y] = 1
        return kingdom_s

    get_coordinat(L, battalion)

    def field(N,M,kingdom_s):
        for x in range(N):
            for y in range(M):
                 if check_full(x,y):
                    continue
                 if check_priviosly(x,y):
                    kingdom_s[x][y] = 2
                    get_neighbors(x,y)
        return kingdom_s

    for i in range(N):
        for j in range(M):
            if kingdom_s[i][j] == 0:
                day +=1
                field(N,M,kingdom_s)
            else:
                return day
N = 3
M = 4
L = 2
battalion = [2, 2, 3, 4]

print(ConquestCampaign(N, M, L, battalion))