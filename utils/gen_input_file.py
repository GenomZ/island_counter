import sys
import random
from eprint import eprint_and_quit


def gen_input_file(num_rows=100, num_col=50, land_probability=0.1):
    """
    If a custom sized test input is required, this can create it with specified array size and amount of 1's
    Default values are defined in the method if no arguments are given to the script in the console.

    Console usage:
        python3 utils/gen_input_file.py <number_of_rows> <number_of_columns> <land_tile_probability>

    Example:
        python3 utils/gen_input_file.py 100 50 0.1

    Or with no parameters for default values of 100, 50, 0.1
    """
    try:
        if len(sys.argv) == 2:
            num_rows = int(sys.argv[1])
        if len(sys.argv) == 3:
            num_rows = int(sys.argv[1])
            num_col = int(sys.argv[2])
        if len(sys.argv) == 4:
            num_rows = int(sys.argv[1])
            num_col = int(sys.argv[2])
            land_probability = float(sys.argv[3])
    except ValueError:
        eprint_and_quit("ERROR: Provide appropriate numbers to be converted to int, int, float in order.")

    with open("data/test_input_generated", "w") as f:
        for row in range(num_rows):
            temp_row = ""
            for col in range(num_col):
                is_land = random.random()
                if is_land < land_probability:
                    temp_row += "1"
                else:
                    temp_row += "0"

            if row != num_rows - 1:
                temp_row += "\n"

            f.write(temp_row)

    print(
        f"Created data/test_input_generated file with:\n"
        f" - {num_rows} rows\n"
        f" - {num_col} columns\n"
        f" - {num_rows * num_col} total tiles\n"
        f" - {land_probability} probability for a land tile"
    )


gen_input_file()
