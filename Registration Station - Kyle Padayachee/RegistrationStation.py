"""
Registration Station project
"""

def read_file():

    """
    Read and return contents of text file
    """
    with open('bootcampers.txt', 'r') as file_reader:
        file_contents = file_reader.readlines()
    print(file_contents)
    return file_contents

def input_user_name(file_contents):
    """
    Takes username as input
    """
    user_name = input("Enter username: ")
    if user_name in file_contents:
        print(file_contents.readline())
    else:
        print("Username not found.")


def correct_or_incorrect():

    """
    Prompt to ask if details are correct or not
    @return correct or incorrect
    """
    answer = input("Are the details correct? Y/N: ").lower()
    if answer == "y":
        return "correct"
    elif answer == "n":
        return "incorrect"
    else:
        print("Incorrect submission given")


def correct_details():

    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """
    username = input("Enter username: ")
    date = input("Enter cohort year: ")
    location = input("Enter campus name: ")
    prior_experience = input("Do you have prior coding experience? Y/N").lower()
    if prior_experience == "y":
        experience = "Prior Experience"
    elif prior_experience == "n":
        experience = "No Prior Experience"

    with open('bootcampers.txt', 'a') as f:
        f.write(f"{username} - {date} - {location} - {experience}")

def get_file_contents():

    """Return desired text file"""
    


def find_username(file_name):

    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    


if __name__ == "__main__":
    registrations_file = read_file()
    information = input_user_name(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()