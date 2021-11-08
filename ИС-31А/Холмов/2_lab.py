def f(a):
    t = 1
    while a >= 1:
        t = t * a 
        a = a - 1
    return t #факториал

d = {'H':f(23), 'O':f(16), 'L':f(13), 'M':f(14), 'O':f(16), 'V':f(3)}#1)словарь ключ-значение с факториалом
alf = list(d.items())
alf.sort() 
otsort = dict(alf)#2)сортировка по ключу в афлавитном порядке(латиница)

znach = {}
znach_keys = sorted(d, key=d.get, reverse=True)#берем значение ключа и сортируем по нему
for k in znach_keys:
    znach[k] = d[k]#3) от меньшего к большему


def gen():
    for i in range(1,26):
        yield f(i) #4)функция-генератор для факториала(латиница)

znachh = []
for i in d:
    znachh.append(d[i])#список со значениями 

nije = []
vishe = []
sr = sum(znachh) // len(znachh)#среднее по списку
for i in znachh:
    if i < sr:
        nije.append(i)#5)распределение значение списка относительно его ср.знач
    elif i >= sr:
        vishe.append(i)
