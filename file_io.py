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
import csv
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

    with open('PopChange.csv', 'r', newline='') as pop_change:
        # print(f'{"Pop Apr 1":<10}{"Pop Jul 1":<10}{ "Change Pop":>10}')
        reader = csv.reader(pop_change)
        for record in reader:
            id, geo, tgeo1, tgeo2, apr1, jul1, changepop = record
            print(f'\n{apr1:<20}{jul1:<20}{changepop:<10}')

    user_input = input()
    if user_input == 'a':
        print('\ta. Pop Apr 1')
        pop_data()
    elif user_input == 'b':
        print('\tb. Pop Jul 1')
        pop_data()
    elif user_input == 'c':
        print('\tc. Change Pop')
        pop_data()
    elif user_input == 'd':
        main_menu()
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        pop_data()


def house_data():
    print('\nYou have entered Housing Data')
    print('Select the column you want to analyze: \n')
    print('\ta. Age')
    print('\tb. Bedrooms')
    print('\tc. Built')
    print('\td. Rooms')
    print('\te. Utility')
    print('\tf. Exit Column')

    with open('Housing.csv', 'r', newline='') as house_change:
        # print(f'{"Pop Apr 1":<10}{"Pop Jul 1":<10}{ "Change Pop":>10}')
        reader = csv.reader(house_change)
        for record in reader:
            age, bedrms, built, nunits, rooms, weight, utility = record
            print(f'\n{age:<10}{bedrms:<10}{built:<10}{nunits:<10}{rooms:<10}{weight:<20}{utility:<10}')

    user_input = input()
    if user_input == 'a':
        print('\ta. Age')
        house_data()
    elif user_input == 'b':
        print('\tb. Bedrooms')
        house_data()
    elif user_input == 'c':
        print('\tc. Built')
        house_data()
    elif user_input == 'd':
        print('\td. Rooms')
        house_data()
    elif user_input == 'e':
        print('\te. Utility')
        house_data()
    elif user_input == 'f':
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
