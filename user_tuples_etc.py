"""
Matt Riley
9/10/2023

"""

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Create some tuples
hospital_names = ("Children's Mercy", "Mayo Clinic", "Cedars Sinai", "Cook County", "Lenox Hill")
hospital_cities = ("Kansas City", "Rochester", "Los Angeles", "Chicago", "New York")

logger.info(f"Hospital Names = {hospital_names}")
logger.info(f"Hospital Cities = {hospital_cities}")

def sets_etc():
    hospital_names2 = {"Children's Mercy", "Mayo Clinic", "Cedars Sinai", "Cook County", "Lenox Hill"}
    hospital_cities2 = {"Kansas City", "Rochester", "Los Angeles", "Chicago", "New York"}

    logger.info(f"{hospital_names2 = }")
    logger.info(f"{hospital_cities2 = }")

    union_hospitals = hospital_names2 | hospital_cities2
    logger.info(f"Union is: {union_hospitals}")

    intersection_hospitals = hospital_names2 & hospital_cities2
    logger.info(f"Intersection is: {intersection_hospitals}")


def dictionaries_etc():
    doctor_dict = {"Name": "Wilson", "Specialty": "Cardiology", "School": "Harvard"}
    surgeon_dict = {"Name": "Brown", "Specialty": "Orthopaedics", "School": "Stanford"}

    logger.info(f"{doctor_dict = }")
    logger.info(f"{surgeon_dict = }")

    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info(f"Using text_simple.txt, the word_counts_dict = {word_counts_dict}")

    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    logger.info("Using text_simple.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")
    

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
    sets_etc()
    dictionaries_etc()

    show_log()