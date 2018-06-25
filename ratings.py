"""Restaurant rating lister."""
import sys


# put your code here
def get_ratings_from_file(filename):
    """Gets restaurant ratings from file and returns it in a dictionary"""

    ratings = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            raw_rating_data = line.split(":")
            ratings[raw_rating_data[0]] = raw_rating_data[1]
    return ratings


def print_ratings_alphabetically(ratings_dictionary):
    """Takes a restaurant ratings dictionary and prints it alphabetically"""

    alpha_dictionary = sorted(ratings_dictionary)
    for restaurant in alpha_dictionary:
        print(f"{restaurant} is rated {ratings_dictionary[restaurant]} stars")


def add_rating():
    """Asks user for restaurant name and rating, appends to score.txt"""
    restaurant_name = input("Please enter the restaurant name: ").title()
    if restaurant_name in get_ratings_from_file("scores.txt"):
        print(f"{restaurant_name} is already rated")
        return
    restaurant_rating = input("Please enter the score for the restaurant: ")
    try:
        restaurant_rating = int(restaurant_rating)
    except ValueError:
        print("That was not a number, try again later")
        return

    new_line = f"{restaurant_name}:{restaurant_rating}\n"

    # write into file
    with open("scores.txt", "a") as file:
        file.write(new_line)


# print_ratings_alphabetically(get_ratings_from_file(sys.argv[1]))
while True:

    print("1. Get restaurant ratings in alphabetical order")
    print("2. Add restaurant rating")
    print("Type q or quit to end program")
    user_choice = input(">").lower()
    if user_choice == "q" or user_choice == "quit":
        break
    if user_choice == "1":
        print_ratings_alphabetically(get_ratings_from_file("scores.txt"))
    elif user_choice == "2":
        add_rating()
    else:
        print("Choose an actual option, jerk")
