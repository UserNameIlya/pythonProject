def MadMax(N,Tele:list):

    def bubble_sort(N,Tele):
        for bypass in range(1, N):
            for k in range(0,N-bypass):
                if Tele[k] > Tele [k+1]:
                        Tele[k], Tele[k+1] = Tele[k+1],Tele[k]
        return Tele

    def reverse_list(N,Tele):
        def get_center_index(N):
            center_index = N// 2
            return center_index

        center_list = get_center_index(N)

        for i in range(1,N-center_list):
            for k in range(center_list,N-i):
                if Tele[k] < Tele [k+1]:
                        Tele[k], Tele[k+1] = Tele[k+1],Tele[k]
        return Tele

    bubble_sort(N,Tele)
    reverse_list(N,Tele)
    return Tel