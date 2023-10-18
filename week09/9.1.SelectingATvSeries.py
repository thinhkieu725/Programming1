"""
COMP.CS.100 Programming 1.
9.1.SelectingATvSeries.py
Creator: Thinh Kieu
Student id number: 152167613
"""
def read_file(fileName):
    """
    read the file and return the file handle.
    Param: fileName _ string _ name of the file
    return: fHandle: the file handle
    """
    try:
        readFile = open(fileName, "r")
        return readFile
    except OSError:
        print(f"Reading the file {fileName} was not successful.")
        return None


def main():
    # Open the file to read
    fileName = input("Enter the name of the file: ")
    readFile = read_file(fileName)
    if readFile is None:
        return

    # Define the nested data structure: A dictionary of lists.
    genres = dict()

    # Read through the lines in the file and process
    for file_line in readFile:
        file_line = file_line.rstrip()
        MovieAndGenres = file_line.split(";")
        movie = MovieAndGenres[0]
        movieGenres = MovieAndGenres[1].split(",")

        for g in movieGenres:
            if g in genres:
                genres[g].append(movie)
            else:
                genres.update({g: [movie]})



    #Print out
    availableGenres = sorted(genres)
    print("Available genres are:", ", ".join(availableGenres))

    readFile.close()

    inquiredGenre = ""
    while True:
        inquiredGenre = input("> ")
        inquiredGenre = inquiredGenre.strip()
        if inquiredGenre == "exit":
            return
        elif inquiredGenre in genres:
            for m in sorted(genres[inquiredGenre]):
                print(m)


if __name__ == "__main__":
    main()
