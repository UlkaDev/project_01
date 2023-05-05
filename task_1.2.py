# Задача 1.2.
import time
# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random

time_random_songs = 0

for i in range(0, 2):
    x = random.randint(0, len(my_favorite_songs)-1)
    time_random_songs = my_favorite_songs[x][1]


print(f"Три песни звучат {time_random_songs.__round__(2)} минут")

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

time_random_songs_dict = 0
for i in range(0, 2):
    a = random.choice(list(my_favorite_songs_dict))
    time_random_songs_dict = my_favorite_songs_dict[a] + time_random_songs_dict

print(f"Три песни звучат {round(time_random_songs_dict, 2)} минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

print(my_favorite_songs[random.randint(0, 8)][0])
print(random.choice(list(my_favorite_songs_dict)))

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime
from datetime import datetime

list_for_format_time = []
for item in my_favorite_songs:
    list_for_format_time.append(item[1])

for item in list_for_format_time:
    s = datetime.strptime(str(item), '%M.%S')

    print(s)
