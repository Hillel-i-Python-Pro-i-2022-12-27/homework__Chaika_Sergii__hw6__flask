import csv

from application.config.path import FILES_OUTPUT_PATH


def average_value_from_csv(name_file: str = "output") -> str:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{name_file}.csv")
    with open(path_to_file) as file:
        dict_reader = csv.DictReader(file)
        sum_average_height = 0.0
        sum_average_weight = 0.0
        for row in dict_reader:
            sum_average_height += float(row[' "Height(Inches)"'].strip())
            sum_average_weight += float(row[' "Weight(Pounds)"'].strip())
        average_height_cm = round((sum_average_height / int(row["Index"])) * 2.54, 1)
        average_weight_kg = round((sum_average_weight / int(row["Index"])) * 0.45, 1)
        return f"Average height in cm {average_height_cm} , average weight in kg {average_weight_kg}"

if __name__ == "__main__":
    average_value_from_csv()
