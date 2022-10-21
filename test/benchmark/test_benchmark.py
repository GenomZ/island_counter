import unittest
import time

from src.island_count import IslandCounter
from src.benchmark.island_count_DFS import IslandCounterDFS
from src.benchmark.island_count_DFS_2 import IslandCounterDFS2


# class SomeTest(unittest.TestCase):
#     def setUp(self):
#         self.startTime = time.time()
#
#     def tearDown(self):
#         t = time.time() - self.startTime
#         print('%s: %.3f' % (self.id(), t))
#
#     def testOne(self):
#         time.sleep(1)
#         self.assertEqual(int('42'), 42)
#
#     def testTwo(self):
#         time.sleep(2)
#         self.assertEqual(str(42), '42')


class TestIslandCounter(unittest.TestCase):
    """
    Simple tests with different input files.
    Checking for the right amount of counted islands per file.
    """

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_normal_case_1(self):
        ic = IslandCounter("data/test_input1")
        self.assertEqual(ic.count_islands(), 0)

    def test_normal_case_2(self):
        ic = IslandCounter("data/test_input2")
        self.assertEqual(ic.count_islands(), 3)

    def test_normal_case_3(self):
        ic = IslandCounter("data/test_input3")
        self.assertEqual(ic.count_islands(), 4)

    def test_normal_case_4(self):
        ic = IslandCounter("data/test_input4")
        self.assertEqual(ic.count_islands(), 7)

    def test_normal_case_5(self):
        ic = IslandCounter("data/test_input5")
        self.assertEqual(ic.count_islands(), 1)

    def test_normal_case_6(self):
        ic = IslandCounter("data/test_input6")
        self.assertEqual(ic.count_islands(), 6)

    def test_normal_case_7(self):
        ic = IslandCounter("data/test_input7")
        self.assertEqual(ic.count_islands(), 84096)


class TestIslandCounterDFS(unittest.TestCase):
    """
    Simple tests with different input files.
    Checking for the right amount of counted islands per file.
    """

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_normal_case_1(self):
        ic = IslandCounterDFS("data/test_input1")
        self.assertEqual(ic.count_islands(), 0)

    def test_normal_case_2(self):
        ic = IslandCounterDFS("data/test_input2")
        self.assertEqual(ic.count_islands(), 3)

    def test_normal_case_3(self):
        ic = IslandCounterDFS("data/test_input3")
        self.assertEqual(ic.count_islands(), 4)

    def test_normal_case_4(self):
        ic = IslandCounterDFS("data/test_input4")
        self.assertEqual(ic.count_islands(), 7)

    def test_normal_case_5(self):
        ic = IslandCounterDFS("data/test_input5")
        self.assertEqual(ic.count_islands(), 1)

    def test_normal_case_6(self):
        ic = IslandCounterDFS("data/test_input6")
        self.assertEqual(ic.count_islands(), 6)

    def test_normal_case_7(self):
        ic = IslandCounterDFS("data/test_input7")
        self.assertEqual(ic.count_islands(), 84096)


class TestIslandCounterDFS2(unittest.TestCase):
    """
    Simple tests with different input files.
    Checking for the right amount of counted islands per file.
    """

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_normal_case_1(self):
        ic = IslandCounterDFS2("data/test_input1")
        self.assertEqual(ic.count_islands(), 0)

    def test_normal_case_2(self):
        ic = IslandCounterDFS2("data/test_input2")
        self.assertEqual(ic.count_islands(), 3)

    def test_normal_case_3(self):
        ic = IslandCounterDFS2("data/test_input3")
        self.assertEqual(ic.count_islands(), 4)

    def test_normal_case_4(self):
        ic = IslandCounterDFS2("data/test_input4")
        self.assertEqual(ic.count_islands(), 7)

    def test_normal_case_5(self):
        ic = IslandCounterDFS2("data/test_input5")
        self.assertEqual(ic.count_islands(), 1)

    def test_normal_case_6(self):
        ic = IslandCounterDFS2("data/test_input6")
        self.assertEqual(ic.count_islands(), 6)

    def test_normal_case_7(self):
        ic = IslandCounterDFS2("data/test_input7")
        self.assertEqual(ic.count_islands(), 84096)


if __name__ == "__main__":
    unittest.main()
