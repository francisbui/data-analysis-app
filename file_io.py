"""
 * Francis Bui
 * SDEV 300
 * Professor Chris Howard
 * Lab 4 - Matrix Application (with Validation)
 * Sept 18, 2020
 * The purpose of this program is to validate inputs by the user using Python Regular
 * Expression. Additionally it will also performs mathematical operations using Numpy
 * and Pandas (if necessary) on 3 by 3 matrices. User will choose between the math
 * options which will output the results onto the console along with the transpose
 * and average for each respective rows and columns.
"""

import sys
import re
import numpy as np
# import pandas as pd


def main_menu():
    """
    Main Menu function
    Executes first and after every function excepts when the user exits
    :return:
    """
    print('Select the file you want to analyze: \n')
    print('\t1. Population Data')
    print('\t2. Housing Data')
    print('\t3. Exit the Program')

    user_input = input()
    if user_input == '1':
        pop_data()
    elif user_input == '2':
        house_data()
    elif user_input == '3':
        exit_program()
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        main_menu()


def pop_data():
    print('\nYou have entered Population Data')
    print('Select the column you want to analyze: \n')
    print('\ta. Pop Apr 1')
    print('\tb. Pop Jul 1')
    print('\tc. Change Pop')
    print('\td. Exit Column')

    user_input = input()
    if user_input == 'a':
        pop_data()
    elif user_input == 'b':
        house_data()
    elif user_input == 'c':
        exit_program()
    elif user_input == 'd':
        main_menu()
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        pop_data()


def house_data():
    print('\nYou have entered Housing Data')
    print('Select the column you want to analyze: \n')
    print('\ta. Pop Apr 1')
    print('\tb. Pop Jul 1')
    print('\tc. Change Pop')
    print('\td. Exit Column')

    user_input = input()
    if user_input == 'a':
        pop_data()
    elif user_input == 'b':
        house_data()
    elif user_input == 'c':
        exit_program()
    elif user_input == 'd':
        main_menu()
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        house_data()


def exit_program():
    """
    Exit Function
    Thank the user and exits the system
    :return:
    """
    print('')
    print('{:*^80}'.format(''))
    print('{:^80}'.format(' Thank you for using the Python Data Analysis Application '))
    print('{:^80}'.format(' We hope you try it again very soon '))
    print('{:*^80}'.format(''))
    print('')
    sys.exit()


# Application begins here
print('')
print('{:*^80}'.format(''))
print('{:^80}'.format(' Welcome to the '))
print('{:^80}'.format(' Python Data Analysis Application '))
print('{:*^80}'.format(''))
print('')

main_menu()
