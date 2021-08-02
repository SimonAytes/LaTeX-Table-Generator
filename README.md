# LaTeX-Table-Generator

## Description

Creating tables in LaTeX is a labor-intensive provess that is prone to errors. This program remedies this by allowing you to generate a table in a matter of seconds. By inputting a tab-delimited `.txt` file, this program generates a `.tex` file containing a table with default formatting.

# Running the application

## Creating a tab-delimited file

Because this program only accepts tab-delimited `.txt` files, it is very important that you make sure to export your Excel Workbook as one. Follow the steps below to learn how to do this:

1. In Excel, go to **File -> Save As**.
2. After specifying a name for your file, click the dropdown and select "Tab delimited text (.txt)".


![Screen Shot 2021-08-02 at 4 29 25 PM](https://user-images.githubusercontent.com/44680601/127925051-aaa13d66-eac0-405b-92ff-1806ac04294f.png)

4. Click **Save**. _(NOTE: If you are prompted with a data-loss warning, ignore it and continue)_

5. Done! Now you can use this file to generate a LaTeX table.

## Operation

To start using LaTeX-Table-Generator, follow the steps below:

1. Clone the GitHub repository to your local computer (learn how [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)).
2. Open Terminal and navigate to the location of the repository.
3. In Terminal, type `python table_generator.py`. Hit enter.
4. Before continuing, confirm that your Terminal window looks like the picture below _(NOTE: You may have to resize your console window)_

![Screen Shot 2021-08-02 at 4 38 03 PM](https://user-images.githubusercontent.com/44680601/127922809-ede64ceb-feec-409f-978e-3fe24be27257.png)

5. Enter the full system path of your tab-delimeted file. Hit enter.

![Input Target Path](https://user-images.githubusercontent.com/44680601/127922775-a973818d-8133-4001-9441-653c2641fc17.png)

7. When prompted, enter the name of the output file **without** extension (it will output as a `.tex` file). Hit enter.

![Screen Shot 2021-08-02 at 4 59 12 PM](https://user-images.githubusercontent.com/44680601/127923100-b4c65954-e3c5-45be-bb01-3dcf24147cdd.png)

9. The file has been created! Your Terminal window should look like the picture below.

![Finished Example](https://user-images.githubusercontent.com/44680601/127923928-d7843e74-df0d-4ba2-91b4-3533f0f3d797.png)

11. Locate the output file in the `/Outputs/` folder within the repository directory.

![Output File](https://user-images.githubusercontent.com/44680601/127923941-05b9764c-2b0b-413c-83a4-941338cc5b2f.png)

You can now open the `.tex` file in your preferred LaTeX environment. Below is an example of a generated table in TexStudio.

![TexStudio Table](https://user-images.githubusercontent.com/44680601/127924123-4640aa64-2eb2-4837-99a1-1ba5f4e1cb62.png)

## Errors

The picture below shows the only error message this application provides.

![Error Message](https://user-images.githubusercontent.com/44680601/127922348-6d76fb10-c35f-4b35-9b71-02f0e7b048d7.png)

The most common causes of this error are:
- Input file is not a `.txt` file
- Input file is not tab-delimited
- Input file does not exist
- File path is wrong

If your issues still persists, please create an issue on the GitHub project's page, providing details and pictures as necessary.

# Contact

[Send me an email](mailto:simon.aytes@lc.cuny.edu?subject=[GitHub]%20LatexTableGenerator%20Issue) **or** contact me via my [personal site](https://www.saytes.io).
