"""Vehicles Routing Problem (VRP)."""

from __future__ import print_function
import parseData
from urllib.request import urlopen



def get_string_from_website(website):
    url = website
    output = urlopen(url).read()
    file_string = (output.decode('utf-8'))
    return file_string


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_distance_matrix(points):
    distance_vector = []
    distance_matrix = []
    for point in points:
        for i in range(len(points)):
            distance_vector.append(get_distance(point[0], point[1], points[i][0], points[i][1]))
        distance_matrix.append(distance_vector)
        distance_vector = []
    return distance_matrix


def create_data_model(file_string, set, vehicles):
    """Stores the data for the problem."""
    data = {}
    name, capacity, dimension, points, demands, vehicles = parseData.parse_file(file_string, set, vehicles)
    distance_matrix = get_distance_matrix(points)
    data['distance_matrix'] = distance_matrix
    data['demands'] = demands
    data['vehicle_capacities'] = capacity
    data['num_vehicles'] = vehicles
    data['depot'] = 0
    data['points'] = points
    return data, name

