number_str = input('Введите цифры через разделитель: ')
number_list = []
number_list = number_str.replace(';', ',').replace('/', ',').split(',')
itog_list = []
for number in number_list:
    if number_list.count(number) == 1:
            itog_list.append(int(number))
print(itog_list)

# альтернативный вариант через удаление элементов в списке
# number_str = input('Введите цифры через разделитель: ')
# number_list = []
# number_list = number_str.replace(';', ',').replace('/', ',').split(',')
# for number in number_list:
#     if number_list.count(number) > 1:
#         for i in range(number_list.count(number)):
#             number_list.remove(number)
# itog_list = []
# for number in number_list:
#     itog_list.append(int(number))
# print(itog_list)