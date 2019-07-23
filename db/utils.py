def convertTuple(tup):
    """Convert a tuple to a string"""
    string = ','.join(tup)
    return string


def return_values(values_list):
    string = ''
    for value in values_list:
        if type(value) is int:
            string = string + "," + str(value)
        else:
            string = string + ",'" + value + "'"
    if string[0] == ',':
        string = string[1:]
    return string
