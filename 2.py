# -*- coding: utf-8 -*-
"""02_basic_structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CHx-F-T28iQ4aAHK-HhAAZ9xD4Y2MMZ6

# Структуры данных

## Структура лекции:

* Встроенные структуры: 
    * Список (list)
    * Кортеж (tuple)
    * Словарь (dict)
    * Множество (set, frozenset)
    * Стек (stack) и очередь (queue)
* Функции:
    * Сигнатура
    * Область видимости
    * Аргументы по умолчанию
    * Передача аргументов
    * Lambda-функции
* Исключения
* Генераторы

### Список (list)

Допустим, близится 8 марта и вы решили спросить у своих знакомых девушек, какие цветы они предпочитают. Вы это сделали и записали соответствующие значения в переменные:
"""

Masha = 'розы'
Dasha = 'лилии'
Katya = 'орхидеи'
Sasha = 'пионы'

"""Но это не очень удобно, можно хранить всю информацию в одной переменной:"""

flowers = ['розы', 'лилии', 'орхидеи', 'пионы']

a = [2 ,3, 4]
a

a = list()

a = []
a

flowers

"""В листе можно хранить информацию разных типов:"""

2 + 3j

my_list = [20, 'котики', 0.45, 2 + 3j]
print(my_list)

"""К элементам листа можно обращаться по индексу:"""

flowers[0]

flowers[1]

flowers[-1]

flowers

flowers[:-3]

a = 0
b = -2
flowers[a:b]

for el in range(-4, 0):
    print('Это значение индекса: {}, а это элемент списка: {}'.format(el, flowers[el]))

flowers[-4]

flowers[1:-1]

"""Листы можно итерировать естественным способом:"""

for flower in flowers:
    print(flower)

"""Или так:"""

for i in range(4):
    print(flowers[i])

"""А еще бывает лист из листов :)"""

flowers = [['Masha', 'розы'], ['Dasha', 'лилии'], ['Katya', 'орхидеи'], ['Sasha', 'пионы']]
flowers

flowers[2][1]

for el in flowers:
    print('имя: {}, цветы: {}'.format(el[0], el[1]))

"""**Есть много методов (т.е. функций, которые присущи только листам) для работы с листами:**

Методы
- list.append(x)	Добавляет элемент в конец списка
- list.extend(L)	Расширяет список list, добавляя в конец все элементы списка L
- list.insert(i, x)	Вставляет на i-ый элемент значение x
- list.remove(x)	Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
- list.pop([i])	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
- list.index(x, [start [, end]])	Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
- list.count(x)	Возвращает количество элементов со значением x
- list.sort([key=функция])	Сортирует список на основе функции
- list.reverse()	Разворачивает список
- list.copy()	Поверхностная копия списка
- list.clear()	Очищает список
"""

a = [1, 2, 3]

a[1] = 'КОТИКИ'
a

a.append('фрукты')
a

a = [1, 2, 3, 4, 5, 5, 5]
a

a.count(5)

print(a)

b = a.copy()
b

c = a
c

b[1] = 'Kotiki'
b

a

c[4] = 'cats'
c

a

"""### Задача 1

Добавьте новый элемент в массив с цветами, соответствующий информации "мама любит фиалки"
"""

flowers

flowers.append(['мама', 'фиалки'])
print(flowers)

"""### Кортеж (tuple)"""

('Masha', 'розы', 'Dasha', 'лилии', 'Katya', 'орхидеи', 'Sasha', 'пионы')

my_tuple = ('Masha', 'розы', 'Dasha', 'лилии', 'Katya', 'орхидеи', 'Sasha', 'пионы')

my_tuple.count?

"""У кортежа есть встроенные методы:
    * .count(some_value) - возвращает кол-во появлений some_value в кортеже
    * .index(some_value) - возвращает индекс элемента some_value в кортеже
"""

my_tuple.index('лилии')

my_tuple.count('лилии')

"""Элементы нельзя изменить (!)"""

