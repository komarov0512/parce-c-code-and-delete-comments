# Открытие файла
def openfile(name):
    data = []
    file = open("code.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        data.append(line)
    return data


# Удаление комментариев
def del_comment(data):
    for i in range(len(data)):
        check = data[i].find("/*")
        check2 = data[i].find("*/")
        if not check == -1:
            if not check2 == -1:
                data[i] = ''
                continue
            while True:
                data[i] = ''
                i += 1
                if not data[i].find("*/") == -1:
                    data[i] = ''
                    break
    for i in range(len(data)):
        check = data[i].find("//")
        if not check == -1:
            data[i] = data[i].partition('//')[0] + '\n'
    return data


# Вывод в консоль
def print_code(data):
    for s in data:
        print("\033[38m\033[40m {}".format(s), end='')


# Main
name_file = "code.txt"
data_file = openfile(name_file)
print("\033[0m\033[33m {}" .format("Before edit:"))
print_code(data_file)
del_comment(data_file)
print("\n\n\033[0m\033[33m {}" .format("After edit:"))
print_code(data_file)






