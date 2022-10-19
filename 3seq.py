number_str = input('Введите цифры через разделитель: ')
number_str_del = input('Введите цифры через разделитель, которые будут удаляться: ')
number_list = []
number_list = number_str.replace(';', ',').replace('/', ',').split(',')
number_list_del = []
number_list_del = number_str_del.replace(';', ',').replace('/', ',').split(',')

for number in number_list_del:
    if number_list.count(number) >= 1:
        for i in range(number_list.count(number)):
            number_list.remove(number)
itog_list = []
for number in number_list:
    itog_list.append(int(number))
print(itog_list)