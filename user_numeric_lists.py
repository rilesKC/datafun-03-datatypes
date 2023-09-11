"""
Matt Riley
9/10/2023

"""

# import some standard modules first - how many can you make use of?
import math
import statistics

# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................

# Call the setup_logger function
logger, logname = setup_logger(__file__)

# define a variable with some univariant data
# (one varabile, many readings)
list1 = [
    17, 29, 34, 36, 62, 69, 116, 141, 149, 158, 166, 180, 199, 226, 251, 256, 282, 294, 313, 352
]

listx = [
    8, 321, 748, 834, 1118, 1224, 1630, 2111, 2233, 2313
]

listy = [
    61, 63, 80, 82, 84, 103, 105, 115, 120, 148
]

# Define some custom functions

def standard_statistic_functions():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"list1: {list1}")

    # Descriptive: Averages and measures of central tendency
    # Use statisttics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    logger.info(f"mean: {mean:.2f}")
    logger.info(f"median: {median:.2f}")
    logger.info(f"mode: {mode:.2f}")

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"stdev: {stdev:.2f}")
    logger.info(f"variance: {variance:.2f}")


def list_correlation_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statisttics module to get correlation between list1 and list2

    correlationxy = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationxy:.2f}")

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope:.2f}x + {intercept:.2f}")

    # Predict the y value for a given x value outside the range of the data

    #x_max = max(listx)
    newx = 15  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info(f"We predict that when x = {newx}, y will be about {newy:.2f}")


def list_built_in_functions():
    # Calcuate the max and min wait times
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Wait times list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list:.2f}")

    set_list = set(list1)
    logger.info(f"Set of wait times: {set_list}")

    # Return a new list soreted in ascending order
    asc_wait_times = sorted(list1)
    logger.info(f"Wait times sorted ascending: {asc_wait_times}")

    # Return a new list soreted in descending order
    desc_wait_times = sorted(list1, reverse=True)
    logger.info(f"Wait times sorted descending: {desc_wait_times}")


def list_methods():
    """This function illustrates methods that can be called on a list"""

    # append an item to the end of the list
    lst = [11, 12, 13]
    lst.append(5)

    # extend the list with another list
    lst.extend([14, 15, 16])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 22
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 5
    lst.remove(item_to_remove)

    # Count how many times 2 appears in the list
    ct_of_2 = list1.count(2)
    logger.info(f"The number 2 appears {ct_of_2} times in the list.")

    # Sort the list in ascending order using the sort() method
    list1.sort()
    logger.info(f"Wait times sorted ascending: {list1}")

    # Sort the list in descending order using the sort() method
    list1.sort(reverse=True)
    logger.info(f"Wait times sorted descending: {list1}")

    # Copy the list to a new list
    new_lst = list1.copy()
    logger.info(f"New wait times is: {new_lst}")

    # Remove the first item from the new list
    first = new_lst.pop(0)
    logger.info(f"Popped the first (index=0): {first} and now, new_scores is: {new_lst}")

    # Remove the last item from the new list
    last = new_lst.pop(-1)
    logger.info(f"Popped the last (index=-1): {last} and now, new_scores is: {new_lst}")


def list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info(f"Wait times list: {list1}")

    waits_over_100 = list(filter(lambda x: x > 100, list1))
    logger.info(f"Wait times over 100 minutes: {waits_over_100}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its cuberoot
    cubed_waits = list(map(math.cbrt, list1))
    logger.info(f"Cuberoot of wait times: {cubed_waits}")

    # remember to cast the result to a list (using square brackets)
    list_value = 5
    volume = (list_value**3)
    logger.info(f"Volume of a cube with sides equal to {list_value} is: {volume}")


def list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info(f"Wait times list: {list1}")

    # Filter the new list to only include wait times less than 60
    wait_times_under_60 = [x for x in list1 if x < 60]
    logger.info(f"Wait times under 60: {wait_times_under_60}")

    # Map each element to its triple
    tripled_wait_times = [x * 3 for x in list1]
    logger.info(f"Tripled wait times: {tripled_wait_times}")

    # Map each element to its value in hours
    wait_times_in_hours = ["%.2f" % (x / 60) for x in list1]
    logger.info(f"Wait times in hours: {wait_times_in_hours}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    standard_statistic_functions()
    list_correlation_prediction()
    list_built_in_functions()
    list_methods()
    list_transformations()
    list_comprehensions()

    show_log()

