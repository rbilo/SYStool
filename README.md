# SYStool
Command line python script which allows for some basic txt and sql operations, without using argparse for arguments.

!!!IMPORTANT!!!
TESTING FILES IN THE TESTING FOLDER ARE ROUGH AND UNFINISHED. I DO NOT RECCOMEND USING THEM FOR SENSETIVE TASKS.

TXTS USED IN CONJUNCTION WITH DBS HAVE TO BE FORMATTED VERY SPECIFICALLY IN ORDER TO PREVENT DATA LOSS (format guide below)

The purpose of this project was to write a small command line tool which can combine txts, manipulate dbs and convert the SQL data to txt and vice versa.
As of current, this tool can combine two (or more) txts together, and add the contents of a txt into a db.
The script of SYStool.py is submitted "programmer done", meaning it works, but not elegantly, and certianly not very efficiently.
Once all functions are implimented to the script, I will begin to optimise the code.
I am still learning, so forgive me for any bugs.

SYStool.py is best run through command line, as previously mentioned.
it is launched by typing: python SYStool.py (filetype argument) (operation argument) (files)

The currently supported file types are txt and db, triggered with -txt and -db in the command line respectively.
-txt and -db will mean different things for different functions, read below

The currently supported operation arguments are "-c", "-v", and "-a". 
-c stands for "combine", and will combine any txts after it into one txt, which will be called "combinedx.txt" the x is an integer, from 0 to infinity.
The value of x depends on whether or not you already have a file called combinedx.txt in the folder your cmd is targeting. 
To put it shortly, the value of x counts up from zero until it finds a non-taken file name, so as to ensure it does not overwrite a pre-existing file.
Only txt files are supported with -c.

-v stands for "validate", and simply checks if the txts are openable. This is performed automatically anyways, and adding -v just stops the program after validation
-txt and -db work with validate, you can call -db and use the function only to validate txt files, and vice versa. 

-a stands for "add to". calling -a in the command line will add the contents of a specifically formatted txt to a database. the amount of txts is unlimited, but the function is currently poorly optimised. 
This is not to say it would take hours to add gbs of data to a db, but rather that it could be faster. 
-a is limited to only adding into one table of the db per call of the program. I hope to create a more functional -a in future commits.
-a only works with ONE database file. call -db to use -a, then include your database file. after this, include your txt files
An example use of -a is as follows: 
python SYStool.py -db -a database.db file1.txt file2.txt 

An example input therefore looks like: 
python SYStool.py -txt -c file1.txt file2.txt file3.txt
This would combine the contents of file1.txt, file2.txt, and file3.txt into a new combinedx.txt file 

TXT formatting for -a function:
Any txt files you submit have to be formatted very specifically for the function to work. failure to do so will result in errors out the wazzoo, and potential loss of data.
Take an example database with the table "COMPANY", and five columns inside the "COMPANY". these columns are titled ID, NAME, AGE, ADDRESS, SALARY. (you can find this db in the testing folder).
The -a function assumes automatically that the first column is the ID, and that all IDs must be unique. therefore, the function auto-generates IDs, and IDs should not be included in your txt. 
The rest of the columns must be included in your txt. 
If you wanted to add an entry into your db where the Name is "Richard", the age is 20, the Address is "Montague", and the salary is 45000.00, you would have the following as one line in your txt:
'Richard', 20, 'Montague', 45000.00
The next entry would be on an immediately consecutive line, blank lines will result in error. 
As you can see, string must have inverted commas around it in order to be entered properly. 
Double quotation marks, "", will not work, and will result in an error with the auto-generated SQL command, as -a uses "" to concatenate.
In order to see a practical working example of formatting, see test.db and values.txt in the testing folder of this repository.

I will be adding more functionality soon

If you enjoy this project, and would like to help me bring it out of the pet project category, please message me.
