# homework
multiplied = 1
for i in range(2, 21, 2):
    print(f'2*{multiplied}={i}')# тут таблица умножения на 2
    multiplied += 1
# и так далее

'''
конспект
В этом уроке прошли списки. В них можно сохранять разные виды данных.
Можно писать спец команду чтобы сделать список
'''
l3 = list((1, 2, 3))
'''
или же просто поместимть в квадратные скобки. Так же внутри списка может быть еще список.
'''
l = [1, 2, 3, 'hello', ['test', 10], 'world', True]