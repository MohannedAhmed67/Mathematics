import numpy as np
import matplotlib.pyplot as plt

#You can put here the function you want to calculate the area under its curve.
def f(z):
    return z**np.cos(z)+2

#Asking the user for the desired number of points, the start and the end of the interval.
N = int(input("The number of points to be randomised: "))
S = float(input("The start of the interval: "))
E = float(input("The end of the interval: "))
step = float(input("The value of the step between plots: "))

#The plots of the main function.
x = np.arange(S, E, step)
y = f(x)
graph_maximum = max(f(x))

#Generating random variables between 0 and 1 and then converting them to the proper numbers of the graph to be fit with the scale of the curve.
random_x = S + (E - S)*np.random.random(N)
random_y = graph_maximum*np.random.random(N)

#Defining the points below and above the curve.
below_the_curve = np.where(random_y < f(random_x))
above_the_curve = np.where(random_y >= f(random_x))

#Plotting the points above and under the curve.
Below_the_curve = plt.scatter(random_x[below_the_curve], random_y[below_the_curve], color="blue")
Above_the_curve = plt.scatter(random_x[above_the_curve], random_y[above_the_curve], color="red")

#Graphing the main function.
plt.plot(x, y, color="green")

#The x-axis and the y-axis.
plt.xlabel("X")
plt.ylabel("F(X)")

#Calculating the ratio between the number of points under the curve and the number of points inside the rectangle.
num_of_points_under_the_curve = len(below_the_curve[0])
num_of_points_in_the_rectangle = len(below_the_curve[0]) + len(above_the_curve[0])

#Multiplying this ratio by the area of the rectangle to get the area under the curve.
proportion_of_the_area = num_of_points_under_the_curve / num_of_points_in_the_rectangle
The_area_under_the_curve = proportion_of_the_area * (graph_maximum * (E - S))

print(f"The area under the curve: {The_area_under_the_curve}")
plt.show()
