'''author:
Group 3
Section 9
Mohanned Ahmed Elsayed 120200113
Gana Elsaid Elemam 120200224
'''

import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return z**np.cos(z)+2


N = int(input("The number of points to be randomised: "))
S = int(input("The integer start of the interval: "))
E = int(input("The integer end of the interval: "))
step = float(input("The value of the step between plots: "))

x = np.arange(S, E, step)
y = f(x)
graph_maximum = max(f(x))


random_x = S + (E - S)*np.random.random(N)
random_y = graph_maximum*np.random.random(N)

below_the_curve = np.where(random_y < f(random_x))
above_the_curve = np.where(random_y >= f(random_x))

Below_the_curve = plt.scatter(random_x[below_the_curve], random_y[below_the_curve], color="blue")
Above_the_curve = plt.scatter(random_x[above_the_curve], random_y[above_the_curve], color="red")


plt.plot(x, y, color="green")

plt.xlabel("X")
plt.ylabel("F(X)")

num_of_points_under_the_curve = len(below_the_curve[0])
num_of_points_in_the_rectangle = len(below_the_curve[0]) + len(above_the_curve[0])

proportion_of_the_area = num_of_points_under_the_curve / num_of_points_in_the_rectangle
The_area_under_the_curve = proportion_of_the_area * (graph_maximum * (E - S))

print(f"The area under the curve: {The_area_under_the_curve}")
plt.show()
