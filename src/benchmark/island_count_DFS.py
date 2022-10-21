import sys

from utils.read_file import read_file


class IslandCounterDFS:
    """
    Alternative algorithm for the Island Counter assignment with Depth First Search (DFS) algorithm implemented.
    """
    def __init__(self, file_path):
        self.COL = None
        self.ROW = None
        self.data_split_as_int = []
        self.file_path = file_path
        self.island_count = 0

    def is_safe(self, i, j, visited_tiles):
        """
        A function to check if a given cell (row, col) can be included in DFS
        row number is in range, column number is in range and value is 1 and not yet visited
        """
        return (
                0 <= i < self.ROW
                and 0 <= j < self.COL
                and not visited_tiles[i][j]
                and self.data_split_as_int[i][j]
        )

    def dfs(self, i, j, visited_tiles):
        """
        A utility function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours
        as adjacent vertices.
        These arrays are used to get row and column numbers of 8 neighbours of a given cell
        """
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited_tiles[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited_tiles):
                self.dfs(i + row_nbr[k], j + col_nbr[k], visited_tiles)

    def count_islands(self) -> int:
        """
        The main function that return count of islands in a given boolean 2D matrix
        """
        self.data_split_as_int = read_file(self.file_path)
        self.ROW = len(self.data_split_as_int)
        self.COL = len(self.data_split_as_int[0])

        # Make a bool array to mark visited cells. Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and traverse through the all cells of given matrix
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, then new island found
                if visited[i][j] is False and self.data_split_as_int[i][j] == 1:
                    # Visit all cells in this island and increment island count
                    self.dfs(i, j, visited)
                    self.island_count += 1

        return self.island_count


if __name__ == "__main__":
    island_counter = IslandCounterDFS(sys.argv[1])
    print(island_counter.count_islands())
