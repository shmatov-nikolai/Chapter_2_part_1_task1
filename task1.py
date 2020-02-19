'''
Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
регистре (заглавные) и в нижнем регистре (прописные).
'''


vvod_user = input("введите текст для обработки:")
small_letter = []
big_letter = []
for letter in vvod_user:
    if letter == letter.lower():
        small_letter.append(letter)
        
    elif letter == letter.upper():
        big_letter.append(letter)

procent_small = len(small_letter)*100 / len(vvod_user)
procent_big = len(big_letter)*100 / len(vvod_user)


print(f"Общая длина введеного текста:{len(vvod_user)}")
print("количество букв в нижнем регистре:{}, в процентах: {:.1f} %".format(len(small_letter), procent_small))
print("Количество букв в вверхнем регистре:{}, в процентах: {:.1f} %".format(len(big_letter), procent_big))
