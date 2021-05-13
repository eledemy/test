# “discount” - размер скидки, генерируется случайным образом, в виде натурального числа от 1 до 100.
# Если скидка отсутствует, то поле принимает значение None.


import random

discount = random.randint(1, 100)
print(discount)
if discount == 0:
    print('None')