my_tuple[0]  = 'КОТИКИ'

"""Но с ними можно производить операции:"""

my_tuple[0] + ' and ' + my_tuple[4]

"""### Словарь (dict)"""

my_dict = {'Masha' : 'розы', 
           'Dasha' : 'лилии', 
           'Katya' : 'орхидеи',
           'Sasha' : 'пионы'
          }

my_dict

"""У словаря есть 'ключи' и 'значения':"""

my_dict.keys()

my_dict.values()

my_dict.items()

my_dict['Masha']

my_dict.pop('Masha')
my_dict

my_dict.update?

a = ()
a

"""### Множество (set)

Как создать переменную типа множество?

Два способа:
"""

my_set = set([4, 5, 6])
type(my_set)

my_set = {4, 5, 6}
type(my_set)

"""А так нельзя, получится словарь:"""

my_set = {}
type(my_set)

"""Что можно делать с множествами?

Теоретико-множественные операции + добавление/удаление/изменение элементов
"""

flowers_set = set(["розы", "лилии", "фиалки", "ирисы", "фиалки", "розы", "пионы", "розы", "ромашки"])
flowers_set

len(flowers_set)

"""Теоретико-множественные операции:

Диаграммы Венна:

![caption](slide_8.jpg)
"""

flowers_set

flowers_set_2 = set(["розы", "незабудки", "ромашки"])
flowers_set_2

"""Пересечение (рис 1):"""

flowers_set & flowers_set_2

flowers_set.intersection(flowers_set_2)

flowers_set | flowers_set_2

flowers_set.union(flowers_set_2)

"""Все элементы множества А, не принадлежащие множеству B (рис 4):"""

flowers_set - flowers_set_2

flowers_set.difference(flowers_set_2)

"""Все элементы множества B, не принадлежащие множеству A (рис 5):"""

flowers_set_2 - flowers_set

flowers_set_2.difference(flowers_set)

"""Проверить, содержатся ли элементы множества B в множестве А:"""

print(flowers_set)
print(flowers_set_2)

flowers_set_3 = set(["розы", "фиалки"])
flowers_set_3

flowers_set_2.issubset(flowers_set)

flowers_set_3.issubset(flowers_set)

"""Удаление/добавление элементов:

* .add(some_element) - добавляет элемент в множество
* .remove(some_element) - удаляет элемент из множества. KeyError, если такого элемента не существует
* .discard(some_element) - удаляет элемент, если он находится в множестве
* .pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым
* .clear() - очистка множества
"""

flowers_set.discard('cats')

flowers_set_3

flowers_set_3.add('КОТИКИ')
flowers_set_3

"""**frozenset** - то же самое, что и **set**, но является неизменяемым типом данных

Что это значит?
"""

set_A = set([3, 4, 5])
set_B = frozenset([3, 4, 5])
print(set_A)
print(set_B)

set_A.add(6)
print(set_A)

set_B.add(6)

"""### Стек и очередь

**Стек (stack LIFO)** 

![caption](lifo_stack.png)

В python стек - это список.

* Добавление элемента в стек: .append(element)
* Извлечение элемента с вершины стека: .pop()
"""

stack = [1, 2, 3, 4, 5]
print(stack)

stack.append(6)
print(stack)

stack.pop()
print(stack)

"""**Очередь (queue FIFO)**

![caption](Fifo_queue.jpg)

В python очередь - это тоже список.

* Добавление элемента в очередь: .append(element)
* Извлечение элемента «в порядке очереди»: .pop(0)
"""

queue = [1, 2, 3, 4, 5]
print(queue)

queue.append(6)
queue.append(7)
print(queue)

queue.pop(0)
print(queue)

a = queue.pop(0)

queue

"""### Функции:

* Сигнатура
* Область видимости
* Аргументы по умолчанию
* Передача аргументов
* Lambda-функции

**Сигнатура**

Функции - это маленькие программки :)
    
Чтобы создать собственную функцию, нужно:
* придумать и определить название функции
* придумать и прописать переменные, которые будет принимать функция на вход (от которых она зависит)
* придумать, что будет явдяться результатом работы функции, т.е. что она будет возвращать
"""

