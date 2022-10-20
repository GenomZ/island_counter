import sys


class IslandCounter:
    """
    Alternative algorithm for the Island Counter assignment with Depth First Search (DFS) algorithm implemented.
    Here without the use of 'visited matrix'.
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

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def count_islands(self):
        self.data_split_as_int = self.read_file()
        self.ROW = len(self.data_split_as_int)
        self.COL = len(self.data_split_as_int[0])
        # A utility function to do DFS for a 2D
        # boolean matrix. It only considers
        # the 8 neighbours as adjacent vertices
        def DFS(i, j):
            if i < 0 or i >= len(self.data_split_as_int) or j < 0 or j >= len(self.data_split_as_int[0]) or self.data_split_as_int[i][j] != 1:
                return

            # mark it as visited
            self.data_split_as_int[i][j] = -1

            # Recur for 8 neighbours
            DFS(i - 1, j - 1)
            DFS(i - 1, j)
            DFS(i - 1, j + 1)
            DFS(i, j - 1)
            DFS(i, j + 1)
            DFS(i + 1, j - 1)
            DFS(i + 1, j)
            DFS(i + 1, j + 1)
        # Initialize count as 0 and traverse
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if self.data_split_as_int[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    DFS(i, j)
                    self.island_count += 1

        return self.island_count
