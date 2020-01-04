# -*- coding: utf-8 -*-
"""08_Visualization_with_Matplotlib_homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uk46YydytYiABaCKeEUr0fIdjpE4zExS

# Визуализация данных с MatPlotLib
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import misc
import matplotlib.colors as mcolors
import seaborn as sns
# %matplotlib inline

"""### Задача 1

Постройте график экспоненты. Подпишите оси. Дайте название графику.
"""

x = np.linspace(0, 5, 100)
y = np.exp(x)
plt.plot(y)
plt.title('график экспоненты')
plt.xlabel('ось  x ')
plt.ylabel('ось  y ')

"""### Задача 2

Постройте график функции $\rho = 4 \sin(2\phi)$ в полярных координатах. Линия должна быть любого нестандартного цвета из доступных по ссылке ниже (на ваш вкус). Дайте название графику.

https://matplotlib.org/3.1.0/gallery/color/named_colors.html
"""

plt.figure(1, figsize=(10,7))
r = np.arange(0, 2, 0.01)
q = 2 * np.pi * r
y = 2* np.sin(2*q)
ax = plt.subplot(projection='polar')
ax.plot(y, c= 'lime')
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2]) 
plt.title('  ρ=4sin(2ϕ) ')
plt.show()

"""### Задача 3

Постройте графики функций $y = x^3$ и $y = x^2$ на одном графике. 

* Дайте название графику 
* Дайте названия осям
* Присвойте лейблы и выведите легенду
* Графики функций должены быть отрисованы пунктирными линиями (любыми из доступных на ваш вкус)
"""

plt.figure(1, figsize=(10,7))
x = np.linspace(0,10,80)
y= x**3
y_=x**2
plt.plot(x, y, label='y=x**3', c='r', ls=':', mec='b')
plt.plot(x, y_, label='y=x**2', c='tan', ls=':', mec='r')
plt.title('y=x**3 и y=x**2')
plt.xlabel('ось х')
plt.ylabel('ось y')
plt.legend()
plt.show()

"""### Задача 4

Выведите на экран картинку ascent, которая подгружается кодом ниже
"""

from scipy import misc
img = misc.ascent()
plt.imshow(img)
plt.colorbar()
plt.show()

img

img.shape

"""### Задача 5

Выведите на экран картинку выше в серых цветах (grayscale)
"""

plt.imshow(img, cmap ='gray')
plt.colorbar()
plt.show()

"""### Задача 5

Для датасета "Ирисы", который подгружается кодом ниже, нарисуйте точечную диаграмму (scatter plot) всех четырех признаков. Каждый признак должен быть нарисован на отдельном графике. Используйте для этого subplot формата 2 на 2. Графики должны быть читаемыми, т.е. отрегулируйте размер subplot'ов. Добовьте названия признаков к каждому графику в качестве имени графика. Используйте метки классов (y) в качестве цветовой разметки. Добавьте расшифровку цветов, соответствующих меткам классов, в качестве лейблов.

P.S. используйте функцию plt.scatter(x, y, color)
"""

from sklearn import datasets
data = datasets.load_iris(return_X_y=False)
X = data.data
y = data.target
names = data.target_names

iris = sns.load_dataset("iris")
iris.head()

sns.pairplot(iris, hue='species', size=3);

"""### Преобразования изображений"""

import scipy
from scipy import misc
face = misc.face()

# выводим изображение на экран
plt.imshow(face)
plt.show()

import matplotlib.transforms as mtransforms

def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)


# prepare image and figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
Z = face.copy()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1, .5))

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1, .5).translate(.5, -1))

plt.show()