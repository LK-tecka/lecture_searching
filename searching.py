import os
import json
with open("sequential.json", "r") as fileseg:
    data = json.load(fileseg)
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    with open(file_name, "r") as fileseg:
        data = json.load(fileseg)
    if field not in data:
        return None
    return data[field]
    """
    
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)




def main():
    sequential_data= read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    pass


if __name__ == '__main__':
    main()