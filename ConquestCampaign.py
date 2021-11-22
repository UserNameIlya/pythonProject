def ConquestCampaign(N:int,M:int,L:int,battalion:list):

    #1. Создаем поле размером N*M
    map_city = [[0 for x in range(N)] for y in range(M)]
    print(map_city)

    #2. Проверяем, что все поля захвачены. Возварщаем True если есть еще открытые поля иначе False
    def is_complete(map_city):
        count_open_position = 0
        count_day = 0
        for y in range(M):
            count_open_position =+1 if 0 in map_city[y] else 0
        if count_open_position > 0:
            return True
        else:
            return False

    print(is_complete(map_city))

    #3. Получаем координаты первоночальной высадки групп  для каждой группы
    def get_start_position(battalion):
            x = battalion[0]
            y = battalion[1]
            return x,y
            battalion[2:]

    print(get_start_position(battalion))

    # 4. Записываем координаты нулевых позиций для групп
    def start_position(count_group):
        i = 0
        if i != count_group:
            get_start_position(battalion)
            i += 1



    start_position(L)
    # # Проверяем, что ячейка пустая
    #     if map_city[x][y] == 0:
    #         exit
    #     else:
    #         return x,y
    #
    # x,y = group_positon(battalion)
    # map_city[x][y] = 1

ConquestCampaign(3,4,2,(1,2,2,3))
