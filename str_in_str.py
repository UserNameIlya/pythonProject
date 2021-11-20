st1 = 'молоко' #подстрока
st2 = 'gмолоfаывафымолокоафываыфп' #cтрока

def find_str(st1, st2):
    if len(st1) > len(st2) or len(st1) == len(st2) == 0:
        return False

    i = 0
    for a in range(len(st2)):
        if st1[i] == st2[a]:
            i = i + 1
            if i == len(st1):
                return True
                break
        else:
            i = 0
    return False

print(find_str(st1,st2))