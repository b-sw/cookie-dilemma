"""
    Name:
    Purpose:

    @author Bartosz Świtalski, Marcel Kawski

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
import matplotlib.pyplot as plt


def plot_graph(data, title, x_label, y_label, graph_filename, colour):
    fig, ax = plt.subplots()

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_yscale('log')

    ax.plot(data[0], data[1], colour + '.')

    plt.savefig('output/' + graph_filename + '.jpg')


def plot_single_run_properties(data, algorithm):
    if algorithm == 'es':
        plot_graph(data, "Single run best fits", "Number of evals", "Best fit", "esBF", 'g')
        plot_graph(data, "Single run expected fits", "Number of evals", "Expected fit", "esEF", 'r')
    else:
        plot_graph(data, "Single run best fits", "Number of evals", "Best fit", "gaBF", 'g')
        plot_graph(data, "Single run expected fits", "Number of evals", "Expected fit", "gaEF", 'r')
