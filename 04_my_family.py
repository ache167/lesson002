#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья
my_family = ["Mascot", "Agatha", "Zoizehn"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 22],
    [my_family[1], 15],
    [my_family[2], 18]
]

# Выведите на консоль рост отца в формате
#   Рост Zoizehn - ХХ см
print(my_family_height[2][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
height_sum = 0

for i in my_family_height:
    height_sum += i[1]

print(height_sum)
