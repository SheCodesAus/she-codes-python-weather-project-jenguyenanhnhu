from datetime import datetime
from itertools import tee
import statistics
import csv

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def convert_date(iso_string):
    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")
# print(convert_date("2021-07-02T07:00:00+08:00"))
    # """Converts an ISO formatted date into a human readable format.
    # Args:
    #     iso_string: An ISO date string.
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    # pass


def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"
# print(format_temperature(3))
    # """Takes a temperature and returns it in string format with the degrees
    #     and Celcius symbols.
    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees Celsius."
    # """


def convert_f_to_c(temp_in_fahrenheit):
    if isinstance(temp_in_fahrenheit, float):
        return round((int(temp_in_fahrenheit) - 32)/1.8)
    else:
        return round((int(temp_in_fahrenheit) - 32)/1.8, 1)
# print(convert_f_to_c(0))
    # """Converts an temperature from fahrenheit to Celsius.
    # Args:
    #     temp_in_fahrenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celsius, rounded to 1dp.
    # """
    # pass

def calculate_mean(weather_data):
    return statistics.mean(map(float(weather_data)))
# print(calculate_mean([49, 57, 56, 55, 53]))
    # """Calculates the mean value from a list of numbers.
    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    # pass


def load_data_from_csv(csv_file):
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file)
        a = []
        for line in reader: 
            if line != []:
                b = [line[0], int(line[1]), int(line[2])]
                a.append(b)
        return a
# print(load_data_from_csv("tests/data/example_two.csv"))
    # """Reads a csv file and stores the data in a list.
    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    # pass


# def find_min(weather_data):
#     c = [i for i in weather_data[::-1]]
#     find_min = min(map(float, c)), weather_data.index(min(map(float, c)))
#     return find_min
#     # if min(x for x in weather_data if weather_data.count(x) > 1):
#     #     return min(map(float, weather_data[c])), weather_data.index(min(map(float, weather_data[c])))
#     # else:
#     #     return min(map(float, weather_data)), weather_data.index(min(map(float, weather_data)))
# print(find_min([3, 5, 0, 9, 0]))


def find_min(weather_data):
    if weather_data:
        min_val = min(weather_data)
        for i in range(len(weather_data)):
            if weather_data[i] == min_val:
                idx = i
        return float(min_val), idx
    else:
        return ()
    # """Calculates the minimum value in a list of numbers.
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """
    # pass

def find_max(weather_data):
    if weather_data:
        max_val = max(weather_data)
        for i in range(len(weather_data)):
            if weather_data[i] == max_val:
                idx = i
        return float(max_val), idx
    else:
        return ()
    # """Calculates the maximum value in a list of numbers.
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """
    # pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
