import numpy as np
import matplotlib.pyplot as plt

# Определим функцию y = sqrt(x) * exp(-x**2)
def func(x):
    return np.sqrt(x) * np.exp(-x**2)

# Зададим диапазон значений x
x = np.linspace(0, 2, 100)  # от 0 до 2 с шагом 0.01

# Построим график функции
plt.plot(x, func(x), label='y = sqrt(x) * exp(-x**2)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Найдем производную функции для определения наклона касательной
def derivative(x):
    return (1 - 2*x**2) * np.exp(-x**2) / (2*np.sqrt(x))

# Найдем значение производной в точке x=1
slope = derivative(1)

# Найдем значение функции в точке x=1
y_val = func(1)

# Уравнение касательной
tangent_line = lambda xx : slope*(xx - 1) + y_val

# Построим уравнения касательной
plt.plot(x, tangent_line(x), label='Tangent at x=1', linestyle='--')
plt.scatter(1, y_val, color='red')  # отметим точку касания))

plt.title('График функции с касательной')
plt.legend()
plt.show()



