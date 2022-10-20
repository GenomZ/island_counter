# Island Counter Python Project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

----

This is a recruitment project for a position of Python Developer.

To install the package execute the following in the main directory:

    pip install .

This will confirm the minimum required packages are present (which is quite cert as no external packages were used).


I have found two implementations of Depth First Search (DFS) algorithm for the solution of this problem on top
of the solution I made myself to the best of my ability.

    Source: https://www.geeksforgeeks.org/find-number-of-islands/

Unit testing on the DFS implementations shows that for the provided test files the suggested routines are slower
than what I have implemented.
This sparks joy.

To run unit tests with the sample files provided in /data please use the following command:

    python3 -m unittest test.test_island_counter.TestIslandCounter

To run tests with the two DFS implementations please execute:

    DFS:    python3 -m unittest test.test_island_counter_DFS.TestIslandCounter
    DFS_2:  python3 -m unittest test.test_island_counter_DFS_2.TestIslandCounter

If there are no issues all seem to mean everything works!
