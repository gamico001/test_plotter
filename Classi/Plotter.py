"""
Superenalotto
-------------

Classe e metodi per la rappresentazione grafica di una serie.
Usata per la rappresentazione grafica della Regressione su una serie di dati X/Y

"""

import matplotlib.pyplot as plotter

class Plotter:
    """
    Classe per la gestione delle istruzioni per la rappresentazione grafica su assi cartesiani X e Y
    """

    def __init__(self):
        self.x_axsis = []
        self.y_axis = []
        self.error = 0
        self.id_figure = 0

    def show_graph(self):
        plotter.show()

    def load_axis(self, x_axis, y_axis):
        """
        Load list for X & Y data
        :param x_axis: X series
        :param y_axis: Y series
        :return:
        """
        print("lista X:", type(x_axis), ' data:', x_axis)
        print("lista Y:", type(y_axis), ' data:', y_axis)

        try:
            self.x_axsis = x_axis
            self.y_axis = y_axis
            self.error = 0
        except Exception as error:
            self.error = 1
            print("errore in load:", error)

        return self.error

    def plot_setting(self, reset_figure=False, new_figure=False, title='Titolo', x_label='X', y_label='Y', label_legend='linea1'):
        try:
            if reset_figure:  # if reset --> clear all figure and start with clear graph
                plotter.figure().clear()
                plotter.close()
                plotter.cla()
                plotter.clf()

            if new_figure:
                self.id_figure = self.id_figure + 1
                plotter.figure(self.id_figure)

            plotter.title(title)
            plotter.xlabel(x_label)
            plotter.ylabel(y_label)
            plotter.plot(self.x_axsis, self.y_axis, label=label_legend)
            plotter.legend()
            self.error = 0
        except Exception as e:
            self.error = 1
            print("errore in plot:", e)

        return self.error