def my_function(var_1, var_2, var_3):
    
    
    
    return var_1 + var_2

"""**Пример:**
    
Написать функцию, которая выполняет сложение двух чисел
"""

def simple_sum(a, b):
    return a + b

simple_sum(10, 3)

simple_sum(a=10, b=3)

def simple_sum_2():
    return aa + bb

aa = 13
bb = 4
simple_sum_2()

def simple_sum_3(aa, bb):
    return aa + bb

simple_sum_3(aa=aa, bb=bb)

d = 10
def my_functions(a, b):
    c = 5
    return (a + b + c + d)

my_functions(1, 1)

d = 10
a = 4
b = 4
my_functions(1, 1)

d = 10
a = 4
b = 4
c = 50
my_functions(1, 1)

my_functions(a=a, b=b)

"""**Задание 2**

Написать функцию, которая считает сумму чисел от a до b включительно
"""

def sum_numbers(a, b):
    sum_=0
    for i in range(a, b+1):
        sum_+=i
    return sum_

sum_numbers(1,3)

1 + 2 + 3

"""**Область видимости**

* Локальная область видимости 
* Глобальная область видимости

**Локальная область видимости**
"""

x = 10
 
def my_function(a, b):
    print("это х:", x)
    print(z)

my_function(1, 2)

"""z - не определена, т.е. **вне области видимости функции**"""

def my_function(a, b):
    k = 10
    print(a, b, k)

my_function(1, 2)

print(k)

"""k - определена **только внутри функции**

**Глобальная область видимости**
"""

def my_function(a, b):
    global k
    k = 10
    print(a, b, k)

my_function(1 ,2)

k

"""**Lambda функции**"""

x = lambda b : b ** 2 + 10

x(3)

x(15)

"""### Исключения"""

my_dict

my_dict['Dasha']

my_dict['Vika']

try:
    print(my_dict['Dasha'])
except:
    print("No such key in the dictionary")

"""### Генераторы"""

def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i

mygenerator = createGenerator() 
print(mygenerator)

for i in mygenerator:
    print(i)

"""#### Задача 1

Используя цикл for, найдите сумму всех элементов заданного списка. (Без использования встроенных функций sum и т.д.)
"""

my_list = [40, 32, 45, 22, 69, 3, 59, 150, 34, 0, 2, 5, 1, 38, 65, 39, 94]
s = 0
for i in my_list:
  s = i + s
  
print(s)

"""Проверка:"""

sum(my_list)

"""#### Задача 2

Напишите функцию, которая принимает на вход список из предыдущего задания и возвращает сумму всех элементов списка. (Без использования встроенных функций sum и т.д.)
"""

def printSum(arr):
  s_ = 0
  for i in arr:
    s_ = i + s_
    return print(s)
  
printSum(my_list)

"""#### Задача 3

Используя цикл (любой) найдите значение максимального элемента списка из предыдущего задания. (Без использования встроенных функций max и т.д.) Можно использовать встроенные методы списков (любые). 

P.S.: не стесняйтесь гуглить :)

P.S.2: гуглить нужно фразу "алгоритм поиска максимального элемента массива"

Пример: для списка [3, 4, 1, 7, 2] значением максимального элемента является число 7
"""

my_list = [40, 32, 45, 22, 69, 3, 59, 150, 34, 0, 2, 5, 1, 38, 65, 39, 94]
maximum = my_list[0]
for i in range(1, len(my_list)):
  if my_list[i] > maximum :
    maximum = my_list[i]
print(maximum)

"""Проверка:"""

max(my_list)

"""#### Задача 4

Напишите функцию, которая принимает на вход список из предыдущего задания и возвращает его максимальный элемент. (Без использования встроенных функций max и т.д.) Можно использовать встроенные методы списков (любые). Т.е. заверните решение предыдущего задания в функцию.
"""

