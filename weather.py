from datetime import datetime
import statistics
import csv

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def convert_date(iso_string):
    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")
    # """Converts an ISO formatted date into a human readable format.
    # Args:
    #     iso_string: An ISO date string.
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    # pass


def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"
    # """Takes a temperature and returns it in string format with the degrees
    #     and Celcius symbols.
    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees Celsius."
    # """


def convert_f_to_c(temp_in_fahrenheit):
    return round((float(temp_in_fahrenheit) - 32)/1.8, 1) 
    # """Converts an temperature from fahrenheit to Celsius.
    # Args:
    #     temp_in_fahrenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celsius, rounded to 1dp.
    # """
    # pass

def calculate_mean(weather_data):
    return statistics.mean(map(float,weather_data))
    # """Calculates the mean value from a list of numbers.
    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    # pass


def load_data_from_csv(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(file)
        list_of_lists = []
        for line in reader: 
            if line != []:
                list = [line[0], int(line[1]), int(line[2])]
                list_of_lists.append(list)
        return list_of_lists
    # """Reads a csv file and stores the data in a list.
    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    # pass


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
    min_value, min_pos = find_min(min_list)
    min_temp = convert_f_to_c(min_value)
    min_date = convert_date(weather_data[min_pos][0])
    max_value, max_pos = find_max(max_list)
    max_temp = convert_f_to_c(max_value)
    max_date = convert_date(weather_data[max_pos][0])
    min_mean_value = calculate_mean(min_list)
    min_mean = convert_f_to_c(min_mean_value)
    max_mean_value = calculate_mean(max_list)
    max_mean = convert_f_to_c(max_mean_value)
    return f"{n} Day Overview\n  The lowest temperature will be {min_temp}{DEGREE_SYMBOL}, and will occur on {min_date}.\n  The highest temperature will be {max_temp}{DEGREE_SYMBOL}, and will occur on {max_date}.\n  The average low this week is {min_mean}{DEGREE_SYMBOL}.\n  The average high this week is {max_mean}{DEGREE_SYMBOL}.\n"
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
        date = convert_date(value[0])
        min_temp = convert_f_to_c(value[1])
        max_temp = convert_f_to_c(value[2])
        result += f"---- {date} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n"
    return result
    # """Outputs a daily summary for the given weather data.
    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    # pass
