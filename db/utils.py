def convertTuple(tup):
    """Convert a tuple to a string"""
    string = ','.join(tup)
    return string


def return_values(values_list):
    """Return string that can be used in sql command"""
    string = ''
    for value in values_list:
        if type(value) is int:
            string = string + "," + str(value)
        else:
            string = string + ",'" + value + "'"
    if string[0] == ',':
        string = string[1:]
    return string


def sql_from_dict(dict_values):
    """Return string that can be used in sql command"""
    string = ''
    for key, value in dict_values.items():
        if type(value) is int:
            string = string + f"{key}={value},"
        else:
            string = string + f"{key}='{value}',"
    if string[-1] == ',':
        string = string[:-1]
    return string