def printStatistics(arr):
    arr.sort()
    print('число элементов:',len(arr))
    if len(arr) == 0:
        print('среднее значение: 0')
    else:
        print('среднее значение:',sum(arr)/len(arr))       
    if len(arr) == 1:
        arr1 = arr.copy()
        n = arr1.pop(0)
        if n == 0:
            print('min: 0')
            print('max: 0')
        else:
            print('min:', float(n))
            print('max:', float(n))
    else:
        print('min:',min(arr))
        print('max:',max(arr))
   
    

printStatistics(my_list)

"""#### Задача 5

Используя список из предыдущего задания (my_list) создайте кортеж и назовите его my_tuple. Найдите индекс элемента, который равен 5. 

P.S. Используйте один из встроенных методов для кортежей
"""

my_list = [40, 32, 45, 22, 69, 3, 59, 150, 34, 0, 2, 5, 1, 38, 65, 39, 94]
my_tuple = tuple(my_list)
print (my_tuple[5])

"""**Задача 6**

Создайте словарь, соответствующий следующему описанию: 
    
В честь 8 марта начальник отдела Валера решил принести на работу коробку конфет и угостить коллег :) Красотка Наташа съела две конфеты, ее подруга Алина - целых три, разработчик Марат унес с собой в соседний опен-спейс целых пятнадцать, чтобы поделиться со своей командой, менеджер проекта Лев проходил мимо и съел одну конфету, а сам Валера, будучи сторонником здорового образа жизни, ни съел ни одной.

P.S. все совпадения случайны :)
"""

slovar_mart = {'Наташа' : 2,
               'Алина' : 3,
               'Марат' : 15,
               'Лев' : 1,
               'Валера'  : 0     
              }
print(slovar_mart)

"""**Задача 7**

Добавьте в словарь из предыдущего задания данные для студента Ромы, который работает неполный рабочий день, и, придя на работу после экзамена, с удовольствием съел 4 конфеты.

P.S. используйте встроенный метод .update
"""

slovar_mart.update({'Рома' : 4})
print(slovar_mart)

"""**Задача 8**

Двое друзей решили отправиться в путешествия. Дима посетил следующие страны: Украина, Египет, США, Германия, Дания. Алина же побывала на Украине, в Египте, Испании, Тунисе, Германии, Швейцарии.

Создайте два множества (set), соответствующие странам, которые посетили Дима и Алина.

Найдите:
* только те страны, в которых побывали и Дима, и Алина (пересечение)
* все страны, которые посетили друзья (объединение)
* страны, в которых Алина побывала, а Дима еще нет
"""

dima = set (['Украина', 'Египет', 'США', 'Германия', 'Дания'])
alina = set(['Украина','Египет', 'Испания', 'Тунис', 'Германия', 'Швейцария'])
print('Дима и Алина были в общих следующих странах :', dima & alina)
obshie = (dima | alina)
print('Все страны которые посетили :', obshie)
print('Страны, в которых Алина побывала, а Дима еще нет, следующие:', alina - dima)

"""**Задача 9**

Запустите две ячейки с кодом ниже и убедитесь, что вы понимаете разницу в выполнении кода:
"""

my_array = [1, 3, "Котики", 4]

for element in my_array:
    print(element / 2)
    
print("Я следующий кусок кода, который НЕ отработал!")

my_array = [1, 3, "Котики", 4]

try:
    for element in my_array:
        print(element / 2)
except:
    print("Не могу поделить, элемент не численного типа!")
    
print("\n")
print("Я следующий кусок кода, который отработал!")

"""**Задача 10**

Используя lambda функцию напишите функцию, которая возводит числа в квадрат. Используя написанную функцию, найдите квадрат числа 12.
"""

kv = lambda a : a**2
kv(12)

