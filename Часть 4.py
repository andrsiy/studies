# # 4.1
# a = [1,2,3,4,5]
# print("Первый элемент: ",a[0])
# print("Третий элемент: ",a[2])
# print("Первые 3 элемента:",a[:3])

# # 4.2
# a = ["Ростов", "+", "на","-","Дону"]
# a[1] = "-"
# print(a[0],a[1],a[2],a[3],a[4])

# # 4.3
# a = ["a","s","1","a","32","23"]
# letters = []
# numbers = []
#
# for item in a:
#     if item.isalpha():
#         letters.append(item)
#     elif item.isdigit():
#         numbers.append(item)
#
# print("Буквы",letters)
# print("Числа",numbers)

# # 4.4
# a = ["a","s","1","a","32","23"]
# letters = []
# numbers = []
#
# for item in a:
#     if item.isalpha():
#         letters.append(item)
#     elif item.isdigit():
#         numbers.append(item)
#
# letters = letters[:-1]
# print(letters)

# # 4.5
# a = ["a","s","1","a","32","23"]
# my_set = set(a)
# print(my_set)
# # все элементы выводятся рандомным списком, а также нет повторений