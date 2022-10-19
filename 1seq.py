count_elements = ''
while not count_elements.isdigit():
    count_elements = input('Введите количество элементов: ')
count_elements = int(count_elements)
element_list = []
for element in range(count_elements):
    num = ''
    while not num.isdigit():
        num = input(f'Введите {element + 1}  элемент: ')
    element_list.append(int(num))
print(element_list)