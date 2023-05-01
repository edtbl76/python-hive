#! /usr/bin/env python3

from graph_search import bfs, dfs
from vancouver_metro import vancouver_metro
from vancouver_landmarks import vancouver_landmarks
from landmark_choices import landmark_choices


# Setup
landmark_string = ""
stations_under_construction = ['Burnaby Lake', 'Central Park']
for letter, landmark in landmark_choices.items():
    landmark_string += f'{letter} - {landmark}\n'


# Helper Functions
def greet():
    print('Hello and welcome to Vancouver SkyRoute')
    print(f"We'll help you find the shortest route between the following Vancouver Landmarks:\n {landmark_string}")


def goodbye():
    print("Thanks for using Vancouver SkyRoute!")


def set_start_and_end(start, end):
    if start is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for destination or "
                             "'b' for both': ")

        if change_point == 'b':
            start = get_start()
            end = get_end()
        elif change_point == 'o':
            start = get_start()
        elif change_point == 'd':
            end = get_end()
        else:
            print("Invalid Selection: You can enter 'o' for 'origin', 'd' for destination or 'b' for both': ")
            set_start_and_end(start, end)
    else:
        start = get_start()
        end = get_end()
    return start, end


def get_start():
    start_selection = input("Where are you coming from?\nType in the corresponding letter: ")

    if start_selection in landmark_choices.keys():
        start = landmark_choices[start_selection]
        return start
    else:
        print("Sorry, that's not an available landmark. Please try again...")
        get_start()


def get_end():
    end_selection = input("Where are you going?\nType in the corresponding letter: ")

    if end_selection in landmark_choices.keys():
        end = landmark_choices[end_selection]
        return end
    else:
        print("Sorry, that's not an available landmark. Please try again...")
        get_end()


def new_route(start=None, end=None):
    start, end = set_start_and_end(start, end)
    shortest_route = get_route(start, end)
    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print(f'The shortest metropolitan route from {start} to {end} is \n{shortest_route_string}')
    else:
        print(f'Unfortunately, due to maintenance, there is currently no path between {start} and {end}.')
        print("We sincerely apologize for the inconvenience.")

    again = input("Would you like to see another route? Enter (y/n): ")
    if again == 'y':
        show_landmarks()
        new_route(start, end)


def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter (y/n): ")
    if see_landmarks:
        print(landmark_string)



def get_route(start, end):
    start_stations = vancouver_landmarks[start]
    end_stations = vancouver_landmarks[end]
    routes = []

    for start_station in start_stations:
        for end_station in end_stations:
            # Additional code to handle stations under construction
            metro_system = get_active_stations() if stations_under_construction else vancouver_metro

            # Before BFS, we use DFS to see if a route exists. (Short circuit BFS)
            if (len(stations_under_construction)) > 0:
                possible_route = dfs(metro_system, start_station, end_station)
                if not possible_route:
                    return None

            route = bfs(metro_system, start_station, end_station)
            if route is not None:
                routes.append(route)
    shortest_route = min(routes, key=len)
    return shortest_route


def get_active_stations():
    updated_metro = vancouver_metro
    for inactive_station in stations_under_construction:
        for current_station, neighbor_stations in vancouver_metro.items():
            if current_station is not inactive_station:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])

    return updated_metro


# MAIN
def skyroute():
    greet()
    new_route()
    goodbye()



skyroute()