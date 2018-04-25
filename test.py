import datetime
import random
import string
import re
import urllib.request
import urllib.parse


# 2. Есть массив с 20 целыми числами. Найти первые 3 числа
# больше заданного.
def av(x):
    random_list = [int(random.choice(string.digits)) for _ in range(20)]
    result = []
    for i in random_list:
        if i <= x:
            continue

        result.append(i)

        if len(result) > 3:
            break

    return result


# 3. Есть фраза на английском. Необходим уникальный
# массив согласных, использованный в этой фразе.
def get_consonants_set(s):
    consonants = 'bcdfghigklmnpqrstvwxz'
    return set(i for i in s if i in consonants)


# 4. Есть словарь. Инвертировать его. Т.е. пары ключ:
# значение поменять местами — значение: ключ.
def convert_dict(initial):
    return dict(((value, key) for key, value in initial.items()))


# 8. Есть сущность "Задание" Task, есть "Исполнитель"
# Executor.
# Они находятся в отношении Many-to-Many.
# С помощью Django ORM вытащить все задания с
# исполнителем id = 5, созданные в промежутке "2018-03-01"
# и "2018-03-10" и в status = "closed"

class Task:
    pass


start = datetime.datetime.strptime('2018-03-01', '%Y-%m-%d')
finish = datetime.datetime.strptime('2018-03-10', '%Y-%m-%d')
Task.objects.filter(executor_id=5, created_at__gt=start, created_at__lt=finish, status='closed')


# 12. В таблице хранятся целые числа, отсортированные по возрастанию, некоторые были удалены.
# Написать SQL-запрос для поиска второго пропущенного числа.
# Числа порядковые. 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17 => Найти 10

"""SELECT generate_series FROM generate_series(1, 17) WHERE
    NOT generate_series IN (SELECT x FROM values) offset 1 limit 1;
"""


# 13. Написать скрипт который забирает страничку с интернета и вытаскивает все
# ссылки ведущие на внешние(на другом домене)страницы. Без использования BeautifulSoup и подобного.
def get_external_link_list(url):
    response = urllib.request.urlopen(url).read().decode()
    netloc = urllib.parse.urlparse(url).netloc

    link_list = re.findall(r'<a .*href=\"(https?://.+?)\".*>', response)
    return [link for link in link_list if urllib.parse.urlparse(link).netloc != netloc]


# 14. Есть функция.
# Если в качестве аргумента передать 1, то результат будет 2,
# если передали 2, результат равен 1.
# Как может выглядеть эта функция без использования условных операторов. (2 способа)

# Решение с помощью словаря
def first_method_dict(arg):
    return {1: 2, 2: 1}.get(arg)


# Решение с помощью целочисленного деления
def second_method_set(arg):
    return 2 // arg


# 15. Есть таблица с книгами Books, у книги может быть несколько авторов,
# которые хранятся в табличке Author (У автора тоже может быть несколько книг).
# Написать запрос для получения списка книг, у которых авторов и соавторов менее 3.
# отношение ManyToMany в Django
# Book_Authors - дополнительная таблица с двумя колонками: author_id, book_id
"""
SELECT *, COUNT("Book_Authors"."book_id") AS "c" FROM "Book" 
LEFT OUTER JOIN "Book_Authors" ON ("Book"."id" = "Book_Authors"."book_id") 
GROUP BY "Book"."id" HAVING COUNT("Book_Authors"."branch_id") < 3;
"""
