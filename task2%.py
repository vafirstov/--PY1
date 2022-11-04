dict_ = {}
def get_count_char(str_):
    str_ = "".join(str_.lower().split())
    for letter in str_:
        if letter.isalpha():
            if letter in dict_:
                dict_[letter] += 1
            else:
                dict_[letter] = 1
    return dict_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_percent_char(new_dict):
    total_count = sum(new_dict.values())
    for count in new_dict:
        new_dict[count] = round(new_dict.get(count) * 100 / total_count, 1)
    return new_dict

print(get_percent_char(dict_))



