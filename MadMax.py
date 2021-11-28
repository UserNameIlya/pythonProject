def MadMax(Tele:list):

    #Отсортировать массив по возрастанию
    def bubble_sort(Tele):
        for bypass in range(1, len(Tele)):
            for k in range(0,len(Tele)-bypass):
                if Tele[k] > Tele [k+1]:
                        Tele[k], Tele[k+1] = Tele[k+1],Tele[k]
        return Tele

    #Сортируем вторую часть перестоновкой
    def reverse_list(Tele):
        #Находим центр
        def get_center_index(Tele):
            center_index = len(Tele)//2
            return center_index

        center_list = get_center_index(Tele)

        for i in range(1, len(Tele)-center_list):
            for k in range(center_list,len(Tele)-i):
                if Tele[k] < Tele [k+1]:
                        Tele[k], Tele[k+1] = Tele[k+1],Tele[k]
        return Tele

    #вернуть Tele
    bubble_sort(Tele)
    reverse_list(Tele)
    return Tele

print(MadMax([2,1,7,4,5,6,3]))