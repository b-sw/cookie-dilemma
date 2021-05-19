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


def plot_single_run_properties(data, algorithm, title, y_label, graph_filename, colour):
    if algorithm == 'es':
        plot_graph(data, title, "Number of evals", y_label, graph_filename, colour)
    else:
        plot_graph(data, title, "Number of evals", y_label, graph_filename, colour)


def print_loading_bar(i, total):
    done = '#' * i
    left = '-' * (total - i)
    print('\rOptimizing: ' + str(round((i / total) * 100, 2)) + '% ' + '[' + done + left + ']', end='')
