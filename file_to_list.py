def file_to_list():

    # empty list to read list from a file
    names = []
    # open file and read the content in a list
    with open(r'data_name.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            names.append(x)

    # display list
    return names