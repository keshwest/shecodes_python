import csv
from datetime import datetime
from unittest import result

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
    # for i in range(0, len(weather_data)):
    #     weather_data[i] = float(weather_data[i])
    # return sum(weather_data) / len(weather_data)
    sum = 0
    for temp in weather_data:
        sum = sum + float(temp)
        mean = sum / len(weather_data)
    return mean
    #Correct!

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, line in enumerate(csv_reader):
            if line != [] and index != 0:
                data.append([line[0],int(line[1]),int(line[2])])
    return data
    #correct!


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i]) # turn str into float 
    if len(weather_data) == 0:
        return ()
    temp_min = min(weather_data) # find min value
    position = weather_data.reverse() # reverse list
    position = len(weather_data) - weather_data.index(temp_min) -1 #i dentify position
    return temp_min, position
    #Correct!


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i]) # turn str into 
    if len(weather_data) == 0:
        return ()
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
    count = 0
    min_temp = []
    max_temp = []
    date_time = []

    for index, item in enumerate(weather_data):
        if len(weather_data) == 0:
            return ()
        if index != []:
            count += 1
            date_time.append(item[0])
            min_temp.append(item[1])
            max_temp.append(item[2])
            
    min_temps, index_date_min = find_min(min_temp)
    max_temps, index_date_max = find_max(max_temp)

    min_temp_c = convert_f_to_c(str(min_temps))
    max_temp_c = convert_f_to_c(str(max_temps))

    mean_min_c = convert_f_to_c(calculate_mean(min_temp))
    mean_max_c = convert_f_to_c(calculate_mean(max_temp))

    date_min = date_time[index_date_min]
    date_max = date_time[index_date_max]

    result = ""
    result += f"{count} Day Overview\n"
    result += f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {convert_date(date_min)}.\n" 
    result += f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {convert_date(date_max)}.\n"
    result += f"  The average low this week is {format_temperature(mean_min_c)}.\n"
    result += f"  The average high this week is {format_temperature(mean_max_c)}.\n"
    
    return result


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    dash = "----"
    result = ""
    for item in weather_data:
        result += f"{dash} {convert_date(item[0])} {dash}\n"
        result += f"  Minimum Temperature: {format_temperature(convert_f_to_c(item[1]))}\n" 
        result += f"  Maximum Temperature: {format_temperature(convert_f_to_c(item[2]))}\n\n"

    return result

#     ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 ----
#   Minimum Temperature: 13.9°C
#   Maximum Temperature: 20.0°C

# ---- Sunday 04 July 2021 ----
#   Minimum Temperature: 13.3°C
#   Maximum Temperature: 16.7°C

# ---- Monday 05 July 2021 ----
#   Minimum Temperature: 12.8°C
#   Maximum Temperature: 16.1°C

# ---- Tuesday 06 July 2021 ----
#   Minimum Temperature: 11.7°C
#   Maximum Temperature: 16.7°C
