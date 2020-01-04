# -*- coding: utf-8 -*-
"""Copy_of_07_Intro_to_Pandas_II_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IL9IzhtstUoiAiU7gQQQR5oo9APlZfug

#  Обработка данных с Pandas II

### Задача 1: DateTime index

* Подгрузите данные 'data.csv' (возможно придется указать кодировку encoding сp1250)
* Преобразуйте колонку Invoice Date в DateTime index
* Удалите колонку Invoice Date
* Сохраните получившуюся табличку в новую переменную data
"""

from google.colab import files
import pandas as pd
import numpy as np

file = files.upload()

!ls

date = pd.read_csv('data.csv', encoding="cp1252")
date.head()

date.index = pd.to_datetime(date.InvoiceDate)
date.head()

date.drop('InvoiceDate', axis=1, inplace=True)
data = date
data.head()

"""### Задача 2

Используя табличку, полученную в результате выполнения предыдущей задачи, выберите все заказы, совершенные за период 7 Декабря 2010 года с часа дня до часа и одной минуты.
"""

data['2010-12-07 13:00':'2010-12-07 13:01']

"""### Задача 3

По той же рабочей табличке:
* посчитайте кол-во уникальных наименований товаров, которые купили за весь период (т.е. по всем данным). Используйте соответствующий метод
* найдите все уникальные страны, в которых были размещены заказы
"""

data.Description.nunique()

data.Country.nunique()

"""### Задача 4

Посчитайте матрицу корреляции Спирмена для наших данных
"""

data.corr('spearman')

"""### Задача 5

Найдите 1%, 50% и 99% квантили цены за единицу товара
"""

data.quantile([0.01, 0.50, 0.99])

"""### Задача 6

Найдите количество клиентов, которые оформляли заказ в понедельники. Для этого:
* сделайте подвыборку, соответствующую условию "в понедельник", используйте метод datetime индекса weekday_name
* посчитайте кол-во уникальных ID клиентов
"""

data_M = data[data.index.weekday_name == 'Monday']

data_M.CustomerID.nunique()

data_M

"""### Задача 7

Создайте новый столбец TotalCost со значениями Quantity * UnitPrice. Сделайте resampling данных в еженедельные со значениями суммы по столбцам TotalCost.
"""

data['TotalCost'] = data.Quantity * data.UnitPrice
data.head()

data.TotalCost.resample('W').sum()

"""### Задача 8
Посчитайте скользящее недельное среднее суммы ежедневных заказов. Для этого:
* Сделайте resampling в ежедневные данные
* Посчитайте скользящее среднее за 7 дней по столбцу TotalCost
"""

data_sr = data.TotalCost.resample('D').sum()
data_sr.head(9)

data_sr.rolling(7).mean().head(9)

data_sr.rolling('7D').mean().head(9)

"""### Задача 9 GroupBy

Посчитайте общую стоимость заказов на ежемесячной основе в разбивке по странам
"""

pd.options.display.float_format = '{:,.1f}'.format
data.groupby(['Country'])['TotalCost'].sum()

"""### Задача 10 Groupby + agg

Посчитайте на ежемесяной основе:
* сумму по общей стоимость заказа TotalCost
* кол-во уникальных клиентов CustomerID
* кол-во заказов (уникальные по полю InvoiceNo)
"""

data.groupby([data.index.month])['TotalCost'].sum()

data.groupby([data.index.month])['CustomerID'].nunique()

data.groupby([data.index.month])['InvoiceNo'].nunique()

"""### Задача 11 JOIN

* Подгрузите данные, содержащие информацию о номерах карт лояльности пользователей (card_data.csv)
* Назовите ее cards
* Сделайте Left Join исходной таблицы (которая получилась после задачи с datetime индексом) и таблицы cards
"""

file = files.upload()

!ls

cards = pd.read_csv('card_data.csv', encoding="cp1252")
cards.head()

data_M.merge(cards, on = 'CustomerID', how = 'left')