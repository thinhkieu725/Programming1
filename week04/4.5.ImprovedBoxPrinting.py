"""
COMP.CS.100 Programming 1
4.5.ImprovedBoxPrinting.py
Creator: Thinh Kieu
Student number: 152167613
"""

def print_box(width, height, border_mark = "#", inner_mark = " "):
    """
    print out the box
    variables:
        height _ int _ number of rows
        width _ int _ number of columns
        border_mark _ char _ print mark for the border _ set default = "#"
        inner _ char _ print mark for the inner part _ set default = " "
    return: none
    """
    for i in range(height):
        if i == 0 or i == height - 1:
            for j in range(width):
                print(border_mark, sep = "", end = "")
        else:
            for j in range(width):
                if j == 0 or j == width - 1:
                    print(border_mark, sep = "", end = "")
                else:
                    print(inner_mark, sep = "", end = "")
        print()
    print()
def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
