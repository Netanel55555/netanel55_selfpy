from datetime import date

my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
           "hobbies": ["Sing", "Compose", "Act"]}


def add_tuple_date(input_dict):
    day = int(input_dict["birth_date"][0:2])
    month = int(input_dict["birth_date"][3:5])
    year = int(input_dict["birth_date"][6:10])
    birth_date_tuple = (month, day, year)
    input_dict["birth_date"] = birth_date_tuple


def add_age(input_dict):
    input_dict["age"] = date.today().year - input_dict["birth_date"][2] + int(
        date.today().year < input_dict["birth_date"][1])


def actions_on_dict(num):
    """Performs a specific action on the dictionary based on the input number."""

    if num == 1:
        print(my_dict["first_name"] + " " + my_dict["last_name"])
    elif num == 2:
        print(my_dict["birth_date"][3:5])
    elif num == 3:
        print(len(my_dict["hobbies"]))
    elif num == 4:
        print(my_dict["hobbies"][-1])
    elif num == 5:
        print(my_dict["hobbies"][-1])
    elif num == 6:
        add_tuple_date(my_dict)
    elif num == 7:
        my_dict["hobbies"].append("Cooking")
    elif num == 8:
        print(my_dict["birth_date"])
    elif num == 9:
        add_age(my_dict)
    else:
        print("Invalid action number")


actions_on_dict(1)