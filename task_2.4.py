# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    x = ''
    for char in s:
        if char != '!':
            x = x + char

    return x

print(remove_exclamation_marks("Hi! Hello!"))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    for char in s:
        a = ''
        if s[-1] == '!':
            a = s[:-1]
        else: a = s
    return a

print(remove_last_em("Hi!!!"))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi!! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    arr = s.split(' ')
    total_arr = []
    for i in arr:
        a = 0
        for j in i:
            if j == '!':
                a +=1
        if a != 1:
            total_arr.append(i)
    x = ' '.join(total_arr)
    return x



print(remove_word_with_one_em("Hi! !Hi! Hi!"))