src = not False and True or False and not True

# TODO расписать упрощение выражения
# not False = True, следовательно первая часть выражения True and True = True
# not True = False, следовательно вторая часть выражения False and False = False
# Итог: True or False = True
result = True

print(src == result)
