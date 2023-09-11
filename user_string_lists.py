"""
Matt Riley
9/10/2023

"""

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Define a string list
list_patients = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

# Define a list of outcomes
list_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Define a list of calls
list_doctors = ["Spock", "Wilken", "Tom", "Strange", "Zhivago", "Who"]

# Define a list for rock, paper, scissors
list_departments = ["Emergency", "Radiology", "Cardiology", "Pharmacy", "Oncology"]

# Define a list of colors
list_nurses = ["Sanger", "Nightingale", "Barton", "Mahoney", "Whitman", "Henderson"]

# reusable functions next

def built_in_funtions():
    logger.info("Calling built_in_function()")

    logger.info(f"There are {len(list_patients)} patients on the schedule today.")
    logger.info(f"There list of unique departments {set(list_departments)}.")

    doctors_and_nurses = list(zip(list_doctors, list_nurses))
    logger.info(f"The combined list of doctors and nurses is: {doctors_and_nurses}.")


def random_choice():
    """Create a random sentence from our pre-defined lists"""
    on_call = random.choice(list_doctors)
    logger.info(f"Today's on-call physician is Dr. {on_call}.")

    logger.info("Calling random_choice()")

    # Create a random sentence
    sentence = (
        f"Dr. {random.choice(list_doctors)} will be in {random.choice(list_departments)} "
        f"on {random.choice(list_days)} with nurse {random.choice(list_nurses)} "
        f"to see {random.choice(list_patients)}."
    )

    logger.info(f"Random sentence: {sentence}")


def get_unique_words():
    """Read in text_juliuscaesar.txt and process it"""
    logger.info("Calling get_unique_words() for Julius Caesar")

    # read in juliuscaesar to get a list of words
    with open("text_juliuscaesar.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)
        logger.info(f"There are {unique_word_ct} unique words in the file.")


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
    built_in_funtions()
    random_choice()
    get_unique_words()

    show_log()


