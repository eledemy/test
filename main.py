"""
Составление словаря с описанием параметров книг: название, год, страницы, ISBN, рейтинг, цена, скидка, автор.
"""
from random import random, randint, choice

from conf import MODEL

AUTHOR_FILE = 'author.txt'


def dict_() -> dict:

    pk = 1

    while True:

        with open('book.txt', encoding='utf-8') as f:
            a = f.readlines()
            title = choice(a)
        print(title)

        year = randint(2000, 2021)
        print(year)

        pages = randint(1, 500)
        print(pages)

        rating = 5 * random()
        print(rating)

        price = random()
        print(price)

        discount = randint(1, 100)
        print(discount)


        with open(AUTHOR_FILE, encoding='utf-8') as f:
            a = f.readlines()
        author_ = choice(a)
        print(author_)

        dict_book = {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title,
                "year": year,
                "pages": pages,
                "isbn13": "978-1-60487-647-5",
                "rating": rating,
                "price": price,
                "discount": discount,
                "author": author_
            }
        }

        yield dict_book
        pk += 1


if __name__ == '__main__':
    gen = dict_()
    for _ in range(4):
        print(next(gen))
