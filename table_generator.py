import tg_functions
import os

#================================================================
#                       MAIN PROGRAM
#================================================================

# Draw the tile
tg_functions.DrawTitle()

# Get the target file name
file_name = input("\t>>> Please input the path of the file: ")

# Check if the file is a .txt file
if ".txt" in file_name:
    # Check if the file exists
    if os.path.isfile(file_name):
        # Generate table and print success message
        output_table_file_name = tg_functions.GenerateTableFromFile(file_name)
        print(f"\n\n\t>>> Your file has been created!\n\n\t>>> It has been saved to {output_table_file_name}\n\n\n")
    # If it does not exist, throw an error
    else:
        print("\n\n\tERROR: A problem has occured, please try again.\n\n\n")
# If it is not a .txt file, print error message
else:
    print("\n\n\tERROR: A problem has occured, please try again.\n\n\n")



                                                                                                   
                                                                                               