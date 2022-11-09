def get_count_char(str_):
    str_ = str_.lower()
    d = {}

    for c in str_:
        if c.isalpha():
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    return d


def percent(d):
    sum_d = 0
    for c in d:
        sum_d += d[c]
    for c in d:
        d[c] = round(d[c] / sum_d * 100, 1)
    return d

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent(get_count_char(main_str)))

