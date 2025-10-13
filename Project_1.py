# SI 201 Project 1
# Your name: Huy Pham
# Your student id: 3483 3492
# Your email: huypham@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# Felicia Wang, John (Yohan) Park

import os
import unittest
import csv

# INPUT: file_path (str): The path to the penguins.csv file.
# OUTPUT: list of dictionaries, where each dictionary represents a row in the CSV file.
# This function reads the penguins.csv file and returns a list of dictionaries
# where each dictionary represents a row in the CSV file.
# Including: Species, Island, Bill Length (mm), Bill Depth (mm), 
#            Flipper Length (mm), Body Mass (g), Sex, and Year.
def read_penguins_csv(file_path):
    
    # Initialize an empty list to store the dictionaries.
    list_of_dicts = []
    
    # Open the CSV file and read its contents.
    inFile = open(file_path, 'r')
    penguins = csv.reader(inFile)
    
    # Skip the header row.
    header = next(penguins)
    
    # Loops through each row.
    for row in penguins:
        # Initialize an empty dictionary for each row.
        penguin_dict = {}
        # Loops through each column in the row, creating a key and value pair
        for i in range(len(header)):
            penguin_dict[header[i].strip()] = row[i].strip()
        # Adds the dictionary to the list.
        list_of_dicts.append(penguin_dict)  
            
    # Close the file.
    inFile.close()  
    
    return list_of_dicts


# INPUT: penguins (list of dicts)
# OUTPUT: male_penguins (list of dicts)
# This function takes in a list of penguin dictionaries and returns a new list
# containing only the dictionaries where the "Sex" key has the value "male".    
def filter_by_males(penguins):
    
    # Initialize an empty list to store the male penguins.
    list_of_males = []
    
    # Loops through each penguin in the list.
    for penguin in penguins:
        if penguin["sex"] == "male":
            list_of_males.append(penguin)
            
    return list_of_males

# INPUT: penguins (list of dicts)
# OUTPUT: species_dict (dict of lists)
# This function takes in a list of penguin dictionaries and returns a dictionary
# where the keys are the unique species of penguins and the values are lists of
# dictionaries representing the penguins of that species.
def group_by_species(penguins):
    
    species_dict = {}
    
    for penguin in penguins:
        species = penguin["species"]
        if species not in species_dict:
            species_dict[species] = []
        
        species_dict[species].append(penguin)
        
    return species_dict
        

def main():

    if __name__ == '__main__':
        main()