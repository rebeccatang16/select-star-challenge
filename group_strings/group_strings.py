import json
import re
import sys


def get_all_prefixes(input_string):
    # Return a list of all possible prefixes for a string
    matches = re.finditer(r"([a-zA-Z0-9]+).?", input_string)
    prefixes = []
    curr_prefix = ""
    for match in matches:
        prefixes.append(curr_prefix + match.group(1))
        curr_prefix = curr_prefix + match.group(0)
    return prefixes


def group_strings(input_strings):
    # Sort first so that prefix strings always end up being encountered
    # first, before other strings that would be grouped with them
    input_strings.sort()

    groups = {}
    for input_string in input_strings:
        prefix = prefix_match(input_string, groups)
        if prefix:
            groups[prefix].append(input_string)
        else:
            groups[input_string] = [input_string]

    return groups


def prefix_match(input_string, groups):
    # Given a string and a dict with existing prefixes as keys,
    # return the string's prefix that already exists as a key
    # or None if it isn't found.
    for prefix in get_all_prefixes(input_string):
        if groups.get(prefix):
            return prefix
    return None


def write_to_json(input_strings, destination="grouped_strings.json"):
    groups = group_strings(input_strings)
    with open(destination, "w") as write_file:
        json.dump(groups, write_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: group_strings.py CSV_FILENAME DESTINATION")
        exit(1)
    
    with open(sys.argv[1], "r") as csv_file:
        # For sake of time, just assume items in csv file are separated
        # by newline
        input_strings = csv_file.read().split("\n")

    write_to_json(input_strings, sys.argv[2])
