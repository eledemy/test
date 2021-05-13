AUTHOR = 'author.txt'

import random

with open(AUTHOR, encoding='utf-8') as f:
    a = f.readlines()

author = random.choice(a)

print(author)
