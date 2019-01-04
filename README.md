# Logs Analysis

This project builds a summary of the following information from the tables in the news database:
* The three most popular articles of all time
* The most popular article authors of all time
* Days with a spike in http request errors

## Usage

After placing the logsdb.py folder into the folder containing the required newsdata, 
and vagrant files, simply run `python logsdb.py`. The program will print the report in the order outlined above.

## Config

To present the results for a specific question, scroll to the bottom of logsdb.py and comment out the functions that you do not want displayed. The default configuration is:

```
questionOne()
questionTwo()
questionThree()
```