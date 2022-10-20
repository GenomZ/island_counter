import sys


class IslandCounter:
    """
    Island Counter is a simple program to count islands o ones ("1") in a 2D binary array on the sea of zeros ("0")
    """
    def __init__(self, file_path):
        self.data_split_as_int = []
        self.file_path = file_path
        self.island_count = 0

    def read_file(self):
        """
        Reads the input file specified in the console for the bash script

        The file is read and converted to a list of rows.
        Each row is then split into a list of ints per obtained row.
        The whole binary 2D array is passed to self.count_islands

        Routine is in place that checks if all the rows in the array are of the same length
        and if the only characters in the array are only zeros (ASCII character 48)
        and ones (ASCII character 49) and end-of-line"
        :return:
        """
        with open(self.file_path) as f:
            data_from_file = f.read().split()
            reference_line_length = len(data_from_file[0])
            for line_from_file in data_from_file:
                if len(line_from_file) != reference_line_length:
                    return -1
                temporary_row = []
                for character_in_line in line_from_file:
                    if character_in_line != "0" and character_in_line != "1":
                        return -1
                    try:
                        temporary_row.append(int(character_in_line))
                    except TypeError:
                        return -1
                self.data_split_as_int.append(temporary_row)

        return self.data_split_as_int

    def count_islands(self):
        """
        Actual routine for counting the islands in the input files.
        Accepts the binary 2D array from self.read_file
        Iterates through every value in the array.
        Marks all the visited LAND tiles (value: 1) as -1 and adds to the count of island.
        If a tile with value of 1 has a neighbour, it does not add to island count.

        The order of range in y_coordinate is reversed to scan the array from the bottom left corner
        as in the coordinate system.

        If reading the input file fails, the routine returns -1.
        :return:
        """
        self.data_split_as_int = self.read_file()
        if self.data_split_as_int == -1:
            return -1
        for y_coordinate in reversed(range(len(self.data_split_as_int))):
            for x_coordinate in range(len(self.data_split_as_int[0])):
                if self.data_split_as_int[y_coordinate][x_coordinate] == 1:
                    self.data_split_as_int[y_coordinate][x_coordinate] = -1
                    """x, y+1"""
                    try:
                        if self.data_split_as_int[y_coordinate + 1][x_coordinate] == -1:
                            continue
                    except IndexError:
                        pass
                    """x, y-1"""
                    try:
                        if self.data_split_as_int[y_coordinate - 1][x_coordinate] == -1:
                            continue
                    except IndexError:
                        pass
                    """x+1, y"""
                    try:
                        if self.data_split_as_int[y_coordinate][x_coordinate + 1] == -1:
                            continue
                    except IndexError:
                        pass
                    """x-1, y"""
                    try:
                        if self.data_split_as_int[y_coordinate][x_coordinate - 1] == -1:
                            continue
                    except IndexError:
                        pass

                    """Diagonals: x+1, y+1"""
                    try:
                        if self.data_split_as_int[y_coordinate + 1][x_coordinate + 1] == -1:
                            continue
                    except IndexError:
                        pass

                    """x+1, y-1"""
                    try:
                        if self.data_split_as_int[y_coordinate - 1][x_coordinate + 1] == -1:
                            continue
                    except IndexError:
                        pass
                    """x-1, y+1"""
                    try:
                        if self.data_split_as_int[y_coordinate + 1][x_coordinate - 1] == -1:
                            continue
                    except IndexError:
                        pass
                    """x-1, y-1"""
                    try:
                        if self.data_split_as_int[y_coordinate - 1][x_coordinate - 1] == -1:
                            continue
                    except IndexError:
                        pass

                    self.island_count += 1

        return self.island_count


if __name__ == '__main__':
    island_counter = IslandCounter(sys.argv[1])
    print(island_counter.count_islands())
