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
    return statistics.mean(map(float,weather_data))
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
                index = i
        return float(min_val), index
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
                index = i
        return float(max_val), index
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
    n = len(weather_data)
    date_list = []
    min_list = []
    max_list = []
    for value in weather_data:
        date_list.append(value[0])
        min_list.append(value[1])
        max_list.append(value[2])
    min_value = min(min_list)
    min_temp = round((min_value - 32)/1.8, 1)
    for a in range(len(min_list)):
        if min_list[a]==min_value:
            min_date = datetime.fromisoformat(date_list[a]).strftime("%A %d %B %Y")
    max_value = max(max_list)
    max_temp = round((max_value - 32)/1.8, 1)
    for b in range(len(max_list)):
        if max_list[b]==max_value:
            max_date = datetime.fromisoformat(date_list[b]).strftime("%A %d %B %Y")
    min_mean_value = statistics.mean(map(float,min_list))
    min_mean = round((min_mean_value - 32)/1.8, 1)
    max_mean_value = statistics.mean(map(float,max_list))
    max_mean = round((max_mean_value - 32)/1.8, 1)
    return f"{n} Day Overview\n  The lowest temperature will be {min_temp}{DEGREE_SYMBOL}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}{DEGREE_SYMBOL}, and will occur on {max_date}.\n  The average low this week is {min_mean}{DEGREE_SYMBOL}.\n  The average high this week is {max_mean}{DEGREE_SYMBOL}.\n"
print(generate_summary([["2020-06-19T07:00:00+08:00", 47, 46],
    ["2020-06-20T07:00:00+08:00", 51, 67],
    ["2020-06-21T07:00:00+08:00", 58, 72],
    ["2020-06-22T07:00:00+08:00", 59, 71],
    ["2020-06-23T07:00:00+08:00", 52, 71],
    ["2020-06-24T07:00:00+08:00", 52, 67],
    ["2020-06-25T07:00:00+08:00", 48, 66],
    ["2020-06-26T07:00:00+08:00", 53, 66]]
))
    # """Outputs a summary for the given weather data.
    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    # pass


def generate_daily_summary(weather_data):
    result = ""
    for value in weather_data:
        date = datetime.fromisoformat(value[0]).strftime("%A %d %B %Y")
        min_temp = round((int(value[1]) - 32)/1.8, 1)
        max_temp = round((int(value[2]) - 32)/1.8, 1)
        result += f"---- {date} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n"
    return result
    # """Outputs a daily summary for the given weather data.
    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    # pass
