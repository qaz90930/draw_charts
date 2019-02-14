import matplotlib.pyplot as plt

def line_chart(line_1, line_2):

    def draw_line_1(line_1):
        coordinates_line_1 = []
        for x_axis, y_axis in enumerate(line_1):
            coordinate = [x_axis, y_axis]
            coordinates_line_1.append(coordinate)
        plt.plot([coordinate[0] for coordinate in coordinates_line_1],\
                 [coordinate[1] for coordinate in coordinates_line_1])

    def draw_line_2(line_2):
        coordinates_line_2 = []
        for x_axis, y_axis in enumerate(line_2):
            coordinate = [x_axis, y_axis]
            coordinates_line_2.append(coordinate)

        plt.plot([coordinate[0] for coordinate in coordinates_line_2],\
                 [coordinate[1] for coordinate in coordinates_line_2])
        plt.show()

    draw_line_1(line_1)
    draw_line_2(line_2)

def split_numbers(fh):
    line_1 = []
    line_2 = []
    for line in fh:
        column_1, column_2= line.split(',')
        line_1.append(int(column_1))
        line_2.append(int(column_2))
    line_chart(line_1, line_2)

with open('example.txt', 'r') as fh:
    split_numbers(fh)
