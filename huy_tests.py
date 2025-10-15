# SI 201 Project 1
# Your name: Huy Pham
# Your student id: 3483 3492
# Your email: huypham@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# Felicia Wang, John (Yohan) Park
# Used ChatGPT to debug some syntax errors and help write and understand test cases.

import unittest
import csv
import os

from huy_project import (
    calculate_percentage_of_male_penguins_over_threshold,
    calculate_avg_bill_depth_of_male_on_biscoe,
)

class TestHuyMainFunctions(unittest.TestCase):
    """Tests main functions: calculate_percentage_of_male_penguins_over_threshold and
    calculate_avg_bill_depth_of_male_on_biscoe."""

    # ──────────────────────────────────────────────────────────────────────────────
    # Setup and Teardown
    # Has to set up a temporary CSV file for testing because the main functions read from a file
    # ──────────────────────────────────────────────────────────────────────────────
    def setUp(self):
        self.test_csv = "test_penguins.csv"
        with open(self.test_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex", "year"])
            writer.writerow(["Adelie", "Biscoe", "40.0", "18.0", "190", "4600", "male", "2007"])
            writer.writerow(["Adelie", "Biscoe", "NA", "17.5", "185", "4300", "male", "2007"])  # NA bill length
            writer.writerow(["Gentoo", "Biscoe", "50.0", "15.0", "220", "5700", "male", "2007"])
            writer.writerow(["Chinstrap", "Dream", "49.0", "18.0", "195", "4400", "male", "2007"])
            writer.writerow(["Adelie", "Dream", "39.0", "17.0", "180", "3700", "female", "2007"])

    # Clean up the temporary file after tests
    def tearDown(self):
        os.remove(self.test_csv)
        if os.path.exists("test_output.csv"):
            os.remove("test_output.csv")
        if os.path.exists("test_avg.txt"):
            os.remove("test_avg.txt")

    
    # ──────────────────────────────────────────────────────────────────────────────
    # Tests for calculate_percentage_of_male_penguins_over_threshold
    # ──────────────────────────────────────────────────────────────────────────────
    def test_calculate_percentage_of_male_penguins_over_threshold(self):
        calculate_percentage_of_male_penguins_over_threshold(self.test_csv, 4500, "test_output.csv")
        with open("test_output.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)

        self.assertEqual(rows[0], ["species", "percent_heavy"])
        self.assertEqual(rows[1], ["Adelie", "50.00"])     # 1 of 2 valid males > 4500
        self.assertEqual(rows[2], ["Gentoo", "100.00"])    # 1 of 1 > 4500
        self.assertEqual(rows[3], ["Chinstrap", "0.00"])   # 0 of 1 > 4500
    
    # ──────────────────────────────────────────────────────────────────────────────
    # Tests for calculate_avg_bill_depth_of_male_on_biscoe
    # ──────────────────────────────────────────────────────────────────────────────
    def test_calculate_avg_bill_depth_of_male_on_biscoe(self):
        calculate_avg_bill_depth_of_male_on_biscoe(self.test_csv, "test_avg.txt")
        with open("test_avg.txt", "r") as f:
            content = f.read().strip()

        self.assertEqual(content, "Average Bill Length: 45.00 mm")  # Only one valid bill length

    # ──────────────────────────────────────────────────────────────────────────────
    # Tests for edge cases
    # ──────────────────────────────────────────────────────────────────────────────
    def test_no_males(self):
        with open(self.test_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex", "year"])
            writer.writerow(["Adelie", "Biscoe", "40.0", "18.0", "190", "4600", "female", "2007"])
            writer.writerow(["Gentoo", "Biscoe", "50.0", "15.0", "220", "5700", "female", "2007"])

        calculate_percentage_of_male_penguins_over_threshold(self.test_csv, 4500, "test_output.csv")
        with open("test_output.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)

        self.assertEqual(len(rows), 1)  # Only header row
        
    def test_no_males_on_biscoe(self):
        with open(self.test_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex", "year"])
            writer.writerow(["Adelie", "Dream", "40.0", "18.0", "190", "4600", "male", "2007"])
            writer.writerow(["Gentoo", "Torgersen", "50.0", "15.0", "220", "5700", "male", "2007"])

        calculate_avg_bill_depth_of_male_on_biscoe(self.test_csv, "test_avg.txt")
        with open("test_avg.txt", "r") as f:
            content = f.read().strip()

        self.assertEqual(content, "Average Bill Length: 0.00 mm")

if __name__ == "__main__":
    unittest.main()