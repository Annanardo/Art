"""
This module is the one that tests all the 4 functions
necessary to let the user interact with the database.
Each Test Case tests a Known valid and invalid entries.
tearDown and setUp functions were used as well
to set up mock variables and csv files needed
to test the functions.
"""

import unittest
from checking import Check
import inserter as ins
import similarities as sim
import pandas as pd


class TestName(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
        print(db)
        ind = db.loc[db["Name"] == "Bansky"].index.values
        db.drop(db.index[ind[0]], inplace=True)
        print(db)

    def setUp(self):
        self.T_artist = "Claude Monet"
        self.T_painting = "Impression, Sunrise"
        self.F_artist = "Claude"
        self.F_painting = "11"
        self.new_artist = "Bansky"
        self.database = "artists_paintings.csv"
        self.column = "Nationality"
        self.parameter = "German - Swiss"

    def test_correct_check_artist(self):
        self.assertEqual(Check().check_artist(self.T_artist), True)

    def test_wrong_check_artist(self):
        self.assertEqual(Check().check_artist(self.F_artist), False)
        self.assertEqual(Check().check_artist(self.T_painting), False)
        self.assertEqual(Check().check_artist(self.F_painting), False)

    def test_correct_check_paintings(self):
        self.assertEqual(Check().check_paintings(self.T_painting), True)

    def test_wrong_check_paintings(self):
        self.assertEqual(Check().check_paintings(self.T_artist), False)
        self.assertEqual(Check().check_paintings(self.F_painting), False)

    def test_inserter(self):
        test1 = print("Sorry, but " + self.T_artist +
                      " is already present in the database, thank you anyway")
        self.assertEqual(test1, ins.add_element(self.T_artist))
        test2 = print("Sorry, but " + self.T_painting +
                      " is already present in the database, thank you anyway")
        self.assertEqual(test2, ins.add_element(self.T_painting))
        test3 = print("Thank you for your contribution!")
        self.assertEqual(test3, ins.add_element(self.new_artist, "a"))

    def test_correct_similarities(self):
        self.assertEqual(sim.similarities(self.column, self.parameter), True)

# by setting this up we can run this file
# on the command line without having
# having to call the unittest module.

if __name__ == "__main__":
    unittest.main()