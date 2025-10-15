# SI 201 Project 1
# Your name: Huy Pham
# Your student id: 3483 3492
# Your email: huypham@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# Felicia Wang, John (Yohan) Park
# Used ChatGPT to debug some syntax errors and help write and understand test cases.

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
# OUTPUT: list_of_males (list of dicts)
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
# OUTPUT: list_of_Biscoe (list of dicts)
# This function takes in a list of penguin dictionaries and returns a new list
# containing only the dictionaries where the "island" key has the value "Biscoe". 
def filter_by_Biscoe(penguins):
        
    # Initialize an empty list to store the Biscoe penguins.
    list_of_Biscoe = []
    
    # Loops through each penguin in the list.
    for penguin in penguins:
        if penguin["island"] == "Biscoe":
            list_of_Biscoe.append(penguin)
            
    return list_of_Biscoe

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


# INPUT: penguins (dicionary of lists of dictionaries), threshold (int)
# OUTPUT: percent dictionary (dict)
# This function calculates the percentage of penguins that have a body mass greater
# than the given threshold. It returns a dictionary with the species as keys and
# the percentage of heavy penguins as values.
def calculate_heavy_penguins(penguins, threshold):
    
    percent_dict = {}
    
    for species, penguin_list in penguins.items():
        
        total_count = len(penguin_list)
        percent_dict[species] = 0
        
        if total_count == 0:
            continue
        
        for penguin in penguin_list:
            if penguin["body_mass_g"] == "NA":
                continue
            if int(penguin["body_mass_g"]) > threshold:
                percent_dict[species] += 1 
                
        percent_dict[species] = (percent_dict[species] / total_count) * 100       
        
    return percent_dict

# INPUT: penguins (list of dicts)
# OUTPUT: average_bill_length (float)
# This function calculates the average bill length of the penguins in the list.
def calculate_average_bill_length(penguins):
    
    total_bill_length = 0
    count = 0
    
    for penguin in penguins:
        if penguin["bill_length_mm"] == "NA":
            continue
        total_bill_length += float(penguin["bill_length_mm"])
        count += 1
        
    if count == 0:
        return 0.0
    
    average_bill_length = total_bill_length / count
    return average_bill_length

# INPUT: percent_dict (dict), filename (str)
# OUTPUT: None
# This function writes the species and their corresponding percentage of heavy
# penguins to a CSV file with the given filename.
def Write_Percent_To_CSV(percent_dict, filename):
    
    # Open the file for writing.
    outFile = open(filename, 'w', newline='')
    writer = csv.writer(outFile)
    
    # Write the header row.
    writer.writerow(["species", "percent_heavy"])
    
    # Write each species and its corresponding percentage.
    for species in percent_dict:
        writer.writerow([species, f"{percent_dict[species]:.2f}"])
    
    # Close the file.
    outFile.close()
    
def write_average_bill_length_to_txt(average_bill_length, filename):
    # Open the file for writing.
    outFile = open(filename, 'w')
    
    # Write the average bill length to the file.
    outFile.write(f"Average Bill Length: {average_bill_length:.2f} mm\n")
    
    # Close the file.
    outFile.close()
    
# Main functions to perform the required tasks
def calculate_percentage_of_male_penguins_over_threshold(input_file, threshold, output_file):
    #calling all the helper functions
    penguins = read_penguins_csv(input_file)
    males = filter_by_males(penguins)
    grouped = group_by_species(males)
    percent_dict = calculate_heavy_penguins(grouped, threshold)
    Write_Percent_To_CSV(percent_dict, output_file)
    
# Main functions to perform the required tasks
def calculate_avg_bill_depth_of_male_on_biscoe(input_file, output_file):
    #calling all the helper functions
    penguins = read_penguins_csv(input_file)
    males = filter_by_males(penguins)
    Biscoes = filter_by_Biscoe(males)
    avg_bill_lngth = calculate_average_bill_length(Biscoes)
    write_average_bill_length_to_txt(avg_bill_lngth, output_file)

def main():
    file_path = "penguins.csv"
    outfile_1 = "heavy_male_penguins.csv"
    threshold = 4500
    calculate_percentage_of_male_penguins_over_threshold(file_path, threshold, outfile_1)
    
    outfile_2 = "avg_bill_length_biscoe.txt"
    calculate_avg_bill_depth_of_male_on_biscoe(file_path, outfile_2)    

if __name__ == '__main__':
    main()
