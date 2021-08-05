# Import libraries
import os

#================================================================
#================================================================

# MAIN DRIVER FUNCTION
def GenerateTableFromFile(filename = ""):
    #Retrieve the contents of the file and no. columns
    contents, num_cols = ImportFile(filename)

    #Generate the table
    output_file_name = GenerateTable(num_cols, contents)

    return output_file_name


#================================================================
#================================================================

# Fix Underscores
def ReplaceUnderscores(contents = ""):
    return contents.replace("_", "\\_")

#================================================================
#================================================================

# Import file
def ImportFile(filename = ""):
    f = open(filename)
    file = f.read() #Import the file as string
    f.close()
    rows = ParseInputFile(file) #Get the rows as a list
    num_cols = GetSize(rows[0]) #Get the number of columns

    return rows, num_cols

#================================================================
#================================================================

# Parse the input file
def ParseInputFile(file = ""):
    file = ReplaceUnderscores(file)
    rows = file.split("\n") # Split the string by "\n" to get rows
    return rows
    

#================================================================
#================================================================

# Get size of csv
def GetSize(row_one = ""):
    length = len(row_one.split("\t"))
    return length

#================================================================
#================================================================

# Generate code holder
def GenerateCodeHolder(col = 1):
    l = "l" * col
    top = "\\begin{tabular}{" + l + "}\n"
    bot = "\\end{tabular}\n"

    return top, bot

#================================================================
#================================================================

# Generate table row
def GenerateRow(row = ""):
    variables = "\t" + row.replace("\t", " & ") + "\\\\\n"
    return variables
    
#================================================================
#================================================================

# Generate file and return name
def GenerateFile(table = ""):
    # Get output file name from user and format it
    user_file_name = input("\n\t>>> Output file name: ")
    user_file_name = user_file_name + '.tex'
    
    # Create the final output path
    out_path = os.path.join(os.path.realpath(__file__))
    t_path = os.path.join("/Outputs", user_file_name)
    out_path = out_path.replace('/tg_functions.py', t_path)

    # Create the output file and write to it
    output_file = open(out_path, "w")
    output_file.write(table)
    output_file.close()

    # Return the output path
    return out_path

#================================================================
#================================================================

# Generate table
def GenerateTable(num_cols, rows = []):
    #Get the top and bot rows
    top, bot = GenerateCodeHolder(num_cols)

    #Get the row contents
    row_contents = ""
    for r in rows:
        row_contents = row_contents + GenerateRow(r)

    #Output the file
    table = top + row_contents + bot

    #Return the name of the file
    return GenerateFile(table)

#================================================================
#================================================================

# Draw title (UI)
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