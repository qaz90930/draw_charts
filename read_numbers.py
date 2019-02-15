import matplotlib.pyplot as plt


def draw_single_line(line):
    coordinates = []
    print(line)
    for x_axis, y_axis in enumerate(line):
        coordinate = [x_axis, y_axis]
        coordinates.append(coordinate)
    # print(coordinates)
    plt.plot([coordinate[0] for coordinate in coordinates], \
             [coordinate[1] for coordinate in coordinates])


def draw_lines(lines):
    print("   ")
    print(lines)
    for line in lines:
        draw_single_line(line)
    plt.show()


def split_numbers(fh):
    lines = None  # don't know how many columns we need

    for line in fh:
        row = line.split(',')
        # Now we know know how many columns
        if lines is None:
            lines = []
            # For each column, add empty array
            for i in range(0, len(row)):
                lines.append([])

        # For each cell, add to the right column in lines
        for column, cell in enumerate(row):
            lines[column].append(int(cell))

    draw_lines(lines)


with open('example.txt', 'r') as fh:
    split_numbers(fh)