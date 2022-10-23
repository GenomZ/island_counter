# Island Counter Python Project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

----

This is a recruitment project for the position of Python Developer.

# Read Me

The package requires [Python 3.7+](https://www.python.org/downloads/release/python-3108/) to run.

To confirm you have the correct version of Python and pip, execute the following in the main directory:

    pip install -r requirements

To confirm Your pip version is >=20.

----

# Running the code

To run the code use the island_counter.sh file that accepts a path to an input file as such:

    ./island_counter.sh <path_to_your_file>

Example with test file from /data directory:
    
    ./island_counter.sh data/test_input7

Which will result in 84096 being sent to STDOUT.

Or for all files in /data:

    for i in data/test*; do ./island_counter.sh $i; done


The script was modified with a solution that changes the directory it is executed into the project directory.

    SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
    cd $(echo "$SCRIPT_DIR" | tr -d '\r') || exit

It is done due to the absolute imports of the package components 
so that the functionality is only possible from the project directory if not added to PYTHONPATH.

Paths provided to the bash script should be either relative to the project directory
or absolute system paths

    ~/island_counter/island_counter.sh ~/island_counter/data/test_input7

or
    
    ~/island_counter/island_counter.sh data/test_input7

If the package folder is in the home directory.



In an extreme case where compatible python is not available, provided docker image can be used after installing docker
and executing:

    sudo docker load --input island_counter.tar

Then in the island_counter.sh uncomment docker run command and comment python3 command.

    sudo docker run -i --rm island_counter ./island_counter.sh "$1"

----

# Unit Tests

To run unit tests with the sample files provided in /data please use the following command 
in the main directory of the repo:

    python3 -m unittest test.test_island_counter.TestIslandCounter

The routine checks with provided files if the program detects the correct number of islands.
Additionally, tests are performed on the read_file method, if it returns correct 2D binary array and
if the input arrays have all rows with the same length and if all characters are 1s or 0s correctly converted to int.


File test_input7 was made bigger than 7.4MB with 7355392 characters (0s and 1s) with 84096 islands to check for memory issues. 
None were found.

Additional inputs were prepared that were not included in the repo, and tested with no issues:
    - 73.6MB, 73553920 characters, 840960 islands
    - 1.0GB, 1000000000 characters, 65617638 islands

An additional script was included to create a test input of manual size. It was used to generate the 1GB test file.
It accepts a number of rows and columns and the probability of a land tile. The number of islands will be random,
depending on the placement of the land tiles in the file.

Usage:

    python3 utils/gen_input_file.py <number_of_rows> <number_of_columns> <land_tile_probability>

Example:

    python3 utils/gen_input_file.py 100 50 0.1

Or with no parameters for default values of 100, 50, 0.1

And test it with:

    ./island_counter.sh data/test_input_generated


The file test_wrong_input2 is testing non-ASCII characters. Also, no issues were found.

All errors are communicated to STDERR and terminate the python script.

----

# Benchmark

Additionally, I have found [two implementations of Depth First Search (DFS)](https://www.geeksforgeeks.org/find-number-of-islands/) algorithm for the solution of this problem on top
of the solution I made myself to the best of my ability.

Timed unit testing on the two versions of DFS shows that for the provided test files the suggested routines are slower
than what I have implemented.

This sparks joy.

Additionally, to run timed tests of my implementation and the two DFS implementations please execute:

    python3 -m unittest test.benchmark.test_benchmark

This will display the time per test and makes visible the execution time difference between implementations 
with the use of test files

----

# Additional Notes

Repository [black](https://pypi.org/project/black/) was used to reformat the code up to the current formatting standard.

    black <repository_directory>


The bash script was tested in an old bash shell and has been updated with Linux's new line character.
In case of an error executing the island_counter.sh with the message:

    syntax error: unexpected end of file

Run dos2unix command on the island_counter.sh file to convert text file line endings between CRLF and LF.

    dos2unix island_counter.sh


The file was made executable, and adequate command for the GIT repository was added to keep it executable.
if for some reason the bash script cannot be executed as:

    ./island_counter.sh <path_to_your_file>

Execute command:

    chmod +x island_counter.sh

Git command executed to prevent this issue:

    git update-index --chmod +x island_counter.sh