"""**Задача 11**


Используя циклы, напишите код, который создает список (list) путем конкатенации значений данного листа с целыми числами от 1 до (произвольного) n включительно.

Пример:

для списка ["сосиски", "горчица"] при n = 3 результат должен выглядеть так:

['сосиски$\_$1', 'горчица$\_$1', 'сосиски$\_2$', 'горчица$\_$2', 'сосиски$\_$3', 'горчица$\_$3']

## пробный вариант
"""

spisk = ("сосиска", "горчица")
print(spisk)
t = int(input())
result = []
for y in range(1,t+1):
    y = str(y)
    for i in range(len(spisk)):
      result.append(spisk[i] + "_"+ y + ',')
print(result)

"""## решение"""

sample_list = ["огурцы", "помидоры", "оливковое_масло"]
print('Введите n :')
t = int(input())
result = []
for y in range(1,t+1):
    y1 = str(y)
    for i in range(len(sample_list)):
      result.append(sample_list[i] + "_"+ y1)
print(result)

"""**Задача 12**

Для предудыщей задачи напишите функцию, которая выполняет те же самые действия.
"""

sample_list = ["огурцы", "помидоры", "оливковое_масло"]
print('Введите число :')
t = int(input())
def printR (x):
    res = []
    for yy in range(1, t+1):
        yy = str(yy)
        for ii in range(len(x)):
            res.append(x[ii] + "_" + yy)
    return print(res)

printR(sample_list)

"""**Задача 13**

Напишите код, который считает количество элементов в заданном списке до тех пор, пока не встретится элемент кортежа.

Пример:

для списка [3, "котики", 0.45, 5, (8, 9), "слоники", 34] на выходе должны получить число 4
"""

list_for_pro_task_2 = [35, 0.24, 3 + 4j, "котики", 0.45, (8, 9), "слоники", ("Мадрид", 3), 23498]
print(list_for_pro_task_2)
count = 0
for e in list_for_pro_task_2:
    try:
        list_for_pro_task_2 = int(e)
        count += count
    except ValueError:
        continue
print(count)

"""**Задача 14**


Создайте словарь (dict) c ключами, соответствующими числам от 1 до 20 включительно и значениями, соответствующими квадратам ключей. 

P.S. используйте циклы или функции, прямое "ручное" присваивание не допускается (!!!)

Пример: 

для чисел от 1 до 3 включительно словарь должен выглядеть так: {1 : 1, 2 : 4, 3 : 9}
"""

kvadrat= {j:j**2 for j in range(1, 21)}
print(kvadrat)

"""**Задача 15**

Напишите функцию, которая выполняет все то же самое, что и в предыдущей задаче, но от 1 до произвольного n.
"""

n = int(input())
def slov():
    slov = {x: x**2 for x in range(1, n+1)}
    print(slov)

slov()

"""**Задача 16**

Напишите все то же самое, что и в предыдущей задаче, с помощью lambda функции.
"""

func = lambda x: {x:x**2 for x in range(1, n+1)}
print('Введите число:')
n = int(input())
func(n)

dima = set (['Украина', 'Египет', 'США', 'Германия', 'Дания'])
alina = set(['Украина','Египет', 'Испания', 'Тунис', 'Германия', 'Швейцария'])
print('Дима и Алина были в общих следующих странах :', dima & alina)
obshie = (dima | alina)
print('Все страны которые посетили :', obshie)
print('Страны, в которых Алина побывала, а Дима еще нет, следующие:', alina - dima)

"""**Задача 17**

Напишите функцтю, которая вычисляет квадратный корень для заданного числа. Довабьте в функцию "защиту от дурака", используя конструкцию исключений (try - except - else).

* добавьте проверку на тип введенных данных
* добавьте проверку на неотрицательность числа, подаваемого на вход
"""

chislo = input()
while chislo.isalpha() or int(chislo) < 0:
    chislo = input("Не верный формат. Введите положительное число число: ")
chislo = int(chislo)
print('Квадрат введенного числа равен = ', chislo**2)