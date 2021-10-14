import  matplotlib.pyplot as plt

import Classi.Plotter

plt = Classi.Plotter.Plotter()

plt.load_axis([1, 2, 3, 4, 5], [10, 12, 32, 4, 33])

plt.plot_setting(True, True, 'Prova 1', 'ID', 'numero', 'Serie 1')

plt.load_axis([11, 22, 33, 44, 55], [110, 112, 132, 14, 33])

plt.plot_setting(False, False, 'Prova 2', 'ID', 'numero', 'Serie 2')

plt.show_graph()


"""
plt.figure(1)


# x axis values
x = [1, 2, 3]
# corresponding y axis values
y = [2, 4, 1]

# plotting the points
plt.plot(x, y, label='line 1')

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

plt.legend()

# function to show the plot
plt.show()

plt.close(1)
"""