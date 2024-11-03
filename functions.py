# custom function:
FILEPATH = "names.txt"


def get_names(filepath=FILEPATH):
    # docstring:
    """ Read a text file and return
    the list of the names."""
    with open(filepath, "r") as file_local:
        names_local = file_local.readlines()
        return names_local


def write_names(local_names, filepath=FILEPATH):
    """ Write a name in the list of the names."""
    with open(filepath, "w") as file_local:
        file_local.writelines(local_names)


if __name__ == "__main__":
    print("HAHAHAHAHA")
    print(get_names())
