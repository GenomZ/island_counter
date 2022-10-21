from utils.eprint import eprint_and_quit


def read_file(file_path):
    """
    Reads the input file specified in the console for the bash script

    The file is read and converted to a list of rows.
    Each row is then split into a list of ints per obtained row.
    The whole binary 2D array is passed to count_islands

    Routine is in place that checks if all the rows in the array are of the same length
    and if the only characters in the array are only zeros (ASCII character 48)
    and ones (ASCII character 49) and end-of-line.

    If the array has uneven lengths of rows the routine will communicate to STDERR and terminate.

    If the input data has characters other than specified above or that they cannot be converted to int
    the routine will communicate to STDERR and terminate.

    If the provided file path is invalid and the file cannot be found the routine
    will communicate to STDERR and terminate.
    :return:
    """
    data_split_as_int = []
    try:
        with open(file_path) as f:
            data_from_file = f.read().split()
            reference_line_length = len(data_from_file[0])
            for line_from_file in data_from_file:
                if len(line_from_file) != reference_line_length:
                    eprint_and_quit(
                        "ERROR: The provided input does not have all the rows of the same length!"
                    )
                temporary_row = []
                for character_in_line in line_from_file:
                    if character_in_line != "0" and character_in_line != "1":
                        eprint_and_quit(
                            "ERROR: Provided input has characters that are not 0, 1 "
                            "or next line character!"
                        )
                    try:
                        temporary_row.append(int(character_in_line))
                    except TypeError:
                        eprint_and_quit(
                            "ERROR: The provided input array has characters that cannot"
                            " be converted to int!"
                        )
                data_split_as_int.append(temporary_row)
    except FileNotFoundError:
        eprint_and_quit(
            "ERROR: The provided file path is incorrect or the file in the specified location"
            " does not exist!"
        )

    return data_split_as_int
