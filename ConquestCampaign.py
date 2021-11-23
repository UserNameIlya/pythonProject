def ConquestCampaign(N: int, M: int, L: int, battalion: list):
    # 1. Создаем поле размером N*M
    map_city = [[0 for x in range(M)] for y in range(N)]
    count_day = 0

    # 2. Определяем точки высадки

    # 2.1 Получаем координаты первоночальной высадки групп  для каждой группы
    def get_start_position(battalion):
        x = battalion[0]
        y = battalion[1]
        return x, y

    # 2.2 Проверяем, что ячейка пустая
    def check_position(x, y):
        if map_city[x][y] == 0:
            return True
        else:
            return False

    # 2.3 Записываем координаты позиций высдаки
    def start_position(x, y):
        map_city[x][y] = 1

    # 2.4 Убираем отработанные координаты
    def del_coordinat(battalion):
        new_list = battalion[2:]
        return new_list

    # 3 Высадка
    def normandia(L, battalion):
        for i in range(L):
            pos_x, pos_y = get_start_position(battalion)
            if check_position(pos_x, pos_y):
                start_position(pos_x, pos_y)
            battalion = del_coordinat(battalion)



    normandia(L, battalion)
    print(map_city)

    # 4 Проверяем, что все поля захвачены. Возварщаем True если есть еще открытые поля иначе False
    # def is_complete(map_city):
    #     count_open_position = 0
    #     for y in range(M):
    #         count_open_position = +1 if 0 in map_city[x] else 0
    #     if count_open_position > 0:
    #         return False
    #     else:
    #         return True

    # if is_complete(map_city):
    #     # все поля захвачены
    #     pass
    # else:
    #     #не все поля захвачены
    #     #нужно пройти цикл захвата
    #     #увеличиваем день на один
    #     pass




ConquestCampaign(3, 4, 2, (1, 2, 2, 3))
