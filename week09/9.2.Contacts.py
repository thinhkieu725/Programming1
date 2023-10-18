"""
COMP.CS.100 Programming 1.
9.2.Contacts.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def read_file(fileName):
    """
    read the file and return the nested data structure of contacts.
    Param: fileName _ string _ name of the file
    return: fHandle: the nested data structure
    """
    try:
        readFile = open(fileName, "r")
    except OSError:
        print(f"Reading the file {fileName} was not successful.")
        return None

    # Define the nested data structure: A dictionary of lists.
    contacts = dict()

    # Loop through file lines
    line0 = True            # check whether it's the first line
    for fLine in readFile:
        if line0 == True:
            line0 = False
            continue
        fLine = fLine.strip()
        processList = fLine.split(";")
        infos = {"name": processList[1], "phone": processList[2], "email": processList[3]}
        try:
            infos.update({"skype": processList[4]})
        except:
            pass
        contacts.update({processList[0]: infos})

    return contacts
def main():
    print(read_file("contacts.csv"))

if __name__ == "__main__":
    main()
