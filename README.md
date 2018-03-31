# Natural_Language_Processing_Beginner
A beginner code to the Natural Language Processing doing an sentimental analysis a reports.

Make sure that libraries such as Pandas, urllib, nltk, numpy are installed in the python compiler.

The python version used here in the project is 3.4, any version of Python3 is feasible to run this project.

Compile and Run just the 'master_file.py', to start the project.

Python files - 'data_manipulation.py' and dictionary_create.py' as python files that are called from within the 'master_file.py', so no need to run them separately.

Make sure the files 'cik_list.xlsx', 'MasterDictionary_2014.xlsx' and 'master_file.py' are in the same directory while running the 'master_file.py' file.

Two new files will be generated 'New_cik_list.xlsx' and 'MasterDictionary_editted_2014'.

The final output of the project is stored in 'New_cik_list.xlsx'.

'MasterDictionary_editted_2014' is an intermediatory file.

There are about 150 link in 'cik_list.xlsx' and for the report in each link, the Sentiment Analysis of the text of the report is calculated.

Since each takes about of 2-3 minutes for text analysis on my Machine, it will take almost 8 to 9 hours to complete the whole list.
So , I have just analysed and computed about initial 11-12 links in the file 'cik_list.xlsx' and its console output can be seen in 'console_output.txt'.

This is just an naive approach of the combination of how Data is extracted and in the online fashion without wasting precious machine memory, Text Analysis is done.

'uncertainty_dictionary.xlsx' and 'MasterDictionary_2014.xlsx' and 'constraining_dictionary.xlsx' are the dictionary excel sheet for the sentimental analysis database.
