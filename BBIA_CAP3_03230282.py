################################
# https://github.com/chophel777/03230282_BIA101_CAP3
# Sonam Chophel
# BBI A
# 03230282
################################
# REFERENCES
# https://stackoverflow.com/questions/67631131/how-do-i-read-numbers-from-a-text-file-in-python
# https://stackoverflow.com/questions/12838549/how-can-i-concatenate-two-integers-in-python
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score: <481237>
################################

import re  # Importing the 're' module for regular expression operations

def read_input(file_name):  # Define a function named read_input that takes one argument: file_name
    with open(file_name, 'r') as file:  # Open the file specified by file_name in read mode ('r')
        lines = file.readlines() # Read all lines from the opened file and store them in the variable 'lines'
    return lines # Return the list of lines read from the file


def extract_two_digit_number(line): # Function to extract a two-digit number from a given string
    digits = re.findall(r'\d', line) # Using regular expression to find all digits in the variable 'line' and store them in the list 'digits'
    if len(digits) < 2: # Check if the length of the list 'digits' is less than 2
        return 0  # Return 0 if there are less than 2 digits in the list
    first_digit = digits[0] # Assigning the first digit of the 'digits' list to the variable 'first_digit'
    last_digit = digits[-1] # Assigning the last digit of the 'digits' list to the variable 'last_digit'
    return int(first_digit + last_digit) # Returning the integer value obtained by joining the 'first_digit' and 'last_digit'

def calculate_total_sum(file_name):  # Define a function to calculate the total sum from a file
    lines = read_input(file_name) # Read the input from the specified file
    total_sum = 0 # Initialize the total sum variable to zero
    for line in lines: # Iterate through each line in the list of lines
        total_sum += extract_two_digit_number(line)  # Extract a two-digit number from the current line and add it to the total sum
    return total_sum # Return the final total sum after iterating through all lines

def print_solution(file_name): # Defines a function named print_solution that takes a file name as input
    total_sum = calculate_total_sum(file_name) # Calls a function to calculate the total sum from the contents of the given file
    print(f"The total sum from the given input file {file_name} is {total_sum}") # Prints the total sum obtained from the file

# Example usage
if __name__ == "__main__": # Checks if the script is being run as the main program
    input_file_name = '282.txt' # Assigns the name of the input file to a variable
    print_solution(input_file_name) # Calls a function to print the solution using the input file


