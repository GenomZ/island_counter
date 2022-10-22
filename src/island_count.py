import sys

from utils.read_file import read_file
from utils.eprint import eprint_and_quit


class IslandCounter:
    """
    Island Counter is a simple program to count islands of ones ("1") in a 2D binary array on the sea of zeros ("0")
    """

    def __init__(self, file_path):
        self.data_split_as_int = []
        self.file_path = file_path
        self.island_count = 0

    def count_islands(self) -> int:
        """
        Actual routine for counting the islands in the input files.
        Accepts the binary 2D array from self.read_file
        Iterates through every value in the array.
        Marks all the visited LAND tiles (value: 1) as -1 and adds to the count of island.
        If a tile with value of 1 has a neighbour, it does not add to island count thus all neighbouring 1's
        are counted as one island.

        The order of range in y_coordinate is reversed to scan the array from the bottom left corner
        in the fashion of an x,y coordinate system.

        If reading the input file fails, the routine returns -1.
        The function checks all the neighbouring cells separately with a try, to bypass neighbours that are beyond
        the boundaries of the array. The order was chosen arbitrary, but finding any -1's around stops the scan
        and moves the procedure further, either to increment island counter, or continue scanning the array.
        :return:
        """
        self.data_split_as_int = read_file(self.file_path)
        if self.data_split_as_int == -1:
            eprint_and_quit("ERROR: There was an issue reading the input file!")
        for y_coordinate in reversed(range(len(self.data_split_as_int))):
            for x_coordinate in range(len(self.data_split_as_int[0])):
                if self.data_split_as_int[y_coordinate][x_coordinate] == 1:
                    self.data_split_as_int[y_coordinate][x_coordinate] = -1

                    # Check all neighbouring fields in array if the value is -1
                    # if it is, do not count this 1 as a new island and continue the scan
                    # x, y+1
                    try:
                        if self.data_split_as_int[y_coordinate + 1][x_coordinate] == -1:
                            continue
                    except IndexError:
                        pass

                    # x, y-1
                    try:
                        if self.data_split_as_int[y_coordinate - 1][x_coordinate] == -1:
                            continue
                    except IndexError:
                        pass

                    # x+1, y
                    try:
                        if self.data_split_as_int[y_coordinate][x_coordinate + 1] == -1:
                            continue
                    except IndexError:
                        pass

                    # x-1, y
                    try:
                        if self.data_split_as_int[y_coordinate][x_coordinate - 1] == -1:
                            continue
                    except IndexError:
                        pass

                    # Diagonals:
                    # x+1, y+1
                    try:
                        if (
                            self.data_split_as_int[y_coordinate + 1][x_coordinate + 1]
                            == -1
                        ):
                            continue
                    except IndexError:
                        pass

                    # x+1, y-1
                    try:
                        if (
                            self.data_split_as_int[y_coordinate - 1][x_coordinate + 1]
                            == -1
                        ):
                            continue
                    except IndexError:
                        pass

                    # x-1, y+1
                    try:
                        if (
                            self.data_split_as_int[y_coordinate + 1][x_coordinate - 1]
                            == -1
                        ):
                            continue
                    except IndexError:
                        pass

                    # x-1, y-1
                    try:
                        if (
                            self.data_split_as_int[y_coordinate - 1][x_coordinate - 1]
                            == -1
                        ):
                            continue
                    except IndexError:
                        pass

                    self.island_count += 1

        return self.island_count


if __name__ == "__main__":
    island_counter = IslandCounter(sys.argv[1])
    print(island_counter.count_islands())
