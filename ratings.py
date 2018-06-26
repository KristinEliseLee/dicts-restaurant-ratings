"""Restaurant rating lister."""
import sys
import random
import os


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
        print(f"{restaurant} is rated {ratings_dictionary[restaurant]} star(s)")


def add_rating():
    """Asks user for restaurant name and rating, appends to score.txt"""
    ratings_dictionary = get_ratings_from_file(chosen_file)
    restaurant_name = input("Please enter the restaurant name: ").title()
    if restaurant_name in ratings_dictionary:
        print(f"""{restaurant_name} is already rated at{ratings_dictionary[
            restaurant_name]} Do you want to update the rating?""")
        user_choice = input("> ").lower()
        if user_choice == 'y' or user_choice == "yes":
            update_rating(restaurant_name)
            return
        else:
            return    
    restaurant_rating = "0"
    while restaurant_rating not in ("1", "2", "3", "4", "5"):
        print("The rating system is 1-5.")
        restaurant_rating = input("Please enter a score for the restaurant: ")
       
    new_line = f"{restaurant_name}:{restaurant_rating}\n"

    # write into file
    with open(chosen_file, "a") as file:
        file.write(new_line)


def update_rating(restaurant_name):
    """Changes the rating for an already reviewed restaurant"""
    restaurant_rating = "0"
    while restaurant_rating not in ("1", "2", "3", "4", "5"):
        print("The rating system is 1-5.")
        restaurant_rating = input("Please enter a score for the restaurant: ")
    with open(chosen_file, "r+") as file:
        all_lines = file.readlines()
        file.seek(0)
        for restaurant_data in all_lines:
            if restaurant_name in restaurant_data:
                file.write(f"{restaurant_name}:{restaurant_rating}\n")
            else:
                file.write(restaurant_data)
        file.truncate()


chosen_file = "scores.txt"
# print_ratings_alphabetically(get_ratings_from_file(sys.argv[1]))
while True:

    print("1. Get restaurant ratings in alphabetical order")
    print("2. Add restaurant rating")
    print("3. Rate a random restaurant")
    print("4. Change save file")
    print("Type q or quit to end program")
    user_choice = input(">").lower()
    if user_choice == "q" or user_choice == "quit":
        break
    if user_choice == "1":
        print_ratings_alphabetically(get_ratings_from_file(chosen_file))
    elif user_choice == "2":
        add_rating()
    elif user_choice == "3":
        # restaurant_list = list(get_ratings_from_file(chosen_file))
        # random_restaurant = restaurant_list[random.randint(0, len(restaurant_list)-1)]
        random_restaurant = random.choice(list(get_ratings_from_file(chosen_file)))
        print(f"You're now reviewing {random_restaurant}")
        update_rating(random_restaurant)
    elif user_choice == "4":
        directories = os.listdir()
        all_txts = [file for file in directories if ".txt" in file]
        print("your options to open are:")
        for index in range(len(all_txts)):
            print(f"{index+1}. {all_txts[index]}")
        while True:
            user_choice = input("> ")
            try:
                save_choice = int(user_choice)
            except ValueError:
                print("Not a number")
                continue
            if save_choice > 0 and save_choice <= len(all_txts):
                chosen_file = all_txts[save_choice-1]
                break

        



    else:
        print("Choose an actual option, jerk")
