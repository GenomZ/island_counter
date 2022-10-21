# Island Counter Python Project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

----

# Read Me

This is a recruitment project for a position of Python Developer.

To install the package execute the following in the main directory:

    pip install .

This will confirm the minimum required packages are present.

To run the code use the island_counter.sh file that accepts a path to an input file as such:

    ./island_counter.sh <path_to_your_file>

Example with test file from /data directory:
    
    ./island_counter.sh data/test_input7

Which will result in 84096 being sent to STDOUT.

----

# Unit Tests

To run unit tests with the sample files provided in /data please use the following command 
in the main directory of the repo:

    python3 -m unittest test.test_island_counter.TestIslandCounter

The routine checks with provided files if the program detects correct number of islands.
Additionally, tests are performed on the read_file method, if it returns correct 2D binary array and
if the input arrays have all rows with the same length and if all characters are 1's or 0's correctly converted to int.

File test_input7 was made bigger than 1MB to check for memory issues. None were found.
test_wrong_input2 is testing non-ASCII characters. Also, no issues found.

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

This will display time per test and makes visible the execution time difference between implementations 
with the use of test files

----

# Additional Notes

Repository [black](https://pypi.org/project/black/) was used to reformat the code up to current formatting standard.

    black <repository_directory>


In case of an error executing the island_counter.sh with the message:

    syntax error: unexpected end of file

Run dos2unix command on the island_counter.sh file.
