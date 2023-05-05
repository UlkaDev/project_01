# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [{'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [{'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175},]
}


# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"


#Вариант 1

titles2 = dict(zip(titles.values(), titles.keys()))

allQuantity = {}
allPrice = {}

for item in titles2:
    tQuantity = 0
    tPrice = 0
    for jtem in store[item]:
        tQuantity = tQuantity + jtem['quantity']
        tPrice = tPrice + jtem['quantity']*jtem['price']
        allQuantity[item] = tQuantity
        allPrice[item] = tPrice

result = {}
for item in titles2:
    result[item] = {
    'tittle': titles2.get(item),
    'quantity': allQuantity.get(item),
    'price': allPrice.get(item)
    }

for item in result:
    print(f'{result[item]["tittle"]} - {result[item]["quantity"]} шт, стоимость {result[item]["price"]} руб')



#Вариант 2

idList = titles.values()
all_quantity = {}
all_price = {}
# Бежим по списку ID
for item in idList:
    tQuantity = 0
    tprice = 0
    # Бежим по листу магазинов
    for shop in store[item]:
        tQuantity = tQuantity + shop['quantity']
        tprice = tprice + shop['quantity'] * shop['price']
    all_quantity[item] = tQuantity
    all_price[item] = tprice

for item in idList:
    print(f"{item} - {all_quantity[item]} шт, стоимость {all_price[item]} руб.")
