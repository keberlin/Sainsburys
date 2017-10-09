Application to parse csv files.

Each csv file will have 2 lines, the first line will have a header describing which columns each of the days (mon-fri) will reside along with a description. The second line will have the values associated with each of the days.

To run the application:

python parse.py

The application will parse all files in the current directory with a .csv suffix.

The output will contain an extry for each csv file parsed. Each file will list the valies and descriptions for each day mon to fri.
