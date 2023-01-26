def get_procentage_from_item_description(description):

    if type(description) == float or '%' not in description:
        return "No Data"

    split_description = description.split()
    proc = ""
    size = len(split_description)
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(size):

        if '%' in split_description[i]:
            if len(split_description[i]) == 1:
                proc = split_description[i - 1]
            else:
                no_numbers = False
                for j in range(len(split_description[i])):
                    if split_description[i][j] in nums:
                        no_numbers = False
                        break
                    else:
                        no_numbers = True

                if no_numbers is True:
                    proc = split_description[i - 1]
                else:
                    proc = split_description[i]

            if '%' in proc:
                proc = proc.replace("%", "")
            if ',' in proc:
                proc = change_comma_to_dot(proc)
            try:
                float(proc)
            except ValueError as _:
                listed_proc = list(proc)
                for k in range(len(proc)):
                    if listed_proc[k] not in nums:
                        if k+1 not in range(len(proc)) or (listed_proc[k] == '.' or listed_proc[k-1] not in nums
                                                           or listed_proc[k+1] not in nums):
                            listed_proc[k] = ''
                        elif listed_proc[k] != '.':
                            listed_proc[k] = ''
                        else: pass

                proc = ''.join(listed_proc)

    if proc == '':
        return "No Data"

    return float(proc)


def change_comma_to_dot(string):
    listed_string = list(string)

    for i in range(len(string)):
        if listed_string[i] == ',':
            if i + 1 not in range(len(string)):
                listed_string[i] = ''
            else:
                listed_string[i] = '.'

    new_string = ''.join(listed_string)

    return new_string



