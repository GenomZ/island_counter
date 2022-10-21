import sys

from utils.read_file import read_file


class IslandCounterDFS2:
    """
    Alternative algorithm for the Island Counter assignment with Depth First Search (DFS) algorithm implemented.
    Here without the use of 'visited matrix' array.
    """

    def __init__(self, file_path):
        self.COL = None
        self.ROW = None
        self.data_split_as_int = []
        self.file_path = file_path
        self.island_count = 0

    def dfs(self, x_coordinate, y_coordinate):
        """
        A utility function to do DFS for a 2D boolean matrix.
        It only considers the 8 neighbours as adjacent vertices
        """
        if (
                x_coordinate < 0
                or x_coordinate >= len(self.data_split_as_int)
                or y_coordinate < 0
                or y_coordinate >= len(self.data_split_as_int[0])
                or self.data_split_as_int[x_coordinate][y_coordinate] != 1
        ):
            return

        # mark it as visited
        self.data_split_as_int[x_coordinate][y_coordinate] = -1

        # Recur for 8 neighbours
        self.dfs(x_coordinate - 1, y_coordinate - 1)
        self.dfs(x_coordinate - 1, y_coordinate)
        self.dfs(x_coordinate - 1, y_coordinate + 1)
        self.dfs(x_coordinate, y_coordinate - 1)
        self.dfs(x_coordinate, y_coordinate + 1)
        self.dfs(x_coordinate + 1, y_coordinate - 1)
        self.dfs(x_coordinate + 1, y_coordinate)
        self.dfs(x_coordinate + 1, y_coordinate + 1)

    def count_islands(self):
        """
        The main function that returns count of islands in a given boolean 2D matrix
        """
        self.data_split_as_int = read_file(self.file_path)
        self.ROW = len(self.data_split_as_int)
        self.COL = len(self.data_split_as_int[0])

        # Initialize count as 0 and traverse through the all cells of given matrix
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, then new island found
                if self.data_split_as_int[i][j] == 1:
                    # Visit all cells "in" this island and increment island count
                    self.dfs(i, j)
                    self.island_count += 1

        return self.island_count


if __name__ == "__main__":
    island_counter = IslandCounterDFS2(sys.argv[1])
    print(island_counter.count_islands())
