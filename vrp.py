"""Capacited Vehicles Routing Problem (CVRP)."""

from __future__ import print_function

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

import plot
import data as modelData
import printSolution as print
import getRoutes

def cvrp(data, set, trucks):
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data, name = modelData.create_data_model(data, set, trucks)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # initial plot
    plot.create_initial_plot(data['points'], name)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    # search_parameters.first_solution_strategy = (
    #     routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.AUTOMATIC)
    search_parameters.time_limit.seconds = 20

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution.
    if assignment:
        vehicle_distance, vehicle_load, text = print.print_solution(data, manager, routing, assignment)
    routes = getRoutes.get_routes(manager, routing, assignment, data['num_vehicles'])
    # Display the routes.
    route_arr = print.print_routes(routes)
    plot.create_plot(data['points'], routes, vehicle_distance, name)
    return vehicle_distance, vehicle_load, text, name, route_arr


