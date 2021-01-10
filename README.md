# SYStool
command line python script which allows for some basic txt and sql operations, without using argparse for arguments.

!!!IMPORTANT!!!
SQLTESTING.PY, VALUES.TXT, TEST.DB ARE ALL TEST FILES, AND ARE NOT TO BE USED FOR GENERAL PURPOSE DUE TO THEIR ROUGH AND UNPOLISHED NATURE!

The purpose of this project was to write a small command line tool which can combine txts, manipulate dbs and convert the SQL data to txt and vice versa.
as of current, this tool can only combine two txts together.
I am still learning, so forgive me for any bugs.

SYStool.py is best run through command line, as previously mentioned.
it is launched by typing: python SYStool.py (filetype argument) (operation argument) (files)

the currently supported file type is txt, triggered with -txt in the command line

the currently supported operation arguments are "-c" and "-v". 
-c stands for "combine", and will combine any txts after it into one txt, which will be called "combinedx.txt" the x is an integer, from 0 to infinity.
the value of x depends on whether or not you already have a file called combinedx.txt in the folder your cmd is targeting. 
to put it shortly, the value of x counts up from zero until it finds a non-taken file name, so as to ensure it does not overwrite a pre-existing file.

-v stands for "validate", and simply checks if the txts are openable. This is performed automatically anyways, and adding -v just stops the program after validation

with this in mind, and example input therefore looks like: 
python SYStool.py -txt -c file1.txt file2.txt file3.txt
this would combine the contents of file1.txt, file2.txt, and file3.txt into a new combinedx.txt file 

I will be adding more functionality soon, however this is a pet project designed to work on my machine, and under certain conditions only.
Therefore, please do not send me messages about how using argparse would be better, or how my code does not allow for the program to be run via command line inputs in the python IDLE, because meeting those criteria are not my goals

If you enjoy this project, and would like me to bring it out of the pet project category, and instead create an actual open-source tool (which would probably use argparse lol), please contact me as while I have no intentions of doing so, outside demand could change my mind.
