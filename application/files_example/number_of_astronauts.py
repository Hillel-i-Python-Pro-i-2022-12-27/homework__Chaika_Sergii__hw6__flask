import json

from homework__Chaika_Sergii__hw6__flask.application.config.path import FILES_OUTPUT_PATH


def number_of_astronaut(name_file: str = "output") -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{name_file}.json")
    with open(path_to_file) as file:
        response_dict = json.load(file)
    number_of_astronaut = response_dict["number"]
    answer = f"The number of people in space at this moment: {number_of_astronaut} astronauts."
    print(answer)
    return f"The number of people in space at this moment: {number_of_astronaut} astronauts"

if __name__ == "__main__":
    number_of_astronaut()

