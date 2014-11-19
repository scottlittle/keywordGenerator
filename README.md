keywordGenerator
================

Takes in a single keyword and generates related keywords indefinitely.  Tested in iPython notebooks and made into regular .py file.  

This program first takes in a keyword and generates a definition on Wordnet.  Then, it takes this definition and puts it into the aiOne alpha website.  Since there is no API for getting data from this site, a python module called Selenium was used to extract the final generated keywords.  Finally, these outputs keywords are run as input keywords until the user stops the process.

The purpose of this code is to generate related keywords (and keywords of those keywords).
