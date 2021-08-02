import os

# MAIN DRIVER FUNCTION
def GenerateTableFromFile(filename = ""):
    #print("GENERATE TABLE FROM FILE")

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

# Import csv
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
    #print("PARSE INPUT FILE")
    file = ReplaceUnderscores(file)
    rows = file.split("\n") # Split the string by "\n" to get rows
    return rows
    

#================================================================
#================================================================

# Get size of csv
def GetSize(row_one = ""):
    #print("GET SIZE")
    #length = len(row_one.split(","))
    length = len(row_one.split("\t"))
    #print(f"Length = {length}")
    return length

#================================================================
#================================================================

# Generate code holder
def GenerateCodeHolder(col = 1):
    #print("GENERATE CODE HOLDER")
    l = "l" * col
    top = "\\begin{tabular}{" + l + "}\n"
    bot = "\\end{tabular}\n"

    return top, bot

#================================================================
#================================================================

# Generate table row
def GenerateRow(row = ""):
    #print("GENERATE ROW")
    #variables = "\t" + row.replace(",", " & ") + "\\\\\n"
    variables = "\t" + row.replace("\t", " & ") + "\\\\\n"
    return variables
    
#================================================================
#================================================================

# Generate file and return name
def GenerateFile(table = ""):
    user_file_name = input("\n\t>>> Output file name: ")
    user_file_name = user_file_name + '.tex'
    out_path = os.path.join(os.path.realpath(__file__))
    t_path = os.path.join("/Outputs", user_file_name)
    out_path = out_path.replace('/tg_functions.py', t_path)
    #tg_functions.py/Outputs/out.txt
    output_file = open(out_path, "w")
    output_file.write(table)
    output_file.close()
    return out_path

#================================================================
#================================================================

# Generate table
def GenerateTable(num_cols, rows = []):
    #print("GENERATE TABLE")
    #Get the top and bot rows
    top, bot = GenerateCodeHolder(num_cols)
    #print(f"TOP={top}\nBOT={bot}")
    #Get the row contents
    row_contents = ""
    for r in rows:
        #print(r)
        row_contents = row_contents + GenerateRow(r)
    #print(f"ROW_CONTENTS={row_contents}")
    #Output the file
    table = top + row_contents + bot
    #print(table)
    #Return the name of the file
    return GenerateFile(table)