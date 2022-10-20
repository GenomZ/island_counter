import sys


# Program to count islands in boolean 2D matrix
class IslandCounter:
    """
    Alternative algorithm for the Island Counter assignment with Depth First Search (DFS) algorithm implemented.
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
        # A function to check if a given cell
        # (row, col) can be included in DFS
        def is_safe(i, j, visited):
            # row number is in range, column number
            # is in range and value is 1
            # and not yet visited
            return (0 <= i < self.ROW and
                    0 <= j < self.COL and
                    not visited[i][j] and self.data_split_as_int[i][j])

        # A utility function to do DFS for a 2D
        # boolean matrix. It only considers
        # the 8 neighbours as adjacent vertices
        def dfs(i, j, visited):

            # These arrays are used to get row and
            # column numbers of 8 neighbours
            # of a given cell
            rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
            colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

            # Mark this cell as visited
            visited[i][j] = True

            # Recur for all connected neighbours
            for k in range(8):
                if is_safe(i + rowNbr[k], j + colNbr[k], visited):
                    dfs(i + rowNbr[k], j + colNbr[k], visited)

        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and traverse
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.data_split_as_int[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    dfs(i, j, visited)
                    self.island_count += 1

        return self.island_count


if __name__ == '__main__':
    island_counter = IslandCounter(sys.argv[1])
    print(island_counter.count_islands())