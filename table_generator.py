import tg_functions
import os
def DrawTitle():
    print(' _         _____   __   __  _____     _     _        _____                           _             ')
    print('| |       |_   _|  \ \ / / |_   _|   | |   | |      |  __ \                         | |            ')
    print('| |     __ _| | ___ \ V /    | | __ _| |__ | | ___  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ ')
    print('| |    / _` | |/ _ \/   \    | |/ _` | \'_ \| |/ _ \ | | __ / _ \ \'_ \ / _ \ \'__/ _` | __/ _ \| \'__|')
    print('| |___| (_| | |  __/ /^\ \   | | (_| | |_) | |  __/ | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   ')
    print('\_____/\__,_\_/\___\/   \/   \_/\__,_|_.__/|_|\___|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   ')
    print('\n\n\n')
    print('NOTE: Please refer to the README.md in the GitHub repo for instructions for use.')
    print('\n\n\n')

# Draw the tile
DrawTitle()

file_name = input("\t>>> Please input the path of the file: ")

if ".txt" in file_name:
    if os.path.isfile(file_name):
        output_table_file_name = tg_functions.GenerateTableFromFile(file_name)
        print(f"\n\n\t>>> Your file has been created!\n\n\t>>> It has been saved to {output_table_file_name}\n\n\n")
    else:
        print("\n\n\tERROR: A problem has occured, please try again.\n\n\n")
else:
    print("\n\n\tERROR: A problem has occured, please try again.\n\n\n")



                                                                                                   
                                                                                               