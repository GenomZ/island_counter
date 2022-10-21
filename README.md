# Island Counter Python Project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

----

# Read Me

This is a recruitment project for a position of Python Developer.

To install the package execute the following in the main directory:

    pip install .

This will confirm the minimum required packages are present (which is quite cert as no external packages were used).

To run the code use the island_counter.sh file that accepts a path to an input file as such:

    ./island_counter.sh <path_to_your_file>

Example with test file from /data directory:
    
    ./island_couter.sh data/test_input7



I have found two implementations of Depth First Search (DFS) algorithm for the solution of this problem on top
of the solution I made myself to the best of my ability.

    Source: https://www.geeksforgeeks.org/find-number-of-islands/

Unit testing on the DFS implementations shows that for the provided test files the suggested routines are slower
than what I have implemented.

This sparks joy.

----

# Unit Tests

To run unit tests with the sample files provided in /data please use the following command 
in the main directory of the repo:

    python3 -m unittest test.test_island_counter.TestIslandCounter

To run tests with the two DFS implementations please execute:

    DFS:    python3 -m unittest test.test_island_counter_DFS.TestIslandCounter
    DFS_2:  python3 -m unittest test.test_island_counter_DFS_2.TestIslandCounter

If there are no issues all seem to mean everything works!
