import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.sqrt(x) * math.exp(-x**2)
def f_pr(x):
    return (-4*x*x+1/(2*math.exp(x**2)*x**(1/2)))
def yk(t, x):
    for i in x:
        y1.append(f(t) + f_pr(t) * (i - t))
    return y1
tochka_kasaniya = 0.5
h = float(input())
h = round(1/h)
x = np.linspace(1.5,3,h)
y = []
for i in x:
    y.append(f(i))
x1 = [1.5, 3.0]
y1 =[]
plt.title('График')
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
plt.plot(x, y)
plt.plot(x1, yk(tochka_kasaniya, x1))
plt.plot(tochka_kasaniya, f(tochka_kasaniya), "ro")

plt.show()



