def parse_file(file_string, set, vehicles):
    print('SET: ', set, vehicles)
    if set == 'LIU-ET-AL':
        file_string_split = file_string.split('\r\n')
    elif set == 'SET-E' or set == 'SET-B' or set == 'SET-A' or set == 'SET-F' or set == 'SET-M':
        file_string_split = file_string.split('\n')
    elif set == 'UCHOA' or set == "ARNOLD":
        without_tab = file_string.replace('\t', ' ')
        file_string_split = without_tab.split('\r\n')
    print('converted file', file_string_split)
    for i in file_string_split:
        if "NAME" in i:
            name = i.split(": ", 1)[1]
        if "CAPACITY" in i:
            capacity = int(i.split(": ", 1)[1])
        if "DIMENSION" in i:
            dimension = int(i.split(": ", 1)[1])
        if "NODE_COORD_SECTION" in i:
            index_coord = file_string_split.index(i) + 1
        if "DEMAND_SECTION" in i:
            index_demand = file_string_split.index(i) + 1
        if "trucks: " in i and (set == 'SET-E' or set == "SET-B" or set == "SET-A" or set == 'SET-F' or set == 'SET-M'):
            vehicles = i.split("trucks: ", 1)[1][:2]
            without_coma = vehicles.replace(',', '')
            print('trucks str', without_coma)
            vehicles = int(without_coma)
        if set == 'LIU-ET-AL' or set == 'UCHOA' or set == 'ARNOLD':
            vehicles = int(vehicles)

    capacity = [capacity] * vehicles
    points_string = []
    demands_string = []
    if set != 'LIU-ET-AL':
        points_string = file_string_split[index_coord:index_coord + dimension]
        demands_string = file_string_split[index_demand:index_demand + dimension]
    else:
        points_string = file_string_split[index_coord:index_coord + dimension - 1]
        demands_string = file_string_split[index_demand:index_demand + dimension - 1]

    point_int = []
    for point in points_string:
        point = point.split(" ")
        point_int.append((float(point[1]), float(point[2])))

    demand_int = []
    for demand in demands_string:
        demand = demand.split(" ")
        demand_int.append((int(demand[1])))

    print('capacity', capacity)
    print('dimension', dimension)
    print('point_int', point_int)
    print('demand_int', demand_int)
    print('vehicles', vehicles)
    return name, capacity, dimension, point_int, demand_int, vehicles
