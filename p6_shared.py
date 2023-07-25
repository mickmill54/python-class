def pad_left(input,integer):
    i = 0
    while i < integer:
        input = " " + input
        i += 1
    return input

def pad_right(input_str, size):
    i = 0
    while len(input_str) < size:
        input_str += " "
        i += 1
    return input_str


