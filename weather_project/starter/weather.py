import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):  
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    format_date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return format_date.strftime("%A %d %B %Y")
    #Correct!


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit = float(temp_in_farenheit)
    caculate_temp = (temp_in_farenheit - 32) * (5/9)
    return (round(caculate_temp, 1))
    #Correct!

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i])
    return sum(weather_data) / len(weather_data)
    #Correct!

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_reader = csv.reader(csv_file)
    list_csv = []
    return list_csv
    #I have no idea whats going on


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i]) # turn str into float
    temp_min = min(weather_data) # find min value
    position = weather_data.reverse() # reverse list
    position = len(weather_data) - weather_data.index(temp_min) -1 #i dentify position
    return temp_min, position
    
    #ValueError: min() arg is an empty sequence


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i]) # turn str into float
    temp_max = max(weather_data) # find min value
    position = weather_data.reverse() # reverse list
    position = len(weather_data) - weather_data.index(temp_max) -1 #i dentify position
    return temp_max, position

    #ValueError: max() arg is an empty sequence


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
