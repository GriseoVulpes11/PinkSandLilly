import dill


# Adds a dictionary to the PSL.p file
def add_to_file(dict):
    try:
        dill.dump(dict, open("PSL.p", "wb"))
    except:
        return 1

# Retrieves the dictionary from the PSL.p file
def Retrieve_from_file():
    try:
        return dill.load(open("PSL.p", "rb"))
    except:
        return 1
