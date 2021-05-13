import random

with open('book.txt', encoding='utf-8') as f:
    a = f.readlines()
title = random.choice(a)
print(title)

