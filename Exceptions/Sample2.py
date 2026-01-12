#
numbers1=15
numbers2=0

try:
    num=numbers1/numbers2
    print(num)
except ZeroDivisionError as e:
    print(e)

