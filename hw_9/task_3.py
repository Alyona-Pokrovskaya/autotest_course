# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

f1 = open('test_file/task_3.txt', mode='r', encoding='utf-8')
list_buy = []
current_buy = 0

for one_line in f1.readlines():
    if one_line[:-1] != '':
        current_buy = current_buy + int(one_line[:-1])
    else:
        list_buy.append(current_buy)
        current_buy = 0

list_buy.sort()
three_most_expensive_purchases = int(list_buy[-1]) + int(list_buy[-2]) + int(list_buy[-3])
print(three_most_expensive_purchases)



assert three_most_expensive_purchases == 202346
