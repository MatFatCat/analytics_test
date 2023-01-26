import pandas as pd


def get_procentage_from_item_description(description):
    split_description = description.split()
    proc = ""
    size = len(split_description)

    for i in range(size):

        if '%' in split_description[i]:

            if len(split_description[i]) == 1:
                proc = split_description[i - 1]
            else:
                proc = split_description[i]
            if '%' in proc:
                proc = proc.replace("%", "")
            if ',' in proc:
                proc = change_comma_to_dot(proc)

    return float(proc)


def change_comma_to_dot(string):
    listed_string = list(string)

    for i in range(len(string)):
        if listed_string[i] == ',':
            listed_string[i] = '.'

    new_string = ''.join(listed_string)

    return new_string


print(get_procentage_from_item_description("Сыр Король Эдвард с ароматом топлёного молока, массовой долей жира в сухом веществе 46,56 %"))

milk_products = pd.read_csv("/Users/matthewpopov/Desktop/clean_database/milk_catalogs_items.csv", encoding="utf-8",
                            on_bad_lines="skip")

