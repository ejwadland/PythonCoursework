import random
import math



def read_cities(file_name):

    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    cities_tuple = [tuple(word.strip('\n').split('\t')) for word in open(file_name, 'r').readlines()]

    return cities_tuple



def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    print_map = []

    for element in road_map:
        print_map.append((element [0], element[1], (round(float(element[2]), 2), round(float(element[3]), 2))))

    print(print_map)



def city_distance(city1, city2):

    '''
    Euclidean distance between two cities (x1, x2, y1, y2)
    '''

    x1 = float(city1[2])
    x2 = float(city2[2])
    y1 = float(city1[3])
    y2 = float(city2[3])


    euc_distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return euc_distance

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total = 0
    for i in range(len(road_map)):
        city1 = road_map[i]
        city2 = road_map[(i+1) % len(road_map)]
        total +=  city_distance(city1, city2)
    return total



def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_road_map = road_map
    new_total_distance = 0

    if index1 != index2:

        original_index = new_road_map[index1]

        new_road_map[index1] = new_road_map[index2]

        new_road_map[index2] = original_index

        new_total_distance = compute_total_distance(new_road_map)

    return new_road_map, new_total_distance



def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """

    shifted_road_map = [road_map[-1]] + road_map[:-1]
    return shifted_road_map



def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    shortest_distance = compute_total_distance(road_map)
    shortest_rm = road_map

    for n in range(10000):
        current_rm = shift_cities(shortest_rm)
        index1 = int(random.random() * len(road_map))
        index2 = int(random.random() * len(road_map))
        result = swap_cities(current_rm, index1, index2)
        current_rm = result[0]
        new_distance = result[1]

        if shortest_distance > new_distance:
            shortest_distance = new_distance
            shortest_rm = current_rm

    return shortest_rm




def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    total_dis = 0

    for i in range(len(road_map)):
        city1 = road_map[i]
        city2 = road_map[(i+1) % len(road_map)]
        distance = city_distance(city1, city2)
        print(city1[1], "--->", city2[1], "    ", distance)
        total_dis += distance

    print(total_dis)






def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.

    """

    road_map = read_cities('city-data.txt')
    print_cities(road_map)
    shortest_rm = find_best_cycle(road_map)
    print_map(shortest_rm)













if __name__ == "__main__":  # keep this in
    main()


