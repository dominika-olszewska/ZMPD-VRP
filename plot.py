from __future__ import print_function
import matplotlib.pyplot as plt
from itertools import cycle


def create_initial_plot(points, name):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])

    plt.plot(x, y, 'ro')

    plt.savefig('static\img\plot_img_' + 'initial_' + name + '.png', bbox_inches='tight')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # plt.title('Initial data')
    plt.clf()


def create_plot(points, routes, vehicle_distance, name):
    x = []
    y = []
    trigger = True
    vehicles = list(range(1, len(vehicle_distance) + 1))
    index = 0
    for point in points:
        x.append(point[0])
        y.append(point[1])
    if (points[0]):
        plt.plot(x, y, 'ro')
    else:
        plt.plot(x, y, 'ko')
    generate_color = cycle('bgrcmyk')
    for route in routes:
        color = next(generate_color)
        for i in range(len(route)):
            if i is not len(route) - 1:
                x1, x2 = x[route[i]], x[route[i + 1]]
                y1, y2 = y[route[i]], y[route[i + 1]]
                if trigger:
                    plt.plot([x1, x2], [y1, y2], color + '-', label='Vehicle {}'.format(vehicles[index]))
                    index += 1
                    trigger = False
                else:
                    plt.plot([x1, x2], [y1, y2], color + '-')
        trigger = True
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # plt.title(name)
    plt.savefig('static\img\plot_img_' + name + '.png', bbox_inches='tight')
    plt.clf()
